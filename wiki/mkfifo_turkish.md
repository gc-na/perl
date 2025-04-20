# [Linux] C Shell (csh) mkfifo Kullanımı: İletişim için FIFO dosyaları oluşturma

## Genel Bakış
`mkfifo` komutu, adından da anlaşılacağı gibi, "First In, First Out" (FIFO) dosyaları oluşturmak için kullanılır. FIFO dosyaları, birden fazla süreç arasında veri iletimi sağlamak için kullanılır ve bu dosyalar, verilerin sırayla okunup yazılmasını garanti eder.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```
mkfifo [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-m, --mode=MODE`: Oluşturulan FIFO dosyasının izinlerini belirler.
- `-Z, --context=CONTEXT`: Oluşturulan FIFO dosyasına SELinux bağlamı atar.

## Yaygın Örnekler
Aşağıda `mkfifo` komutunun bazı pratik örnekleri bulunmaktadır:

1. Basit bir FIFO dosyası oluşturma:
   ```csh
   mkfifo myfifo
   ```

2. Belirli bir izinle FIFO dosyası oluşturma:
   ```csh
   mkfifo -m 644 myfifo
   ```

3. Birden fazla FIFO dosyası oluşturma:
   ```csh
   mkfifo fifo1 fifo2 fifo3
   ```

4. SELinux bağlamı ile FIFO dosyası oluşturma:
   ```csh
   mkfifo -Z myfifo
   ```

## İpuçları
- FIFO dosyalarını kullanmadan önce, bu dosyaların hangi süreçler arasında veri iletimi yapacağını planlayın.
- FIFO dosyalarını silmek için `rm` komutunu kullanabilirsiniz.
- FIFO dosyaları, bir süreç yazma işlemi gerçekleştirmeden önce diğer bir sürecin okuma işlemi gerçekleştirmesini bekler, bu nedenle süreçlerin sırasını iyi ayarlayın.