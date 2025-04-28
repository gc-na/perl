<!--
Meta Description: # Perl의 substr 함수: 문자열 조작의 기초 ## 개요 Perl의 `substr` 함수는 문자열에서 특정 위치의 부분 문자열을 추출하거나 수정하는 데 사용됩니다. 문자열 처리 작업에서 매우 유용하며, 다양한 상황에서 활용될 수 있습니다. ## 문서화 ### 목...
Meta Keywords: 문자열의, substr, string, 문자열, perl
-->

# Perl의 substr 함수: 문자열 조작의 기초

## 개요
Perl의 `substr` 함수는 문자열에서 특정 위치의 부분 문자열을 추출하거나 수정하는 데 사용됩니다. 문자열 처리 작업에서 매우 유용하며, 다양한 상황에서 활용될 수 있습니다.

## 문서화
### 목적
`substr` 함수는 문자열의 특정 위치에서 시작하여 지정된 길이만큼의 부분 문자열을 반환하거나, 그 위치의 문자열을 수정할 수 있습니다. 이를 통해 문자열 데이터의 조작이 용이해집니다.

### 사용법
```perl
substr($string, $offset, $length, $replacement);
```

- `$string`: 조작할 원본 문자열.
- `$offset`: 부분 문자열의 시작 위치. 0부터 시작합니다.
- `$length`: 추출할 문자열의 길이(옵션). 생략 시, `$offset`부터 문자열의 끝까지 모두 추출합니다.
- `$replacement`: (옵션) 지정한 위치에 삽입할 문자열. 이 인자가 제공되면, 부분 문자열이 대체됩니다.

### 예시
1. 기본적인 부분 문자열 추출:
   ```perl
   my $string = "Hello, World!";
   my $substring = substr($string, 7, 5); # "World"
   print $substring; # 출력: World
   ```

2. 문자열의 끝까지 추출:
   ```perl
   my $string = "Hello, World!";
   my $substring = substr($string, 7); # "World!"
   print $substring; # 출력: World!
   ```

3. 문자열 수정:
   ```perl
   my $string = "Hello, World!";
   substr($string, 7, 5, "Perl"); # "Hello, Perl!"
   print $string; # 출력: Hello, Perl!
   ```

## 설명
`substr` 함수는 문자열 처리 시 자주 사용되는 함수입니다. 주의할 점은 `$offset` 값이 문자열의 길이를 초과하면 빈 문자열을 반환하며, 음수값을 사용할 경우 문자열의 끝에서부터 계산됩니다. 또한, `$length`가 0일 경우, 아무것도 추출하지 않으며, 대체 문자열의 길이는 기존 문자열의 길이와 관계없이 설정할 수 있습니다.

### 일반적인 실수 및 유의 사항
- `$offset`이 음수인 경우, 문자열의 끝에서부터 오프셋을 계산합니다. 예를 들어, `substr($string, -1)`은 문자열의 마지막 문자 하나를 반환합니다.
- `$length` 파라미터를 지정하지 않으면, `$offset`부터 문자열의 끝까지 모든 문자열이 반환됩니다.
- 대체 문자열을 제공하는 경우, 기존의 문자열이 수정되므로 주의가 필요합니다. 원본 문자열의 값이 변경될 수 있습니다.

## 한 줄 요약
Perl의 `substr` 함수는 문자열에서 특정 부분을 추출하거나 수정하는 데 유용한 도구입니다.