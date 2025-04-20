# [리눅스] C Shell (csh) scp 사용법: 원격 서버 간 파일 전송

## Overview
`scp` 명령은 Secure Copy Protocol의 약자로, 네트워크를 통해 파일을 안전하게 복사하는 데 사용됩니다. 이 명령은 SSH(Secure Shell)를 기반으로 하여 파일 전송을 암호화합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
scp [options] [source] [destination]
```

## Common Options
- `-r`: 디렉토리를 재귀적으로 복사합니다.
- `-P`: 원격 호스트의 포트를 지정합니다. (대문자 P)
- `-p`: 파일의 수정 시간, 접근 시간 및 모드를 유지합니다.
- `-q`: 진행 상황을 표시하지 않습니다.
- `-C`: 전송 중 데이터 압축을 활성화합니다.

## Common Examples
1. **로컬에서 원격 서버로 파일 복사**
   ```bash
   scp localfile.txt user@remotehost:/path/to/destination/
   ```

2. **원격 서버에서 로컬로 파일 복사**
   ```bash
   scp user@remotehost:/path/to/remotefile.txt /local/destination/
   ```

3. **디렉토리 전체를 원격 서버로 복사**
   ```bash
   scp -r /local/directory user@remotehost:/path/to/destination/
   ```

4. **특정 포트를 사용하여 원격 서버로 파일 복사**
   ```bash
   scp -P 2222 localfile.txt user@remotehost:/path/to/destination/
   ```

## Tips
- 파일 전송 속도를 높이기 위해 `-C` 옵션을 사용하여 압축을 활성화하세요.
- 원격 서버에 연결할 때 SSH 키를 사용하면 비밀번호 입력 없이 자동으로 로그인할 수 있습니다.
- 대량의 파일을 전송할 때는 `-r` 옵션을 사용하여 디렉토리를 한 번에 복사하는 것이 효율적입니다.