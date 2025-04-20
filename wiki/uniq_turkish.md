# [Linux] C Shell (csh) uniq Kullanımı: Tekil satırları listeleme

## Overview
`uniq` komutu, bir dosyadaki veya standart girdi akışındaki ardışık tekrarlanan satırları kaldırarak yalnızca benzersiz satırları listelemeye yarar. Genellikle, sıralı verilerle birlikte kullanılır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```csh
uniq [options] [arguments]
```

## Common Options
- `-c`: Her benzersiz satırın önüne, o satırın kaç kez tekrarlandığını gösteren bir sayı ekler.
- `-d`: Sadece tekrar eden satırları gösterir.
- `-u`: Sadece benzersiz, yani tekrar etmeyen satırları gösterir.
- `-i`: Büyük/küçük harf duyarsız olarak karşılaştırma yapar.

## Common Examples
Aşağıda `uniq` komutunun bazı pratik örnekleri verilmiştir:

1. Bir dosyadaki benzersiz satırları listeleme:
   ```csh
   uniq dosya.txt
   ```

2. Tekrar eden satırları sayma:
   ```csh
   uniq -c dosya.txt
   ```

3. Sadece tekrar eden satırları gösterme:
   ```csh
   uniq -d dosya.txt
   ```

4. Büyük/küçük harf duyarsız karşılaştırma ile benzersiz satırları listeleme:
   ```csh
   uniq -i dosya.txt
   ```

## Tips
- `uniq` komutunu kullanmadan önce verilerin sıralı olduğundan emin olun. Gerekirse `sort` komutunu kullanarak verileri sıralayabilirsiniz.
- `uniq` komutu genellikle `sort` ile birlikte kullanılır. Örneğin, `sort dosya.txt | uniq` komutu, önce dosyayı sıralar, ardından benzersiz satırları listeler.
- Büyük veri setlerinde çalışırken, `-c` seçeneği ile satırların sayısını görmek, hangi satırların daha sık tekrarlandığını anlamanıza yardımcı olabilir.