<!--
Meta Description: # Perl의 readdir 함수: 파일 디렉토리 읽기 ## 개요 Perl의 `readdir` 함수는 디렉토리 핸들을 통해 지정된 디렉토리에서 파일 및 서브디렉토리의 목록을 읽어오는 데 사용됩니다. 이 함수는 파일 시스템 작업을 수행하는 데 매우 유용합니다. ## 문서...
Meta Keywords: 디렉토리, readdir, 함수는, 핸들을, 디렉토리를
-->

# Perl의 readdir 함수: 파일 디렉토리 읽기

## 개요
Perl의 `readdir` 함수는 디렉토리 핸들을 통해 지정된 디렉토리에서 파일 및 서브디렉토리의 목록을 읽어오는 데 사용됩니다. 이 함수는 파일 시스템 작업을 수행하는 데 매우 유용합니다.

## 문서
### 목적
`readdir` 함수는 특정 디렉토리에 있는 모든 파일과 서브디렉토리의 이름을 반환합니다. 이 함수는 디렉토리 핸들을 인자로 받아 해당 핸들이 가리키는 디렉토리의 내용을 읽습니다.

### 사용법
```perl
opendir(my $dir_handle, '디렉토리_경로') or die "디렉토리를 열 수 없습니다: $!";
while (my $file = readdir($dir_handle)) {
    print "$file\n";
}
closedir($dir_handle);
```

### 세부 사항
- `opendir` 함수로 디렉토리를 열고, 이때 생성된 핸들을 `readdir`에 전달합니다.
- `readdir`는 디렉토리 내의 파일 이름을 하나씩 반환합니다.
- 모든 파일을 읽은 후, `closedir`로 디렉토리 핸들을 닫아야 합니다.
- `readdir`은 '.'(현재 디렉토리)와 '..'(상위 디렉토리)도 포함하여 반환합니다.

## 예제
```perl
use strict;
use warnings;

# 디렉토리 열기
opendir(my $dh, "/path/to/directory") or die "디렉토리를 열 수 없습니다: $!";

# 디렉토리 내용 읽기
while (my $entry = readdir($dh)) {
    print "$entry\n";
}

# 디렉토리 닫기
closedir($dh);
```

## 설명
- `readdir`을 사용할 때, 반환되는 파일 목록에 '.'와 '..'가 포함된다는 점을 유의해야 합니다. 이를 필터링하려면 추가 조건을 걸어주어야 합니다.
- 디렉토리 핸들이 유효하지 않거나 디렉토리를 찾을 수 없으면 `undef`를 반환하며, 이 경우 오류 처리가 필요합니다.
- `readdir`은 환경에 따라 읽는 속도에 영향을 받을 수 있으므로, 큰 디렉토리의 경우 성능에 유의해야 합니다.

## 한 줄 요약
Perl의 `readdir` 함수는 디렉토리 핸들을 통해 파일 및 서브디렉토리 목록을 읽어오는 기능을 제공합니다.