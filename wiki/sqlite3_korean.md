# [리눅스] C Shell (csh) sqlite3 사용법: SQLite 데이터베이스 관리

## 개요
sqlite3 명령어는 SQLite 데이터베이스를 생성하고 관리하는 데 사용됩니다. 이 명령어를 통해 데이터베이스에 쿼리를 실행하고, 테이블을 생성하며, 데이터를 삽입하거나 수정할 수 있습니다.

## 사용법
기본 구문은 다음과 같습니다:
```csh
sqlite3 [옵션] [인수]
```

## 일반 옵션
- `-help`: 사용 가능한 모든 옵션과 도움말을 표시합니다.
- `-version`: 현재 설치된 SQLite의 버전을 표시합니다.
- `-init <파일>`: 지정된 SQL 파일을 실행하여 데이터베이스를 초기화합니다.

## 일반 예제
- 데이터베이스 생성 및 열기:
```csh
sqlite3 mydatabase.db
```

- 테이블 생성:
```csh
sqlite3 mydatabase.db "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);"
```

- 데이터 삽입:
```csh
sqlite3 mydatabase.db "INSERT INTO users (name) VALUES ('Alice');"
```

- 데이터 조회:
```csh
sqlite3 mydatabase.db "SELECT * FROM users;"
```

- 데이터베이스 백업:
```csh
sqlite3 mydatabase.db ".backup mydatabase_backup.db"
```

## 팁
- SQL 쿼리를 실행할 때는 항상 세미콜론(;)으로 쿼리를 종료해야 합니다.
- `.exit` 명령어를 사용하여 SQLite 셸에서 안전하게 종료할 수 있습니다.
- 데이터베이스 파일을 정기적으로 백업하여 데이터 손실을 방지하세요.