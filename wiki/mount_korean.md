# [리눅스] C Shell (csh) mount 사용법: 파일 시스템을 마운트합니다.

## Overview
`mount` 명령은 파일 시스템을 특정 디렉토리에 연결하여 사용자가 해당 파일 시스템의 파일에 접근할 수 있도록 합니다. 주로 외부 저장 장치나 네트워크 파일 시스템을 사용할 때 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
mount [options] [arguments]
```

## Common Options
- `-t type`: 마운트할 파일 시스템의 유형을 지정합니다.
- `-o options`: 마운트 옵션을 설정합니다. 예를 들어, 읽기 전용으로 마운트할 수 있습니다.
- `-a`: `/etc/fstab` 파일에 정의된 모든 파일 시스템을 마운트합니다.

## Common Examples
- USB 드라이브를 `/mnt/usb`에 마운트하기:
  ```csh
  mount -t vfat /dev/sdb1 /mnt/usb
  ```
  
- NFS 파일 시스템을 마운트하기:
  ```csh
  mount -t nfs server:/path/to/share /mnt/nfs
  ```

- 읽기 전용으로 마운트하기:
  ```csh
  mount -o ro /dev/sr0 /mnt/cdrom
  ```

- 모든 파일 시스템을 마운트하기:
  ```csh
  mount -a
  ```

## Tips
- 마운트하기 전에 해당 디렉토리가 존재하는지 확인하세요.
- 마운트 해제는 `umount` 명령을 사용하여 수행할 수 있습니다.
- 파일 시스템의 유형을 모를 경우, `blkid` 명령을 사용하여 확인할 수 있습니다.