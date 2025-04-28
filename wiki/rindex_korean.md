<!--
Meta Description: # Perl의 rindex: 문자열 내 마지막 위치 찾기 ## 개요 Perl의 `rindex` 함수는 특정 문자열 내에서 주어진 문자의 마지막 위치를 찾는 데 사용됩니다. 이 함수는 주로 문자열 검색 및 조작을 필요로 하는 경우에 유용합니다. ## 문서화 ### 목적 ...
Meta Keywords: rindex, 문자열, 함수는, string, substring
-->

# Perl의 rindex: 문자열 내 마지막 위치 찾기

## 개요
Perl의 `rindex` 함수는 특정 문자열 내에서 주어진 문자의 마지막 위치를 찾는 데 사용됩니다. 이 함수는 주로 문자열 검색 및 조작을 필요로 하는 경우에 유용합니다.

## 문서화

### 목적
`rindex`는 문자열에서 특정 문자가 마지막으로 나타나는 위치를 반환합니다. 이 함수는 문자열 검색을 수행할 때 유용하며, 찾고자 하는 문자열이 존재하지 않을 경우 -1을 반환합니다.

### 사용법
```perl
rindex(STRING, SUBSTRING)
```

- **STRING**: 검색할 원본 문자열입니다.
- **SUBSTRING**: 검색할 서브 문자열입니다.

### 세부사항
- `rindex`는 문자열의 오른쪽 끝에서부터 왼쪽으로 검색을 수행합니다.
- 문자열의 첫 번째 문자 위치는 0부터 시작합니다.
- 만약 서브 문자열이 문자열에 존재하지 않는 경우, 함수는 -1을 반환합니다.
- 이 함수는 대소문자를 구분합니다.

## 예제

### 기본 사용 예
```perl
my $string = "Hello, world! Welcome to the world of Perl.";
my $substring = "world";

my $last_index = rindex($string, $substring);
print "마지막 'world'의 위치는: $last_index\n";  # 출력: 28
```

### 서브 문자열이 존재하지 않을 경우
```perl
my $string = "Hello, world!";
my $substring = "Perl";

my $last_index = rindex($string, $substring);
print "서브 문자열의 위치는: $last_index\n";  # 출력: -1
```

## 설명
`rindex`를 사용할 때 주의해야 할 점은 대소문자를 구분한다는 것입니다. 따라서 `rindex("Hello", "hello")`는 -1을 반환합니다. 또한, 복잡한 문자열 조작이 필요한 경우, `rindex`와 다른 문자열 관련 함수(예: `index`, `substr`)를 함께 사용하는 것이 유용할 수 있습니다.

## 한 줄 요약
Perl의 `rindex` 함수는 문자열 내에서 특정 문자의 마지막 위치를 찾는 데 사용됩니다.