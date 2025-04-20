# [Linux] C Shell (csh) iotop Kullanımı: Disk I/O işlemlerini izleme aracı

## Genel Bakış
iotop, sistemdeki disk girdi/çıktı (I/O) işlemlerini izlemek için kullanılan bir komuttur. Bu komut, hangi süreçlerin en fazla I/O kaynağını kullandığını göstererek, sistem performansını analiz etmenize yardımcı olur.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
iotop [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-o`: Sadece I/O işlemi yapan süreçleri gösterir.
- `-b`: Arka planda çalışır ve çıktıyı sürekli günceller.
- `-d <saniye>`: Güncellemeler arasındaki süreyi belirler (varsayılan 1 saniye).
- `-n <sayı>`: Belirtilen sayıda güncelleme sonrası çıkış yapar.

## Yaygın Örnekler
1. **Temel Kullanım**: Tüm I/O işlemlerini izlemek için.
   ```bash
   iotop
   ```

2. **Sadece I/O yapan süreçleri gösterme**:
   ```bash
   iotop -o
   ```

3. **Arka planda çalıştırma ve her 2 saniyede bir güncelleme**:
   ```bash
   iotop -b -d 2
   ```

4. **5 güncellemeden sonra çıkış yapma**:
   ```bash
   iotop -n 5
   ```

## İpuçları
- iotop komutunu çalıştırmak için genellikle root yetkilerine ihtiyaç duyarsınız; bu nedenle `sudo` ile kullanmanız gerekebilir.
- Disk I/O sorunlarını analiz ederken, hangi süreçlerin en fazla kaynak tükettiğini belirlemek için `-o` seçeneğini kullanmak faydalıdır.
- Uzun süreli izleme yapacaksanız, çıktıyı bir dosyaya yönlendirmek için `-b` seçeneği ile birlikte `>` operatörünü kullanabilirsiniz. Örneğin:
  ```bash
  iotop -b -d 2 > iotop_log.txt
  ```