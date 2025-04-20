# [Linux] C Shell (csh) expr Kullanımı: Matematiksel ifadeleri değerlendirme

## Overview
`expr` komutu, C Shell (csh) ortamında matematiksel ifadeleri değerlendirmek için kullanılan bir araçtır. Bu komut, sayısal hesaplamalar yapmanın yanı sıra, string işlemleri ve mantıksal karşılaştırmalar için de kullanılabilir.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```csh
expr [options] [arguments]
```

## Common Options
- `+` : Toplama işlemi.
- `-` : Çıkarma işlemi.
- `*` : Çarpma işlemi.
- `/` : Bölme işlemi.
- `%` : Modül (kalan) işlemi.
- `=` : Eşitlik kontrolü.
- `!=` : Eşitsizlik kontrolü.

## Common Examples
Aşağıda `expr` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### Toplama İşlemi
```csh
expr 5 + 3
```
Bu komut, 5 ile 3'ü toplar ve sonucu 8 olarak döndürür.

### Çıkarma İşlemi
```csh
expr 10 - 4
```
Bu komut, 10'dan 4'ü çıkarır ve sonucu 6 olarak verir.

### Çarpma İşlemi
```csh
expr 7 \* 6
```
Bu komut, 7 ile 6'yı çarpar ve sonucu 42 olarak döndürür. (Çarpma işlemi için `*` karakteri önüne ters eğik çizgi `\` eklenmelidir.)

### Bölme İşlemi
```csh
expr 20 / 4
```
Bu komut, 20'yi 4'e böler ve sonucu 5 olarak verir.

### Modül İşlemi
```csh
expr 10 % 3
```
Bu komut, 10'un 3'e bölümünden kalanı hesaplar ve sonucu 1 olarak döndürür.

### String Uzunluğu
```csh
expr length "Merhaba"
```
Bu komut, "Merhaba" kelimesinin uzunluğunu hesaplar ve sonucu 7 olarak verir.

## Tips
- `expr` komutunu kullanırken, çarpma işlemi için `*` karakterini kullanmadan önce ters eğik çizgi `\` eklemeyi unutmayın.
- Hesaplamalarda değişken kullanıyorsanız, değişkenin değerini almak için `$` işaretini kullanmayı ihmal etmeyin.
- `expr` komutu, sadece tam sayılarla çalışır; ondalıklı sayılar için başka araçlar kullanmalısınız.