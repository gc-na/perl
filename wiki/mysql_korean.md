# [리눅스] C Shell (csh) mysql 사용법: 데이터베이스 관리 및 쿼리 실행

## Overview
mysql 명령어는 MySQL 데이터베이스에 접속하여 데이터베이스를 관리하고 SQL 쿼리를 실행할 수 있는 클라이언트 프로그램입니다. 사용자는 데이터베이스에 연결하여 데이터를 조회, 삽입, 수정 및 삭제할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다.
```
mysql [options] [arguments]
```

## Common Options
- `-u [username]`: MySQL 사용자 이름을 지정합니다.
- `-p`: 비밀번호 입력을 요청합니다.
- `-h [hostname]`: 연결할 MySQL 서버의 호스트 이름을 지정합니다.
- `-D [database]`: 접속할 데이터베이스를 지정합니다.
- `--execute [query]`: 지정된 SQL 쿼리를 실행합니다.

## Common Examples
- MySQL 서버에 접속하기:
  ```csh
  mysql -u root -p
  ```

- 특정 데이터베이스에 접속하기:
  ```csh
  mysql -u user -p -D mydatabase
  ```

- SQL 쿼리 실행하기:
  ```csh
  mysql -u user -p -e "SELECT * FROM mytable;"
  ```

- 데이터베이스 백업하기:
  ```csh
  mysqldump -u user -p mydatabase > backup.sql
  ```

## Tips
- 비밀번호를 명령줄에 직접 입력하지 않는 것이 좋습니다. `-p` 옵션만 사용하여 비밀번호 입력을 요청받는 것이 안전합니다.
- 데이터베이스에 대한 정기적인 백업을 수행하여 데이터 손실을 방지하세요.
- SQL 쿼리를 실행하기 전에 항상 쿼리를 검토하여 의도한 대로 작동하는지 확인하세요.