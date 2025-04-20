# [리눅스] C Shell (csh) bzip2 사용법: 파일 압축 및 해제

## Overview
bzip2는 파일을 압축하고 해제하는 데 사용되는 명령어입니다. 이 명령어는 주로 대용량 파일의 크기를 줄이는 데 유용하며, 높은 압축률을 제공합니다.

## Usage
bzip2의 기본 구문은 다음과 같습니다.

```bash
bzip2 [options] [arguments]
```

## Common Options
- `-d`, `--decompress`: 압축을 해제합니다.
- `-k`, `--keep`: 원본 파일을 유지하면서 압축합니다.
- `-f`, `--force`: 기존 파일을 덮어씁니다.
- `-v`, `--verbose`: 압축 진행 상황을 자세히 표시합니다.

## Common Examples
압축 및 해제의 몇 가지 일반적인 예는 다음과 같습니다.

### 파일 압축
```bash
bzip2 example.txt
```
이 명령어는 `example.txt` 파일을 압축하여 `example.txt.bz2` 파일을 생성합니다.

### 파일 압축 해제
```bash
bzip2 -d example.txt.bz2
```
이 명령어는 `example.txt.bz2` 파일의 압축을 해제하여 원본 파일인 `example.txt`를 복원합니다.

### 원본 파일 유지하면서 압축
```bash
bzip2 -k example.txt
```
이 명령어는 `example.txt` 파일을 압축하되, 원본 파일을 그대로 유지합니다.

### 압축 진행 상황 보기
```bash
bzip2 -v example.txt
```
이 명령어는 압축하는 동안 진행 상황을 자세히 표시합니다.

## Tips
- 대용량 파일을 압축할 때 bzip2를 사용하면 저장 공간을 절약할 수 있습니다.
- 압축 해제 후 원본 파일이 필요 없는 경우 `-k` 옵션을 사용하지 않도록 주의하세요.
- 여러 파일을 동시에 압축하려면 와일드카드(`*`)를 사용할 수 있습니다. 예: `bzip2 *.txt`