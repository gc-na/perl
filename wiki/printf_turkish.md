# [Linux] C Shell (csh) printf Kullanımı: Formatlı çıktı üretme

## Genel Bakış
`printf` komutu, belirli bir formatta çıktı üretmek için kullanılır. C dilindeki `printf` fonksiyonuna benzer şekilde çalışarak, kullanıcıların metin ve değişkenleri belirli bir biçimde ekrana yazdırmasına olanak tanır.

## Kullanım
Temel sözdizimi şu şekildedir:

```csh
printf [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `%s`: String (metin) formatı için kullanılır.
- `%d`: Tam sayı formatı için kullanılır.
- `%f`: Ondalık sayı formatı için kullanılır.
- `\n`: Yeni satır karakteri ekler.
- `\t`: Tab boşluğu ekler.

## Yaygın Örnekler
Aşağıda `printf` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### Örnek 1: Basit metin yazdırma
```csh
printf "Merhaba, Dünya!\n"
```

### Örnek 2: Değişken ile yazdırma
```csh
set isim = "Ali"
printf "Merhaba, %s!\n" $isim
```

### Örnek 3: Tam sayı yazdırma
```csh
set sayi = 42
printf "Sayı: %d\n" $sayi
```

### Örnek 4: Ondalık sayı yazdırma
```csh
set pi = 3.14159
printf "Pi sayısı: %.2f\n" $pi
```

### Örnek 5: Tab ile ayrılmış çıktı
```csh
printf "İsim\tYaş\nAli\t25\nAyşe\t30\n"
```

## İpuçları
- Format belirleyicilerini doğru kullanarak çıktınızı daha okunabilir hale getirin.
- Değişkenlerinizi kullanırken, `$` işaretini unutmayın.
- Uzun metinleri ve verileri daha düzenli bir şekilde yazdırmak için `\n` ve `\t` karakterlerini kullanın.