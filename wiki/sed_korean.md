# [리눅스] C Shell (csh) sed 사용법: 텍스트 변환 및 편집

## Overview
`sed`는 스트림 편집기(Stream Editor)로, 텍스트 데이터를 처리하고 변환하는 데 사용됩니다. 주로 파일의 내용을 수정하거나 특정 패턴을 찾아 대체하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
sed [options] [arguments]
```

## Common Options
- `-e`: 여러 개의 편집 명령을 지정합니다.
- `-i`: 파일을 직접 수정합니다.
- `-n`: 결과를 출력하지 않고, 명시적으로 지정한 경우에만 출력합니다.
- `s/pattern/replacement/`: 지정한 패턴을 대체합니다.

## Common Examples
1. **문자열 대체하기**
   ```bash
   sed 's/old/new/' filename.txt
   ```
   `filename.txt`에서 "old"를 "new"로 대체합니다.

2. **파일 직접 수정하기**
   ```bash
   sed -i 's/old/new/g' filename.txt
   ```
   `filename.txt`에서 "old"를 "new"로 모든 곳에서 대체하고 파일을 직접 수정합니다.

3. **특정 줄만 출력하기**
   ```bash
   sed -n '2p' filename.txt
   ```
   `filename.txt`의 두 번째 줄만 출력합니다.

4. **여러 개의 대체 명령 사용하기**
   ```bash
   sed -e 's/old1/new1/' -e 's/old2/new2/' filename.txt
   ```
   `filename.txt`에서 "old1"을 "new1"로, "old2"를 "new2"로 대체합니다.

## Tips
- `-i` 옵션을 사용할 때는 원본 파일의 백업을 만드는 것이 좋습니다. 예를 들어, `-i.bak`를 사용하여 `.bak` 확장자를 가진 백업 파일을 생성할 수 있습니다.
- 복잡한 패턴을 다룰 때는 정규 표현식을 활용하면 더욱 강력한 검색 및 대체가 가능합니다.
- `sed`는 파이프와 함께 사용하여 다른 명령의 출력 결과를 처리하는 데 유용합니다.