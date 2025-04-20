# [리눅스] C Shell (csh) resize2fs 사용법: 파일 시스템 크기 조정

## Overview
`resize2fs` 명령은 리눅스에서 ext2, ext3, ext4 파일 시스템의 크기를 조정하는 데 사용됩니다. 이 명령은 파일 시스템의 크기를 늘리거나 줄이는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
resize2fs [옵션] [인수]
```

## Common Options
- `-f`: 강제로 크기를 조정합니다.
- `-p`: 진행 상황을 표시합니다.
- `-s`: 파일 시스템의 크기를 줄입니다.
- `-M`: 파일 시스템을 최소 크기로 조정합니다.

## Common Examples
1. 파일 시스템 크기 늘리기:
   ```bash
   resize2fs /dev/sda1
   ```

2. 특정 크기로 파일 시스템 조정하기:
   ```bash
   resize2fs /dev/sda1 20G
   ```

3. 파일 시스템 크기 줄이기:
   ```bash
   resize2fs -s /dev/sda1
   ```

4. 진행 상황 표시하면서 크기 조정하기:
   ```bash
   resize2fs -p /dev/sda1
   ```

## Tips
- 크기 조정 전에 항상 데이터 백업을 권장합니다.
- 파일 시스템을 조정하기 전에 해당 파일 시스템이 마운트 해제되어 있는지 확인하세요.
- `resize2fs`를 사용하기 전에 파일 시스템의 상태를 확인하기 위해 `e2fsck` 명령을 사용하는 것이 좋습니다.