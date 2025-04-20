# [리눅스] C Shell (csh) rsync 사용법: 파일 및 디렉터리 동기화

## 개요
rsync 명령어는 파일 및 디렉터리를 효율적으로 동기화하고 전송하는 데 사용됩니다. 로컬 및 원격 시스템 간에 데이터를 복사할 수 있으며, 변경된 부분만 전송하여 대역폭을 절약합니다.

## 사용법
기본 구문은 다음과 같습니다:

```
rsync [옵션] [인수]
```

## 일반 옵션
- `-a`: 아카이브 모드로, 파일의 소유권, 권한, 타임스탬프 등을 유지합니다.
- `-v`: 진행 상황을 자세히 보여줍니다 (verbose).
- `-z`: 전송 중 데이터를 압축합니다.
- `-r`: 하위 디렉터리를 재귀적으로 복사합니다.
- `--delete`: 대상 디렉터리에서 소스에 없는 파일을 삭제합니다.

## 일반 예제
1. 로컬 디렉터리 복사:
   ```bash
   rsync -av /path/to/source/ /path/to/destination/
   ```

2. 원격 서버로 파일 전송:
   ```bash
   rsync -av /path/to/local/file user@remote_host:/path/to/remote/destination/
   ```

3. 원격 서버에서 로컬로 파일 다운로드:
   ```bash
   rsync -av user@remote_host:/path/to/remote/file /path/to/local/destination/
   ```

4. 변경된 파일만 동기화:
   ```bash
   rsync -av --update /path/to/source/ /path/to/destination/
   ```

5. 원격 서버에서 디렉터리 삭제:
   ```bash
   rsync -av --delete /path/to/source/ user@remote_host:/path/to/remote/destination/
   ```

## 팁
- rsync를 사용할 때는 항상 소스와 대상 경로의 끝에 슬래시(`/`)를 주의 깊게 확인하세요. 슬래시의 유무에 따라 복사 방식이 달라질 수 있습니다.
- 대량의 데이터를 전송할 때는 `-z` 옵션을 사용하여 전송 속도를 높일 수 있습니다.
- rsync의 `--dry-run` 옵션을 사용하여 실제 전송 전에 어떤 파일이 복사될지를 미리 확인할 수 있습니다.