# [리눅스] C Shell (csh) awk 사용법: 텍스트 처리 및 데이터 분석

## Overview
`awk`는 텍스트 파일에서 데이터 처리 및 분석을 위한 강력한 도구입니다. 주로 패턴 매칭과 데이터 조작을 통해 특정 필드를 추출하거나 변환하는 데 사용됩니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
awk [options] [arguments]
```

## Common Options
- `-F`: 필드 구분자를 지정합니다. 기본값은 공백입니다.
- `-v`: 변수를 설정할 때 사용합니다.
- `-f`: 스크립트 파일을 지정하여 여러 명령을 실행할 수 있습니다.

## Common Examples
- 특정 필드 출력하기:
```bash
awk '{print $1}' filename.txt
```
위의 명령은 `filename.txt` 파일의 첫 번째 필드를 출력합니다.

- 필드 구분자 변경하기:
```bash
awk -F, '{print $1}' filename.csv
```
이 명령은 CSV 파일에서 첫 번째 필드를 출력합니다.

- 조건에 따라 필터링하기:
```bash
awk '$3 > 50 {print $1, $3}' filename.txt
```
이 명령은 세 번째 필드의 값이 50보다 큰 경우 첫 번째와 세 번째 필드를 출력합니다.

- 변수 사용하기:
```bash
awk -v threshold=100 '$2 > threshold {print $1}' filename.txt
```
여기서는 `threshold` 변수를 사용하여 두 번째 필드가 100보다 큰 경우 첫 번째 필드를 출력합니다.

## Tips
- `awk`는 대소문자를 구분하므로, 필요에 따라 `tolower()` 또는 `toupper()` 함수를 사용하여 변환할 수 있습니다.
- 복잡한 스크립트를 작성할 때는 `-f` 옵션을 사용하여 별도의 파일에 명령을 작성하는 것이 좋습니다.
- 정규 표현식을 활용하여 더욱 정교한 패턴 매칭을 수행할 수 있습니다.