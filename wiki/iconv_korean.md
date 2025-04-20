# [리눅스] C Shell (csh) iconv 사용법: 문자 인코딩 변환

## Overview
iconv 명령어는 파일의 문자 인코딩을 변환하는 데 사용됩니다. 다양한 문자 인코딩 간에 변환할 수 있어, 데이터의 호환성을 높이고, 다양한 언어를 지원하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:

```csh
iconv [options] [arguments]
```

## Common Options
- `-f, --from-code=CODE`: 변환할 원본 문자 인코딩을 지정합니다.
- `-t, --to-code=CODE`: 변환할 목표 문자 인코딩을 지정합니다.
- `-o, --output=FILE`: 변환된 내용을 저장할 출력 파일을 지정합니다.
- `-c`: 변환할 수 없는 문자를 무시합니다.

## Common Examples
1. UTF-8에서 ISO-8859-1로 변환하기:
   ```csh
   iconv -f UTF-8 -t ISO-8859-1 input.txt -o output.txt
   ```

2. EUC-KR에서 UTF-8로 변환하기:
   ```csh
   iconv -f EUC-KR -t UTF-8 input.txt -o output.txt
   ```

3. 변환할 수 없는 문자를 무시하고 변환하기:
   ```csh
   iconv -f UTF-8 -t ASCII//IGNORE input.txt -o output.txt
   ```

## Tips
- 변환할 파일의 인코딩을 정확히 알고 있어야 합니다. 잘못된 인코딩을 지정하면 변환이 실패할 수 있습니다.
- 대량의 파일을 변환할 때는 스크립트를 작성하여 자동화하는 것이 효율적입니다.
- 변환 후 결과 파일을 항상 확인하여 데이터 손실이 없는지 검토하는 것이 좋습니다.