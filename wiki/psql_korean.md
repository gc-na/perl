# [리눅스] C Shell (csh) psql 사용법: PostgreSQL 데이터베이스에 연결하고 쿼리를 실행하는 명령

## Overview
`psql` 명령은 PostgreSQL 데이터베이스에 연결하고 SQL 쿼리를 실행할 수 있는 커맨드라인 도구입니다. 이 도구를 사용하면 데이터베이스와 상호작용하고, 데이터를 조회하거나 수정하는 등의 작업을 수행할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
psql [options] [arguments]
```

## Common Options
- `-h`: 데이터베이스 서버의 호스트 이름을 지정합니다.
- `-U`: 데이터베이스 사용자 이름을 지정합니다.
- `-d`: 연결할 데이터베이스의 이름을 지정합니다.
- `-p`: 데이터베이스 서버의 포트 번호를 지정합니다.
- `-W`: 비밀번호 입력을 요구합니다.

## Common Examples
1. 데이터베이스에 연결하기:
   ```csh
   psql -h localhost -U username -d dbname
   ```

2. SQL 파일 실행하기:
   ```csh
   psql -U username -d dbname -f script.sql
   ```

3. 데이터베이스 목록 보기:
   ```csh
   psql -U username -d dbname -c "\l"
   ```

4. 특정 테이블의 데이터 조회하기:
   ```csh
   psql -U username -d dbname -c "SELECT * FROM tablename;"
   ```

## Tips
- `\?` 명령을 사용하여 psql 내에서 사용할 수 있는 모든 명령어를 확인할 수 있습니다.
- 쿼리를 실행하기 전에 항상 데이터베이스와 연결이 잘 되었는지 확인하세요.
- 자주 사용하는 쿼리는 SQL 파일로 저장하고, 필요할 때마다 실행하는 것이 효율적입니다.