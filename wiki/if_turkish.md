# [Linux] C Shell (csh) if kullanımı: Koşullu ifadeleri değerlendirme

## Overview
`if` komutu, belirli bir koşulun doğru olup olmadığını kontrol etmek için kullanılır. Eğer koşul doğruysa, belirli bir komut veya komutlar grubu çalıştırılır. Bu, betik yazımında akış kontrolü sağlamak için oldukça yararlıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```csh
if (koşul) then
    komutlar
endif
```

## Common Options
- `then`: Koşulun doğru olduğu durumda çalıştırılacak komutların başlangıcını belirtir.
- `endif`: `if` bloğunun sonunu belirtir.

## Common Examples
Aşağıda `if` komutunun bazı pratik örnekleri verilmiştir:

### Örnek 1: Basit Koşul Kontrolü
Bir dosyanın var olup olmadığını kontrol etme:

```csh
if (-e dosya.txt) then
    echo "Dosya mevcut."
endif
```

### Örnek 2: Sayı Karşılaştırması
Bir sayının pozitif olup olmadığını kontrol etme:

```csh
set sayi = 5
if ($sayi > 0) then
    echo "Sayı pozitif."
endif
```

### Örnek 3: Birden Fazla Koşul
Bir değişkenin belirli bir değere eşit olup olmadığını kontrol etme:

```csh
set renk = "kırmızı"
if ($renk == "kırmızı") then
    echo "Renk kırmızı."
else
    echo "Renk kırmızı değil."
endif
```

## Tips
- Koşul ifadelerinde dikkatli olun; doğru sözdizimi kullanmak önemlidir.
- `if` komutunu karmaşık koşullar için `else` ve `else if` ile birleştirerek daha esnek hale getirebilirsiniz.
- Koşul ifadelerini test etmek için `echo` komutunu kullanarak çıktıları kontrol etmek, hata ayıklamada faydalı olabilir.