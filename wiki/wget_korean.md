# [리눅스] C Shell (csh) wget 사용법: 파일 다운로드

## Overview
`wget` 명령어는 웹에서 파일을 다운로드하는 데 사용됩니다. HTTP, HTTPS, FTP와 같은 다양한 프로토콜을 지원하며, 비대화형으로 작동하여 백그라운드에서 파일을 다운로드할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
wget [options] [arguments]
```

## Common Options
- `-O [파일명]`: 다운로드한 파일의 이름을 지정합니다.
- `-r`: 재귀적으로 다운로드합니다. 하위 디렉토리의 파일도 포함됩니다.
- `-c`: 중단된 다운로드를 이어서 진행합니다.
- `--limit-rate=[속도]`: 다운로드 속도를 제한합니다.
- `-q`: 조용한 모드로, 진행 상황을 출력하지 않습니다.

## Common Examples
- 단일 파일 다운로드:
```bash
wget http://example.com/file.zip
```

- 파일 이름 지정하여 다운로드:
```bash
wget -O myfile.zip http://example.com/file.zip
```

- 재귀적으로 웹사이트 다운로드:
```bash
wget -r http://example.com/
```

- 중단된 다운로드 이어서 진행:
```bash
wget -c http://example.com/largefile.zip
```

- 다운로드 속도 제한:
```bash
wget --limit-rate=200k http://example.com/largefile.zip
```

## Tips
- 대용량 파일을 다운로드할 때는 `-c` 옵션을 사용하여 중단된 다운로드를 쉽게 이어서 진행할 수 있습니다.
- `-q` 옵션을 사용하면 스크립트에서 wget을 사용할 때 출력이 깔끔해집니다.
- 여러 파일을 동시에 다운로드하려면 `wget`을 여러 번 실행하거나 `xargs`와 함께 사용할 수 있습니다.