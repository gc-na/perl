# [리눅스] C Shell (csh) dig 사용법: DNS 쿼리 수행

## Overview
`dig` 명령어는 DNS(Domain Name System) 쿼리를 수행하는 도구입니다. 이 명령어를 사용하면 도메인 이름을 IP 주소로 변환하거나, DNS 레코드 정보를 조회할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```
dig [옵션] [인수]
```

## Common Options
- `@서버`: 특정 DNS 서버를 지정하여 쿼리를 수행합니다.
- `-t 타입`: 조회할 DNS 레코드의 타입을 지정합니다. 예: A, AAAA, MX 등.
- `+short`: 간단한 출력 형식으로 결과를 표시합니다.
- `+trace`: DNS 쿼리의 전체 경로를 추적하여 보여줍니다.

## Common Examples
- 기본 A 레코드 조회:
  ```bash
  dig example.com
  ```

- 특정 DNS 서버에서 A 레코드 조회:
  ```bash
  dig @8.8.8.8 example.com
  ```

- MX 레코드 조회:
  ```bash
  dig -t MX example.com
  ```

- 간단한 출력 형식으로 A 레코드 조회:
  ```bash
  dig +short example.com
  ```

- DNS 쿼리의 전체 경로 추적:
  ```bash
  dig +trace example.com
  ```

## Tips
- DNS 문제를 해결할 때 `+trace` 옵션을 사용하면 유용합니다.
- 특정 DNS 서버를 지정하여 쿼리하면, 해당 서버의 응답을 직접 확인할 수 있습니다.
- `dig` 명령어의 결과를 스크립트에서 활용할 수 있도록 `+short` 옵션을 사용하여 간단한 출력을 얻는 것이 좋습니다.