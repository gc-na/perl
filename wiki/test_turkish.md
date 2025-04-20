# [Linux] C Shell (csh) test Kullanımı: Koşul ifadelerini değerlendirme

## Overview
`test` komutu, belirli koşulları değerlendirmek için kullanılan bir komuttur. Bu komut, dosya varlığı, dosya türü, sayısal karşılaştırmalar ve metin karşılaştırmaları gibi çeşitli koşulları kontrol etmek için kullanılabilir. `test` komutu, genellikle betiklerde ve koşullu ifadelerde kullanılır.

## Usage
Temel sözdizimi şu şekildedir:

```csh
test [options] [arguments]
```

## Common Options
- `-e [dosya]`: Belirtilen dosyanın var olup olmadığını kontrol eder.
- `-f [dosya]`: Belirtilen dosyanın bir dosya olup olmadığını kontrol eder.
- `-d [dosya]`: Belirtilen dosyanın bir dizin olup olmadığını kontrol eder.
- `-z [string]`: Belirtilen string'in boş olup olmadığını kontrol eder.
- `-n [string]`: Belirtilen string'in boş olmadığını kontrol eder.
- `[sayısal1] -eq [sayısal2]`: İki sayının eşit olup olmadığını kontrol eder.
- `[sayısal1] -ne [sayısal2]`: İki sayının eşit olmadığını kontrol eder.

## Common Examples
Aşağıda `test` komutunun bazı pratik örnekleri verilmiştir:

### Dosya Varlığını Kontrol Etme
```csh
if (test -e myfile.txt) then
    echo "myfile.txt mevcut."
else
    echo "myfile.txt mevcut değil."
endif
```

### Dizin Kontrolü
```csh
if (test -d mydirectory) then
    echo "mydirectory bir dizin."
else
    echo "mydirectory bir dizin değil."
endif
```

### Boş String Kontrolü
```csh
set mystring = ""
if (test -z "$mystring") then
    echo "String boş."
else
    echo "String boş değil."
endif
```

### Sayısal Karşılaştırma
```csh
set num1 = 5
set num2 = 10
if (test $num1 -lt $num2) then
    echo "$num1, $num2'den küçüktür."
endif
```

## Tips
- `test` komutunu kullanırken, koşul ifadelerini parantez içinde yazmak iyi bir uygulamadır.
- `test` yerine `[` ve `]` kullanarak da aynı koşulları kontrol edebilirsiniz; örneğin, `if [ -e myfile.txt ]; then ...`.
- Koşul ifadelerinde, `&&` ve `||` gibi mantıksal operatörleri kullanarak birden fazla koşulu birleştirebilirsiniz.