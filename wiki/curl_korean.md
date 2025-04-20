# [리눅스] C Shell (csh) curl 사용법: 웹에서 데이터 전송

## Overview
curl 명령어는 URL을 통해 데이터를 전송하거나 받아오는 데 사용됩니다. 다양한 프로토콜을 지원하며, 주로 웹 API와 상호작용할 때 유용합니다.

## Usage
curl의 기본 구문은 다음과 같습니다:

```csh
curl [options] [arguments]
```

## Common Options
- `-X`: HTTP 메서드 지정 (예: GET, POST 등)
- `-d`: POST 요청 시 전송할 데이터 지정
- `-H`: 요청 헤더 추가
- `-o`: 응답을 파일로 저장
- `-I`: HTTP 헤더만 요청

## Common Examples
1. **웹 페이지 가져오기**
   ```csh
   curl http://example.com
   ```

2. **POST 요청 보내기**
   ```csh
   curl -X POST -d "name=John&age=30" http://example.com/api
   ```

3. **응답을 파일로 저장하기**
   ```csh
   curl -o output.html http://example.com
   ```

4. **특정 헤더 추가하기**
   ```csh
   curl -H "Authorization: Bearer token" http://example.com/api
   ```

5. **HTTP 헤더만 요청하기**
   ```csh
   curl -I http://example.com
   ```

## Tips
- curl을 사용할 때는 항상 URL을 정확히 입력하세요.
- API와 상호작용할 때는 필요한 인증 정보를 잊지 마세요.
- `-v` 옵션을 사용하면 요청과 응답의 상세 정보를 확인할 수 있어 디버깅에 유용합니다.