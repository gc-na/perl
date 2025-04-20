# [리눅스] C Shell (csh) rev: 문자열 반전

## Overview
`rev` 명령어는 입력된 각 줄의 문자를 반전시켜 출력하는 기능을 제공합니다. 주로 텍스트 파일의 내용을 쉽게 확인하거나 특정 형식으로 변환할 때 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
rev [options] [arguments]
```

## Common Options
- `-o, --output=FILE`: 반전된 출력을 지정된 파일에 저장합니다.
- `-h, --help`: 사용법을 보여줍니다.
- `-V, --version`: 버전 정보를 표시합니다.

## Common Examples
1. **파일의 내용 반전하기**
   ```csh
   rev myfile.txt
   ```

2. **표준 입력에서 반전하기**
   ```csh
   echo "Hello World" | rev
   ```

3. **출력을 파일에 저장하기**
   ```csh
   rev myfile.txt -o reversed.txt
   ```

4. **여러 파일 반전하기**
   ```csh
   rev file1.txt file2.txt
   ```

## Tips
- `rev` 명령어는 파이프와 함께 사용하여 다른 명령어의 출력을 쉽게 변환할 수 있습니다.
- 파일의 내용을 반전할 때, 원본 파일을 덮어쓰지 않도록 주의하세요. `-o` 옵션을 사용하여 다른 파일에 저장하는 것이 좋습니다.