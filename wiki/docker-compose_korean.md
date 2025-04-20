# [리눅스] C Shell (csh) docker-compose 사용법: 컨테이너 오케스트레이션 관리

## Overview
docker-compose는 여러 개의 Docker 컨테이너를 정의하고 실행할 수 있는 도구입니다. YAML 파일을 사용하여 애플리케이션의 서비스, 네트워크 및 볼륨을 설정하고, 단일 명령으로 모든 서비스를 시작하거나 중지할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
docker-compose [options] [arguments]
```

## Common Options
- `up`: 정의된 서비스들을 시작합니다.
- `down`: 실행 중인 서비스들을 중지하고 네트워크를 제거합니다.
- `build`: 서비스의 이미지를 빌드합니다.
- `logs`: 서비스의 로그를 출력합니다.
- `ps`: 현재 실행 중인 서비스의 상태를 보여줍니다.

## Common Examples
- 모든 서비스를 시작할 때:
  ```bash
  docker-compose up
  ```

- 백그라운드에서 서비스를 시작할 때:
  ```bash
  docker-compose up -d
  ```

- 실행 중인 서비스를 중지할 때:
  ```bash
  docker-compose down
  ```

- 서비스의 로그를 확인할 때:
  ```bash
  docker-compose logs
  ```

- 서비스의 상태를 확인할 때:
  ```bash
  docker-compose ps
  ```

## Tips
- YAML 파일을 잘 구성하여 서비스 간의 의존성을 명확히 하세요.
- `docker-compose up -d`를 사용하여 백그라운드에서 실행하면 터미널을 계속 사용할 수 있습니다.
- 주기적으로 `docker-compose down`을 사용하여 불필요한 리소스를 정리하세요.