# [리눅스] C Shell (csh) md5sum 사용법: 파일의 MD5 해시 계산

## Overview
md5sum 명령어는 파일의 MD5 해시 값을 계산하여 파일의 무결성을 확인하는 데 사용됩니다. 이 해시 값은 파일이 변경되지 않았음을 보장하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```csh
md5sum [옵션] [인수]
```

## Common Options
- `-b`: 바이너리 파일을 처리할 때 사용합니다.
- `-c`: 체크섬 파일을 읽고, 해당 체크섬을 검증합니다.
- `-t`: 텍스트 파일을 처리할 때 사용합니다.
- `--help`: 사용법 정보를 출력합니다.

## Common Examples
- 파일의 MD5 해시 계산:
```csh
md5sum example.txt
```

- 여러 파일의 MD5 해시 계산:
```csh
md5sum file1.txt file2.txt
```

- 체크섬 파일을 사용하여 파일 검증:
```csh
md5sum -c checksum.md5
```

- 바이너리 파일의 MD5 해시 계산:
```csh
md5sum -b binaryfile.bin
```

## Tips
- 해시 값을 비교하여 파일이 변경되었는지 확인할 수 있습니다.
- 체크섬 파일을 생성하여 나중에 파일 검증에 사용할 수 있습니다.
- 파일이 클 경우, 해시 계산이 시간이 걸릴 수 있으므로 주의하세요.