<!--
Meta Description: # Perl의 wantarray: 배열 및 스칼라 반환을 위한 기능 ## 개요 `wantarray`는 Perl에서 함수가 호출될 때 반환될 값의 컨텍스트를 확인하는 데 사용되는 특별한 함수입니다. 이 기능은 함수가 스칼라, 배열, 또는 정의되지 않은 상태로 호출될 때 ...
Meta Keywords: wantarray, return, 스칼라, 컨텍스트를, 정의되지
-->

# Perl의 wantarray: 배열 및 스칼라 반환을 위한 기능

## 개요
`wantarray`는 Perl에서 함수가 호출될 때 반환될 값의 컨텍스트를 확인하는 데 사용되는 특별한 함수입니다. 이 기능은 함수가 스칼라, 배열, 또는 정의되지 않은 상태로 호출될 때 각각의 반환값을 조절할 수 있도록 도와줍니다.

## 문서
### 목적
`wantarray`는 함수가 호출된 컨텍스트를 감지하여 함수의 반환값을 조건에 맞게 조정할 수 있도록 하는 기능입니다. 이는 코드의 유연성을 높이고, 다양한 반환 형태를 지원하는 데 유용합니다.

### 사용법
`wantarray`는 호출된 함수 내에서 사용되며, 다음과 같이 작동합니다:
- 반환 컨텍스트가 배열인 경우, `wantarray`는 참(true)을 반환합니다.
- 반환 컨텍스트가 스칼라인 경우, `wantarray`는 거짓(false)을 반환합니다.
- 반환 컨텍스트가 정의되지 않은 경우, `wantarray`는 `undef`를 반환합니다.

```perl
sub example {
    if (wantarray) {
        return (1, 2, 3);  # 배열 반환
    } else {
        return 42;          # 스칼라 반환
    }
}
```

## 예제
다음은 `wantarray`의 기본적인 사용 예제입니다.

### 예제 1: 배열 반환
```perl
sub get_values {
    if (wantarray) {
        return (1, 2, 3);
    }
    return 0;
}

my @array = get_values();  # 배열로 호출
print "@array\n";          # 출력: 1 2 3
```

### 예제 2: 스칼라 반환
```perl
sub get_value {
    if (wantarray) {
        return (1, 2, 3);
    }
    return 0;
}

my $scalar = get_value();  # 스칼라로 호출
print "$scalar\n";         # 출력: 0
```

### 예제 3: 정의되지 않은 상태
```perl
sub check_context {
    return wantarray;
}

my $context = check_context();  # 정의되지 않은 호출
print "$context\n";              # 출력: 
```

## 설명
`wantarray`를 사용할 때 주의해야 할 점은 다음과 같습니다:
- `wantarray`는 항상 함수 내에서만 호출해야 하며, 호출된 컨텍스트에 따라 다르게 반응합니다.
- 이 기능은 주로 다형성을 구현할 때 유용하지만, 코드의 복잡성을 증가시킬 수 있으므로 신중하게 사용해야 합니다.
- `wantarray`는 값이 필요할 때마다 호출되는 것이 아니라, 호출 시점에 해당 컨텍스트를 체크하므로 성능에 큰 영향을 미치지 않습니다.

## 한 줄 요약
`wantarray`는 Perl에서 함수의 반환 컨텍스트를 확인하여 스칼라 또는 배열 형태로 값을 반환할 수 있도록 지원하는 기능입니다.