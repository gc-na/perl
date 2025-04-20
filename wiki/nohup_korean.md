# [리눅스] C Shell (csh) nohup 사용법: 프로세스를 백그라운드에서 실행하기

## Overview
`nohup` 명령어는 사용자가 로그아웃하더라도 프로세스가 계속 실행되도록 하는 데 사용됩니다. 주로 장시간 실행되는 작업을 수행할 때 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
nohup [options] [arguments]
```

## Common Options
- `&` : 명령어를 백그라운드에서 실행합니다.
- `-h` : 도움말을 표시합니다.
- `-v` : 버전 정보를 표시합니다.

## Common Examples
1. **단순한 nohup 사용 예시**
   ```bash
   nohup myscript.sh &
   ```
   이 명령은 `myscript.sh` 스크립트를 백그라운드에서 실행합니다.

2. **출력을 파일로 리디렉션**
   ```bash
   nohup myscript.sh > output.log &
   ```
   이 명령은 스크립트의 출력을 `output.log` 파일로 저장하며 백그라운드에서 실행합니다.

3. **명령어와 인수 사용**
   ```bash
   nohup python myscript.py arg1 arg2 &
   ```
   이 명령은 Python 스크립트를 인수와 함께 백그라운드에서 실행합니다.

## Tips
- `nohup`을 사용할 때는 항상 출력을 파일로 리디렉션하는 것이 좋습니다. 이렇게 하면 나중에 로그를 확인할 수 있습니다.
- 백그라운드에서 실행 중인 프로세스를 확인하려면 `jobs` 명령어를 사용할 수 있습니다.
- 프로세스를 중지하려면 `kill` 명령어를 사용하여 프로세스 ID를 지정해야 합니다.