# [리눅스] C Shell (csh) fmt 사용법: 텍스트 포맷팅

## Overview
`fmt` 명령어는 텍스트 파일의 줄 길이를 조정하여 가독성을 높이는 데 사용됩니다. 주로 긴 문장을 적절한 길이로 나누어 출력하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```csh
fmt [options] [arguments]
```

## Common Options
- `-w <width>`: 출력할 최대 줄 길이를 설정합니다. 기본값은 75자입니다.
- `-s`: 연속된 공백을 하나의 공백으로 줄입니다.
- `-u`: 비정형 텍스트를 정형화하여 출력합니다.

## Common Examples
- 기본 사용법:
```csh
fmt example.txt
```
이 명령어는 `example.txt` 파일의 내용을 포맷하여 출력합니다.

- 최대 줄 길이를 50자로 설정:
```csh
fmt -w 50 example.txt
```
이 명령어는 `example.txt` 파일을 최대 50자 길이로 포맷합니다.

- 연속된 공백을 하나로 줄이기:
```csh
fmt -s example.txt
```
이 명령어는 `example.txt` 파일에서 연속된 공백을 하나로 줄여서 출력합니다.

## Tips
- 포맷된 내용을 새로운 파일로 저장하려면 리다이렉션을 사용할 수 있습니다:
```csh
fmt example.txt > formatted_example.txt
```
- 여러 파일을 한 번에 포맷하려면 파일 이름을 공백으로 구분하여 나열할 수 있습니다:
```csh
fmt file1.txt file2.txt
```
- 포맷팅 후 결과를 확인하기 위해 `cat` 명령어와 함께 사용할 수 있습니다:
```csh
fmt example.txt | cat
```