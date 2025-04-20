# [Linux] C Shell (csh) mpstat Kullanımı: Sistem performansını izleme aracı

## Genel Bakış
mpstat komutu, çoklu işlemci sistemlerinde CPU kullanımını izlemek için kullanılır. Bu komut, her bir işlemcinin veya çekirdeğin performansını ayrı ayrı göstererek, sistemin genel yük durumunu analiz etmeye yardımcı olur.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```bash
mpstat [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-P ALL`: Tüm işlemcilerin istatistiklerini gösterir.
- `-u`: Kullanıcı ve sistem CPU kullanım yüzdelerini gösterir.
- `-h`: Çıktıyı daha okunabilir hale getirir.
- `-s`: İstatistikleri belirli bir süre aralığında toplar.

## Yaygın Örnekler
Aşağıda mpstat komutunun bazı pratik kullanımları verilmiştir:

1. Tüm işlemcilerin istatistiklerini görüntüleme:
   ```bash
   mpstat -P ALL
   ```

2. CPU kullanımını her 5 saniyede bir güncelleme:
   ```bash
   mpstat 5
   ```

3. Kullanıcı ve sistem CPU kullanım yüzdelerini gösterme:
   ```bash
   mpstat -u
   ```

4. Çıktıyı daha okunabilir hale getirme:
   ```bash
   mpstat -h
   ```

## İpuçları
- mpstat komutunu, sistem performansını izlemek için bir izleme aracı olarak kullanın ve zamanla CPU kullanımındaki değişiklikleri analiz edin.
- Uzun süreli izleme için, mpstat çıktısını bir dosyaya yönlendirin:
  ```bash
  mpstat 5 > cpu_usage.txt
  ```
- Belirli bir işlemci üzerinde yoğunlaşmak istiyorsanız, `-P` seçeneği ile işlemci numarasını belirleyin:
  ```bash
  mpstat -P 0 5
  ```