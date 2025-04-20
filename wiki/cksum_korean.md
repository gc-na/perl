# [리눅스] C Shell (csh) cksum 사용법: 파일의 체크섬 계산

## Overview
`cksum` 명령어는 파일의 체크섬과 바이트 수를 계산하여 출력하는 데 사용됩니다. 이 명령어는 파일의 무결성을 확인하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
cksum [options] [arguments]
```

## Common Options
- `-a, --algorithm=ALGO`: 사용할 체크섬 알고리즘을 지정합니다.
- `-h, --help`: 도움말 메시지를 출력합니다.
- `-V, --version`: 버전 정보를 출력합니다.

## Common Examples
- 파일의 체크섬 계산:
  ```csh
  cksum filename.txt
  ```

- 여러 파일의 체크섬 계산:
  ```csh
  cksum file1.txt file2.txt file3.txt
  ```

- 체크섬 알고리즘 지정:
  ```csh
  cksum -a md5 filename.txt
  ```

## Tips
- 체크섬을 사용하여 파일이 변경되지 않았는지 확인할 수 있습니다.
- 여러 파일을 한 번에 체크섬을 계산할 수 있어 편리합니다.
- 결과를 파일에 저장하려면 리다이렉션을 사용할 수 있습니다:
  ```csh
  cksum filename.txt > checksum.txt
  ```