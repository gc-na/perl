# [리눅스] C Shell (csh) docker 사용법: 컨테이너 관리

## Overview
docker 명령어는 컨테이너화된 애플리케이션을 관리하는 데 사용됩니다. 이를 통해 개발자는 애플리케이션을 쉽게 배포하고 실행할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
docker [options] [arguments]
```

## Common Options
- `run`: 새로운 컨테이너를 생성하고 실행합니다.
- `ps`: 현재 실행 중인 컨테이너 목록을 표시합니다.
- `stop`: 실행 중인 컨테이너를 중지합니다.
- `rm`: 중지된 컨테이너를 삭제합니다.
- `images`: 로컬에 저장된 이미지 목록을 표시합니다.

## Common Examples
- 새로운 컨테이너 실행:
  ```bash
  docker run -d nginx
  ```
- 실행 중인 컨테이너 목록 보기:
  ```bash
  docker ps
  ```
- 특정 컨테이너 중지:
  ```bash
  docker stop <컨테이너_ID>
  ```
- 중지된 컨테이너 삭제:
  ```bash
  docker rm <컨테이너_ID>
  ```
- 로컬 이미지 목록 보기:
  ```bash
  docker images
  ```

## Tips
- 컨테이너를 실행할 때 `-d` 옵션을 사용하면 백그라운드에서 실행됩니다.
- `docker ps -a` 명령어를 사용하면 중지된 컨테이너도 포함한 모든 컨테이너 목록을 확인할 수 있습니다.
- 이미지와 컨테이너의 이름을 명확하게 지정하여 관리하기 쉽게 하세요.