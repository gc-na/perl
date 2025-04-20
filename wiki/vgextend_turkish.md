# [Linux] C Shell (csh) vgextend Kullanımı: Mevcut bir hacme yeni fiziksel hacimler ekler

## Genel Bakış
`vgextend` komutu, mevcut bir hacme (volume group) yeni fiziksel hacimler eklemek için kullanılır. Bu, depolama alanını genişletmek ve daha fazla veri saklamak için yararlıdır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```csh
vgextend [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-l, --maxlogicalextents`: Eklenebilecek maksimum mantıksal genişletme sayısını belirtir.
- `-n, --nosync`: Hacim grubunu senkronize etmeden ekleme yapar.
- `-f, --force`: Zorla ekleme yapar, hata mesajlarını göz ardı eder.

## Yaygın Örnekler
Aşağıda `vgextend` komutunun bazı pratik örnekleri bulunmaktadır:

1. Yeni bir fiziksel hacmi mevcut bir hacim grubuna eklemek:
   ```csh
   vgextend my_volume_group /dev/sdb1
   ```

2. Birden fazla fiziksel hacmi aynı anda eklemek:
   ```csh
   vgextend my_volume_group /dev/sdb1 /dev/sdc1
   ```

3. Maksimum mantıksal genişletme sayısını belirterek ekleme yapmak:
   ```csh
   vgextend -l 100 my_volume_group /dev/sdb1
   ```

## İpuçları
- Hacim grubunu genişletmeden önce mevcut durumu kontrol etmek için `vgs` komutunu kullanın.
- Eklediğiniz fiziksel hacimlerin uygun şekilde biçimlendirildiğinden emin olun.
- `vgdisplay` komutunu kullanarak hacim grubunun güncel durumunu kontrol edin.