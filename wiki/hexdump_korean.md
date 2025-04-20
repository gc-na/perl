# [리눅스] C Shell (csh) hexdump 사용법: 이진 파일의 헥사 덤프 출력

## Overview
hexdump 명령어는 파일의 내용을 헥사(16진수) 형식으로 출력하는 데 사용됩니다. 이 명령어는 이진 파일의 내용을 시각적으로 분석하거나 디버깅할 때 유용합니다.

## Usage
hexdump의 기본 구문은 다음과 같습니다.

```csh
hexdump [options] [arguments]
```

## Common Options
- `-C`: 헥사와 ASCII 형식을 함께 출력합니다.
- `-n <number>`: 출력할 바이트 수를 지정합니다.
- `-e <format>`: 출력 형식을 사용자 정의합니다.

## Common Examples
다음은 hexdump 명령어의 몇 가지 일반적인 사용 예입니다.

### 예제 1: 기본 헥사 덤프
파일의 내용을 기본 헥사 형식으로 출력합니다.

```csh
hexdump myfile.bin
```

### 예제 2: 헥사 및 ASCII 출력
헥사와 ASCII 형식을 함께 출력합니다.

```csh
hexdump -C myfile.bin
```

### 예제 3: 특정 바이트 수 출력
파일의 처음 16바이트만 출력합니다.

```csh
hexdump -n 16 myfile.bin
```

### 예제 4: 사용자 정의 출력 형식
특정 형식으로 출력합니다.

```csh
hexdump -e '16/1 "%02x " "\n"' myfile.bin
```

## Tips
- 파일의 크기가 큰 경우, `-n` 옵션을 사용하여 출력할 바이트 수를 제한하면 유용합니다.
- `-C` 옵션을 사용하면 헥사와 ASCII를 동시에 볼 수 있어 분석이 더 쉬워집니다.
- 출력 결과를 파일로 저장하려면 리다이렉션을 사용하세요. 예: `hexdump myfile.bin > output.txt`.