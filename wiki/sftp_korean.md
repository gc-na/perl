# [한국어] C Shell (csh) sftp 사용법: 파일 전송을 위한 안전한 프로토콜

## Overview
`sftp` 명령은 SSH 프로토콜을 통해 안전하게 파일을 전송하는 데 사용됩니다. 이 명령은 파일을 업로드하거나 다운로드할 수 있는 기능을 제공하며, 네트워크를 통해 파일 전송 시 보안을 유지합니다.

## Usage
기본 구문은 다음과 같습니다:
```
sftp [options] [user@]host
```

## Common Options
- `-b <batchfile>`: 배치 모드에서 사용할 명령을 포함하는 파일을 지정합니다.
- `-C`: 전송 중에 데이터를 압축합니다.
- `-P <port>`: 연결할 포트를 지정합니다.
- `-o <option>`: 특정 SSH 옵션을 설정합니다.

## Common Examples
- 원격 서버에 연결하기:
  ```bash
  sftp user@hostname
  ```

- 파일 다운로드:
  ```bash
  sftp user@hostname:/remote/path/to/file /local/path/to/file
  ```

- 파일 업로드:
  ```bash
  sftp /local/path/to/file user@hostname:/remote/path/to/file
  ```

- 디렉토리의 모든 파일 다운로드:
  ```bash
  sftp user@hostname
  get -r /remote/path/to/directory
  ```

## Tips
- 항상 안전한 비밀번호를 사용하여 보안을 강화하세요.
- 대량의 파일 전송 시 `-b` 옵션을 사용하여 배치 파일을 활용하면 효율적입니다.
- 전송 중 문제가 발생하면 `-C` 옵션을 사용하여 데이터를 압축하여 전송 속도를 높일 수 있습니다.