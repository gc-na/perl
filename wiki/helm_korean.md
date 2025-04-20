# [리눅스] C Shell (csh) helm 사용법: 패키지 관리 및 배포

## Overview
helm 명령은 Kubernetes 애플리케이션을 관리하는 데 사용되는 패키지 관리자입니다. 이를 통해 사용자는 애플리케이션을 쉽게 설치, 업그레이드 및 삭제할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
helm [options] [arguments]
```

## Common Options
- `install`: 새로운 차트를 설치합니다.
- `upgrade`: 기존 차트를 업그레이드합니다.
- `uninstall`: 설치된 차트를 삭제합니다.
- `list`: 현재 설치된 차트 목록을 표시합니다.
- `repo`: Helm 차트 저장소를 관리합니다.

## Common Examples
- 새로운 차트 설치:
  ```bash
  helm install my-release my-chart
  ```
  
- 차트 업그레이드:
  ```bash
  helm upgrade my-release my-chart
  ```

- 설치된 차트 삭제:
  ```bash
  helm uninstall my-release
  ```

- 설치된 차트 목록 보기:
  ```bash
  helm list
  ```

- 차트 저장소 추가:
  ```bash
  helm repo add my-repo https://example.com/charts
  ```

## Tips
- Helm 차트를 사용하기 전에 항상 최신 버전으로 업데이트하세요.
- 차트의 값을 조정하려면 `--set` 옵션을 사용하여 사용자 정의 값을 지정할 수 있습니다.
- Helm의 문서를 참조하여 다양한 플러그인과 기능을 활용해 보세요.