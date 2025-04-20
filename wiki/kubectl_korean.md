# [리눅스] C Shell (csh) kubectl 사용법: Kubernetes 클러스터 관리

## Overview
kubectl은 Kubernetes 클러스터를 관리하고 조작하기 위한 명령줄 도구입니다. 이 도구를 사용하면 클러스터의 상태를 확인하고, 리소스를 생성, 수정 및 삭제할 수 있습니다.

## Usage
kubectl의 기본 구문은 다음과 같습니다:

```bash
kubectl [options] [arguments]
```

## Common Options
- `get`: 클러스터에서 리소스를 조회합니다.
- `apply`: 리소스를 생성하거나 업데이트합니다.
- `delete`: 클러스터에서 리소스를 삭제합니다.
- `describe`: 특정 리소스에 대한 자세한 정보를 제공합니다.
- `logs`: 파드의 로그를 확인합니다.

## Common Examples
- 클러스터의 모든 파드 목록 조회:
  ```bash
  kubectl get pods
  ```

- 특정 네임스페이스의 서비스 목록 조회:
  ```bash
  kubectl get services -n my-namespace
  ```

- YAML 파일을 사용하여 리소스 생성 또는 업데이트:
  ```bash
  kubectl apply -f deployment.yaml
  ```

- 특정 파드의 로그 확인:
  ```bash
  kubectl logs my-pod
  ```

- 특정 리소스 삭제:
  ```bash
  kubectl delete pod my-pod
  ```

## Tips
- 명령어를 입력하기 전에 `kubectl`의 `--help` 옵션을 사용하여 추가적인 도움말을 확인하세요.
- 자주 사용하는 명령어는 alias를 설정하여 단축할 수 있습니다.
- YAML 파일을 사용하여 리소스를 정의하면 일관된 배포가 가능합니다.