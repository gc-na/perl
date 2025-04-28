import os
import re
import time
import logging
import sqlite3
import json
import openai

# DB 파일명 및 seed 파일 경로
DB_FILE = "articles.db"
SEED_FILE = "seed.json"

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def init_db():
    """기존 DB 파일이 있다면 삭제하고, 새 스키마로 articles 테이블을 생성합니다."""
    if os.path.exists(DB_FILE):
        logging.info("기존 데이터베이스 파일 삭제: %s", DB_FILE)
        os.remove(DB_FILE)
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            programming_language TEXT,
            article_language TEXT,
            article TEXT,
            meta_description TEXT,
            meta_keywords TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(topic, programming_language, article_language)
        )
        """)
        conn.commit()

def cache_lookup(topic: str, programming_language: str, article_language: str):
    """DB에서 (topic, programming_language, article_language) 조합의 캐시된 결과를 조회합니다."""
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute(
            "SELECT article, meta_description, meta_keywords FROM articles WHERE topic=? AND programming_language=? AND article_language=?",
            (topic, programming_language, article_language)
        )
        row = c.fetchone()
    if row:
        return {"article": row[0], "meta_description": row[1], "meta_keywords": row[2]}
    return None

def cache_save(topic: str, programming_language: str, article_language: str, article: str, meta_description: str, meta_keywords: str):
    """생성된 기사를 DB에 저장(또는 갱신)합니다."""
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        try:
            c.execute(
                "INSERT OR REPLACE INTO articles (topic, programming_language, article_language, article, meta_description, meta_keywords) VALUES (?, ?, ?, ?, ?, ?)",
                (topic, programming_language, article_language, article, meta_description, meta_keywords)
            )
            conn.commit()
        except Exception as e:
            logging.error(f"DB 저장 에러 ({topic} / {programming_language} / {article_language}): {e}")

def slugify(text: str) -> str:
    """파일명에 안전한 슬러그를 생성합니다."""
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)

def extract_keywords(text: str, num_keywords: int = 5) -> str:
    """
    단순한 방식으로 기사의 핵심 단어를 추출합니다.
    (Stopwords를 제외하고 빈도수가 높은 단어를 선택)
    """
    stopwords = set(["the", "and", "of", "in", "to", "a", "is", "for", "on", "with", "by", "an", "it", "this", "that", "as", "are"])
    words = re.findall(r'\b\w+\b', text.lower())
    freq = {}
    for word in words:
        if word in stopwords or len(word) < 3:
            continue
        freq[word] = freq.get(word, 0) + 1
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    keywords = [word for word, count in sorted_words[:num_keywords]]
    return ", ".join(keywords)

def generate_meta_tags(article: str) -> dict:
    """기사를 바탕으로 메타 설명과 메타 키워드를 생성합니다."""
    plain_text = re.sub(r'\s+', ' ', article).strip()
    meta_description = plain_text[:150] + ("..." if len(plain_text) > 150 else "")
    meta_keywords = extract_keywords(article)
    return {"meta_description": meta_description, "meta_keywords": meta_keywords}

def generate_article(topic: str, programming_language: str, article_language: str, max_retries: int = 5) -> tuple:
    """
    OpenAI API를 호출하여, 잘못된 정보 없이 정확한 내용을 담은 Perl 명령어 문서(예: set command 수준의 상세 문서)를 생성합니다.
    문서에는 아래의 섹션들이 포함되어야 합니다.
      - Title: 명령어에 대한 명확한 제목 (검색 키워드 포함)
      - Synopsis: 명령어의 간단한 요약
      - Documentation: 명령어의 목적, 사용법 및 세부 설명
      - Examples: 기본 사용 예제
      - Explanation: 주의사항 및 Gotchas 등 추가 설명
      - One Line Summary: 해당 명령어에 대한 한 줄 요약 (문서 마지막에 출력)
    "See Also" 섹션은 생성하지 않습니다.
    모든 정보는 정확하고 검증된 내용이어야 합니다.
    문서는 {article_language}로 작성됩니다.
    """
    # 캐시 확인
    cached = cache_lookup(topic, programming_language, article_language)
    if cached:
        logging.info(f"캐시 발견: {topic} / {programming_language} / {article_language}")
        return topic, programming_language, article_language, cached["article"], cached["meta_description"], cached["meta_keywords"]

    prompt = f"""
You are an expert documentation writer and SEO specialist in the {programming_language} programming language.
Write a detailed, structured, and SEO-optimized wiki article about "{topic}" as it relates to {programming_language}.
The article must be written in {article_language} and include the following sections:
- Title: A clear title with highly searched keywords.
- Synopsis: A brief summary of the command or feature.
- Documentation: A thorough description covering purpose, usage, and details.
- Examples: Basic usage examples.
- Explanation: Common pitfalls, gotchas, or additional notes.
- One Line Summary: A single sentence summarizing the command.
Ensure all information is accurate and verified. Do not include any misleading or incorrect information.
Do not create a "See Also" section.
Avoid overly verbose explanations.
    """
    attempt = 0
    article = None
    # max_tokens 값을 3000으로 늘려 상세한 답변 생성
    while attempt < max_retries:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": f"You are an expert documentation writer in {programming_language}."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=3000,
                temperature=0.7,
                n=1
            )
            article = response.choices[0].message.content
            break
        except openai.error.RateLimitError:
            wait_time = 2 ** attempt
            logging.warning(f"RateLimit 발생 ({topic} / {programming_language} / {article_language}). {wait_time}초 후 재시도...")
            time.sleep(wait_time)
            attempt += 1
        except Exception as e:
            logging.error(f"기사 생성 에러 ({topic} / {programming_language} / {article_language}): {e}")
            return topic, programming_language, article_language, None, None, None

    if not article:
        logging.error(f"최대 재시도 초과: {topic} / {programming_language} / {article_language}")
        return topic, programming_language, article_language, None, None, None

    meta = generate_meta_tags(article)
    meta_description = meta["meta_description"]
    meta_keywords = meta["meta_keywords"]

    cache_save(topic, programming_language, article_language, article, meta_description, meta_keywords)
    logging.info(f"기사 생성 및 저장 성공: {topic} / {programming_language} / {article_language}")
    return topic, programming_language, article_language, article, meta_description, meta_keywords

def load_seed_file(seed_file: str) -> list:
    """Seed 파일에서 주제 목록을 읽어옵니다."""
    try:
        with open(seed_file, "r", encoding="utf-8") as f:
            topics = json.load(f)
        if isinstance(topics, list):
            return topics
        else:
            logging.error("Seed 파일 형식이 올바르지 않습니다. (리스트 형식 필요)")
            return []
    except Exception as e:
        logging.error(f"Seed 파일 읽기 에러: {e}")
        return []

def main():
    init_db()
    output_dir = "./articles"
    os.makedirs(output_dir, exist_ok=True)

    # 위키로 만들 프로그래밍 언어 이름 (예: Perl, Python, Java 등)
    programming_language = "Perl"  # 원하는 프로그래밍 언어로 수정 가능

    # 생성할 문서의 언어 목록 (총 11개)
    article_languages = [
        "Korean",
        "English",
        "Japanese",
        "Traditional Chinese",
        "Simplified Chinese",
        "Cantonese",
        "Vietnamese",
        "German",
        "Arabic",
        "Spanish",
        "Portuguese"
    ]

    # seed 파일에서 주제 목록 읽기
    topics = load_seed_file(SEED_FILE)
    if not topics:
        logging.error("Seed 파일에 주제 목록이 없습니다. 종료합니다.")
        return

    for topic in topics:
        for article_language in article_languages:
            topic_val, pl, al, article, meta_description, meta_keywords = generate_article(topic, programming_language, article_language)
            if article:
                safe_topic = slugify(topic)
                safe_al = slugify(article_language)
                file_name = f"{safe_topic}_{safe_al}.md"
                file_path = os.path.join(output_dir, file_name)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"<!--\nMeta Description: {meta_description}\nMeta Keywords: {meta_keywords}\n-->\n\n")
                    f.write(article)
                logging.info(f"✅ 기사 생성 완료: {file_path}")
            else:
                logging.error(f"❌ 기사 생성 실패: {topic} / {programming_language} / {article_language}")

if __name__ == "__main__":
    main()

