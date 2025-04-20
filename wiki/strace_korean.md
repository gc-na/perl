# [리눅스] C Shell (csh) strace 사용법: 시스템 호출 추적

## Overview
`strace` 명령어는 프로그램이 수행하는 시스템 호출과 신호를 추적하는 도구입니다. 이를 통해 개발자와 시스템 관리자는 프로그램의 동작을 분석하고 문제를 진단할 수 있습니다.

## Usage
기본적인 `strace` 명령어 구문은 다음과 같습니다.

```csh
strace [options] [arguments]
```

## Common Options
- `-c`: 시스템 호출 통계 요약을 출력합니다.
- `-e`: 특정 시스템 호출만을 추적합니다. 예를 들어, `-e trace=open`은 `open` 호출만 추적합니다.
- `-p`: 이미 실행 중인 프로세스에 `strace`를 붙입니다. 프로세스 ID를 인자로 사용합니다.
- `-o <file>`: 출력 결과를 지정한 파일로 저장합니다.

## Common Examples
1. 기본적인 프로그램 실행 추적:
   ```csh
   strace ls
   ```

2. 특정 시스템 호출만 추적하기:
   ```csh
   strace -e trace=open ls
   ```

3. 실행 중인 프로세스에 `strace` 붙이기:
   ```csh
   strace -p 1234
   ```

4. 출력 결과를 파일로 저장하기:
   ```csh
   strace -o output.txt ls
   ```

5. 시스템 호출 통계 요약 출력하기:
   ```csh
   strace -c ls
   ```

## Tips
- `strace`를 사용할 때는 필요한 정보만 추적하는 것이 좋습니다. 너무 많은 정보를 추적하면 결과가 복잡해질 수 있습니다.
- 프로세스 ID를 확인하려면 `ps` 명령어를 사용할 수 있습니다.
- `strace`의 출력은 디버깅에 유용하지만, 성능에 영향을 줄 수 있으므로 프로덕션 환경에서는 주의해서 사용해야 합니다.