<!--
Meta Description: # Perl에서의 push: 배열에 요소 추가하기 ## 개요 Perl의 `push` 함수는 배열의 끝에 하나 이상의 요소를 추가하는 데 사용됩니다. 이 함수는 배열의 크기를 동적으로 조정할 수 있도록 해주며, 효율적인 데이터 조작을 가능하게 합니다. ## 문서화 `pu...
Meta Keywords: push, 배열의, 요소를, perl, 추가하는
-->

# Perl에서의 push: 배열에 요소 추가하기

## 개요
Perl의 `push` 함수는 배열의 끝에 하나 이상의 요소를 추가하는 데 사용됩니다. 이 함수는 배열의 크기를 동적으로 조정할 수 있도록 해주며, 효율적인 데이터 조작을 가능하게 합니다.

## 문서화
`push` 함수는 배열의 끝에 하나 이상의 값을 추가하는 간단한 방법을 제공합니다. 기본 구문은 다음과 같습니다:

```perl
push @array, $value1, $value2, ...;
```

- **@array**: 요소를 추가할 배열의 이름입니다.
- **$value1, $value2, ...**: 배열의 끝에 추가할 값입니다. 여러 개의 값을 동시에 추가할 수 있습니다.

### 사용 예시:
```perl
my @fruits = ('apple', 'banana');
push @fruits, 'orange', 'grape';
print join(", ", @fruits);  # 출력: apple, banana, orange, grape
```

## 예제
1. 기본적인 `push` 사용:
   ```perl
   my @numbers = (1, 2, 3);
   push @numbers, 4;
   print "@numbers";  # 결과: 1 2 3 4
   ```

2. 여러 요소 추가:
   ```perl
   my @colors = ('red', 'green');
   push @colors, 'blue', 'yellow';
   print "@colors";  # 결과: red green blue yellow
   ```

3. 배열의 크기 확인:
   ```perl
   my @data = (10, 20);
   push @data, 30;
   my $size = scalar @data;  # 배열의 크기
   print $size;  # 결과: 3
   ```

## 설명
- **배열의 동적 크기**: `push`를 사용하면 배열의 크기를 동적으로 증가시킬 수 있습니다. 이는 스택 구조와 유사하게 작동합니다.
- **성능**: `push`는 배열의 끝에 요소를 추가할 때 매우 효율적입니다. 반면 배열의 시작 부분에 요소를 추가하는 `unshift`는 상대적으로 성능이 떨어질 수 있습니다.
- **리턴 값**: `push`는 배열의 새로운 크기를 반환합니다.

### 일반적인 실수 및 주의사항
- **배열이 정의되어 있어야 함**: `push`를 사용하기 전에 배열이 미리 정의되어 있어야 합니다. 그렇지 않으면 에러가 발생합니다.
- **참조 배열**: 배열의 참조를 사용하여 `push`를 사용할 때는 `push @$array_ref, $value;`와 같은 구문을 사용해야 합니다.

## 한 줄 요약
`push`는 Perl에서 배열의 끝에 하나 이상의 요소를 추가하는 간단하고 효율적인 방법입니다.