# [Linux] C Shell (csh) switch Kullanımı: Komutların durumunu değiştirme

## Overview
`switch` komutu, C Shell (csh) içerisinde belirli bir değişkenin değerine göre farklı durumları kontrol etmek için kullanılır. Bu komut, birden fazla durumu yönetmek için oldukça faydalıdır ve program akışını yönlendirmeye yardımcı olur.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```csh
switch (değişken)
    case değer1:
        komutlar
        breaksw
    case değer2:
        komutlar
        breaksw
    default:
        komutlar
        breaksw
endsw
```

## Common Options
`switch` komutunun kendisi için özel bir seçenek yoktur, ancak `case` ve `default` ifadeleri ile birlikte kullanılır. İşte bazı yaygın kullanımlar:

- `case`: Belirtilen değeri kontrol eder.
- `breaksw`: Mevcut `case` bloğundan çıkmak için kullanılır.
- `default`: Hiçbir `case` ile eşleşmeyen durumlar için varsayılan komutları tanımlar.

## Common Examples

### Örnek 1: Basit Switch Kullanımı
```csh
set renk = "kırmızı"
switch ($renk)
    case "kırmızı":
        echo "Renk kırmızı."
        breaksw
    case "mavi":
        echo "Renk mavi."
        breaksw
    default:
        echo "Bilinmeyen renk."
        breaksw
endsw
```

### Örnek 2: Birden Fazla Durum Kontrolü
```csh
set gün = "Cumartesi"
switch ($gün)
    case "Pazartesi":
    case "Salı":
    case "Çarşamba":
        echo "Hafta içi."
        breaksw
    case "Cumartesi":
    case "Pazar":
        echo "Hafta sonu."
        breaksw
    default:
        echo "Bilinmeyen gün."
        breaksw
endsw
```

### Örnek 3: Kullanıcı Girdisi ile Switch
```csh
echo "Bir sayı girin:"
set sayi = $< 
switch ($sayi)
    case 1:
        echo "Bir."
        breaksw
    case 2:
        echo "İki."
        breaksw
    default:
        echo "Bilinmeyen sayı."
        breaksw
endsw
```

## Tips
- `switch` komutunu kullanırken, her `case` bloğunun sonunda `breaksw` ifadesini eklemeyi unutmayın; aksi takdirde, kontrol akışı bir sonraki `case` bloğuna geçebilir.
- `default` ifadesi, tüm `case` seçeneklerinin dışında kalan durumlar için kullanışlıdır ve hata ayıklama sırasında faydalıdır.
- Değişkenlerinizi tanımlarken, boşluk bırakmamaya dikkat edin; aksi takdirde, `switch` komutu beklenmedik sonuçlar verebilir.