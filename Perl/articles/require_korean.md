<!--
Meta Description: # Perl에서의 require: 모듈 및 파일 포함 명령어 ## 개요 Perl의 `require`는 다른 Perl 스크립트나 모듈을 현재 스크립트에 포함시키는 명령어로, 주로 코드 재사용과 모듈화를 위해 사용됩니다. 이 명령어는 필요한 모듈이나 파일이 이미 로드되지 ...
Meta Keywords: require, perl, mymodule, 모듈을, 파일을
-->

# Perl에서의 require: 모듈 및 파일 포함 명령어

## 개요
Perl의 `require`는 다른 Perl 스크립트나 모듈을 현재 스크립트에 포함시키는 명령어로, 주로 코드 재사용과 모듈화를 위해 사용됩니다. 이 명령어는 필요한 모듈이나 파일이 이미 로드되지 않은 경우에만 해당 파일을 실행합니다.

## 문서화
### 목적
`require`는 Perl 프로그램에서 외부 파일이나 모듈을 동적으로 로드하여 코드의 구조를 개선하고, 필요한 기능을 모듈화하여 관리하기 쉽게 합니다.

### 사용법
`require`는 다음과 같이 사용됩니다:

```perl
require 'filename.pl';
```

또는 모듈을 불러올 경우:

```perl
require ModuleName;
```

- `filename.pl`: 포함할 Perl 스크립트의 파일 경로입니다.
- `ModuleName`: 포함할 Perl 모듈의 이름입니다. 파일 확장자는 필요하지 않습니다.

### 세부 사항
- `require`는 런타임에 파일을 로드합니다. 즉, 프로그램 실행 중에 필요할 때만 파일을 로드합니다.
- 동일한 파일을 여러 번 `require`하면, 첫 번째 호출 이후에는 다시 로드되지 않습니다. 이는 중복 실행을 방지합니다.
- `require`는 Perl의 모듈 시스템과 함께 사용할 때, `use`와 다르게 동작합니다. `use`는 컴파일 타임에 모듈을 로드하지만, `require`는 런타임에 로드합니다.

## 예제
### 기본 사용 예
1. 일반 파일 포함
```perl
# example.pl
print "Hello from example.pl\n";

# main.pl
require 'example.pl';
```
위의 코드를 실행하면 `example.pl`의 내용이 출력됩니다.

2. 모듈 포함
```perl
# MyModule.pm
package MyModule;
sub greet {
    print "Hello from MyModule!\n";
}
1;

# main.pl
require MyModule;
MyModule::greet();
```
위의 코드를 실행하면 `MyModule`의 `greet` 함수가 호출되어 출력됩니다.

## 설명
### 일반적인 함정 및 주의사항
- 경로 문제: `require`에 지정한 파일이나 모듈의 경로가 정확해야 하며, 경로가 잘못되면 오류가 발생합니다.
- 사용 시기: `require`는 런타임에 파일을 로드하므로, 모듈 내에서 사용되는 변수가 초기화되지 않을 수 있습니다.
- 모듈 이름: `require`를 사용할 때는 모듈 이름의 대소문자를 정확히 맞춰야 하며, 파일 확장자는 필요하지 않습니다.

## 한줄 요약
Perl의 `require` 명령어는 외부 파일이나 모듈을 런타임에 동적으로 로드하여 코드의 재사용성과 모듈화를 돕는 기능입니다.