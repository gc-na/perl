# [Linux] C Shell (csh) free kullanım: Bellek durumu görüntüleme

## Genel Bakış
`free` komutu, sistemdeki bellek kullanımını gösterir. Bu komut, toplam bellek, kullanılan bellek, boş bellek ve takas alanı gibi bilgileri sağlar. Bellek yönetimi ve sistem performansını izlemek için oldukça yararlıdır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```
free [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-h`: İnsan tarafından okunabilir formatta çıktı verir (örneğin, KB, MB).
- `-m`: Çıktıyı megabayt cinsinden gösterir.
- `-g`: Çıktıyı gigabayt cinsinden gösterir.
- `-s [saniye]`: Belirtilen saniye aralıklarıyla sürekli güncellemeler yapar.
- `-t`: Toplam bellek kullanımını gösterir.

## Yaygın Örnekler
Aşağıda `free` komutunun bazı pratik örnekleri verilmiştir:

1. Temel bellek durumu görüntüleme:
   ```bash
   free
   ```

2. İnsan tarafından okunabilir formatta bellek durumu görüntüleme:
   ```bash
   free -h
   ```

3. Bellek durumunu megabayt cinsinden görüntüleme:
   ```bash
   free -m
   ```

4. Bellek durumunu sürekli güncelleme (her 5 saniyede bir):
   ```bash
   free -s 5
   ```

5. Toplam bellek kullanımını gösterme:
   ```bash
   free -t
   ```

## İpuçları
- `free` komutunu `watch` ile birleştirerek sürekli güncellemeler alabilirsiniz:
  ```bash
  watch free -h
  ```
- Bellek kullanımını analiz etmek için `free` çıktısını `grep` ile filtreleyebilirsiniz.
- Sistem performansını izlemek için `free` komutunu diğer izleme araçlarıyla birleştirmek faydalı olabilir.