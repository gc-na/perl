# [리눅스] C Shell (csh) write 사용법: 다른 사용자에게 메시지 전송

## Overview
`write` 명령은 현재 로그인한 사용자에게 메시지를 전송하는 데 사용됩니다. 이 명령을 통해 실시간으로 다른 사용자와 소통할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```
write [사용자] [터미널]
```

## Common Options
- `-n`: 메시지를 보낼 때 사용자에게 알림을 표시하지 않습니다.
- `-h`: 메시지를 보낼 때 상대방의 터미널을 숨깁니다.

## Common Examples
다음은 `write` 명령을 사용하는 몇 가지 예입니다.

1. 특정 사용자에게 메시지 보내기:
   ```csh
   write user1
   Hello, how are you?
   ```

2. 특정 터미널에 메시지 보내기:
   ```csh
   write user2 pts/1
   Please check your email.
   ```

3. 알림 없이 메시지 보내기:
   ```csh
   write -n user3
   I'm busy right now.
   ```

## Tips
- `write` 명령을 사용하기 전에 상대방이 메시지를 받을 수 있는 상태인지 확인하세요.
- 상대방이 `mesg n` 명령을 사용하여 메시지 수신을 차단한 경우, 메시지를 보낼 수 없습니다.
- 간단하고 명확한 메시지를 작성하여 혼란을 피하세요.