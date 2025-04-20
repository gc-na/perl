# [Linux] C Shell (csh) else komutu: Koşullu ifadelerde alternatif yol

## Genel Bakış
`else` komutu, C Shell (csh) programlama dilinde koşullu ifadelerde alternatif bir yol sunar. Bir `if` koşulu sağlanmadığında, `else` bloğu çalıştırılır. Bu, program akışını kontrol etmek için kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```csh
if (koşul) then
    # koşul doğruysa çalışacak komutlar
else
    # koşul yanlışsa çalışacak komutlar
endif
```

## Yaygın Seçenekler
`else` komutunun kendine özgü seçenekleri yoktur, ancak `if` komutu ile birlikte kullanılır. `if` komutunun bazı yaygın seçenekleri şunlardır:
- `-e`: Dosyanın var olup olmadığını kontrol eder.
- `-d`: Belirtilen yolun bir dizin olup olmadığını kontrol eder.
- `-f`: Belirtilen yolun bir dosya olup olmadığını kontrol eder.

## Yaygın Örnekler
Aşağıda, `else` komutunun kullanıldığı bazı pratik örnekler bulunmaktadır:

### Örnek 1: Dosya var mı kontrolü
```csh
if (-e dosya.txt) then
    echo "Dosya mevcut."
else
    echo "Dosya mevcut değil."
endif
```

### Örnek 2: Dizin kontrolü
```csh
if (-d /home/kullanici) then
    echo "Dizin mevcut."
else
    echo "Dizin mevcut değil."
endif
```

### Örnek 3: Dosya türü kontrolü
```csh
if (-f script.sh) then
    echo "Script dosyası mevcut."
else
    echo "Script dosyası mevcut değil."
endif
```

## İpuçları
- `else` komutunu kullanırken, her zaman `endif` ile kapatmayı unutmayın.
- Koşullarınızı net bir şekilde tanımlamak, kodun okunabilirliğini artırır.
- Birden fazla `if` ve `else` bloğu kullanıyorsanız, kodunuzu düzenli tutmak için uygun girintileme yapın.