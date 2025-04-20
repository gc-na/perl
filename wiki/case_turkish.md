# [Linux] C Shell (csh) case Kullanımı: Değişkenleri Koşullu Olarak İşleme

## Overview
`case` komutu, bir değişkenin değerine göre farklı durumları kontrol etmek ve uygun işlemleri gerçekleştirmek için kullanılır. Bu komut, özellikle birden fazla koşulun kontrol edilmesi gereken durumlarda oldukça faydalıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```csh
case [değişken] in
    [durum1])
        [komutlar]
        ;;
    [durum2])
        [komutlar]
        ;;
    ...
esac
```

## Common Options
`case` komutunun belirli bir seçeneği yoktur, ancak koşulların nasıl yazılacağına dair bazı ipuçları vardır:
- `*`: Herhangi bir değeri temsil eder.
- `?`: Tek bir karakteri temsil eder.
- `[a-z]`: Belirli bir karakter aralığını temsil eder.

## Common Examples

### Örnek 1: Basit Değişken Kontrolü
```csh
set renk = "kırmızı"
case $renk in
    "kırmızı")
        echo "Renk kırmızı."
        ;;
    "mavi")
        echo "Renk mavi."
        ;;
    *)
        echo "Bilinmeyen renk."
        ;;
esac
```

### Örnek 2: Kullanıcı Girişi Kontrolü
```csh
set mevsim = "yaz"
case $mevsim in
    "ilkbahar")
        echo "Doğa canlanıyor."
        ;;
    "yaz")
        echo "Hava sıcak."
        ;;
    "sonbahar")
        echo "Yapraklar dökülüyor."
        ;;
    "kış")
        echo "Kar yağıyor."
        ;;
    *)
        echo "Bilinmeyen mevsim."
        ;;
esac
```

### Örnek 3: Dosya Uzantısına Göre İşlem
```csh
set dosya = "belge.txt"
case $dosya in
    *.txt)
        echo "Bu bir metin dosyası."
        ;;
    *.jpg)
        echo "Bu bir resim dosyası."
        ;;
    *)
        echo "Bilinmeyen dosya türü."
        ;;
esac
```

## Tips
- `case` komutunu kullanırken, her durumdan sonra `;;` eklemeyi unutmayın; bu, her durumun sonunu belirtir.
- Koşulları yazarken, en spesifik olanları en üstte, daha genel olanları ise en altta sıralamak, kodun okunabilirliğini artırır.
- `case` komutunu karmaşık koşullar için kullanmak, kodunuzu daha düzenli ve anlaşılır hale getirebilir.