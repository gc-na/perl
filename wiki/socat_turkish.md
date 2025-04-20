# [Linux] C Shell (csh) socat Kullanımı: İletişim kanalları arasında veri aktarımı

## Genel Bakış
socat, iki veri akışı arasında veri aktarımını sağlayan bir komut satırı aracıdır. Bu, ağ bağlantıları, dosyalar veya diğer veri kaynakları arasında veri yönlendirmek için kullanılabilir. socat, çok çeşitli protokolleri destekler ve esnekliği sayesinde birçok farklı senaryoda kullanılabilir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
socat [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-d`: Hata ayıklama modunu etkinleştirir.
- `-v`: Veri aktarımını gösterir; gönderilen ve alınan verileri ekrana yazdırır.
- `tcp:<host>:<port>`: Belirtilen host ve port üzerinden TCP bağlantısı kurar.
- `udp:<host>:<port>`: Belirtilen host ve port üzerinden UDP bağlantısı kurar.
- `file:<dosya_adı>`: Belirtilen dosyayı veri kaynağı veya hedefi olarak kullanır.

## Yaygın Örnekler

1. **Yerel bir TCP sunucusu oluşturma:**
   ```bash
   socat TCP-LISTEN:1234,fork EXEC:/bin/cat
   ```
   Bu komut, 1234 numaralı portta dinleyen bir TCP sunucusu oluşturur ve gelen verileri `cat` komutuna yönlendirir.

2. **Bir dosyadan veri okuma ve TCP üzerinden gönderme:**
   ```bash
   socat TCP:localhost:1234 file:data.txt
   ```
   `data.txt` dosyasındaki verileri, localhost üzerindeki 1234 numaralı porta gönderir.

3. **UDP üzerinden veri iletimi:**
   ```bash
   socat -v UDP-RECVFROM:1234 STDOUT
   ```
   Bu komut, 1234 numaralı port üzerinden gelen UDP verilerini ekrana yazdırır.

4. **İki terminal arasında veri iletimi:**
   ```bash
   socat PTY,link=/tmp/ttyS0,raw TCP:localhost:1234
   ```
   Bu komut, bir terminal ile localhost üzerindeki 1234 numaralı port arasında bir bağlantı oluşturur.

## İpuçları
- Hata ayıklama için `-d` ve `-v` seçeneklerini kullanarak veri akışını izleyebilirsiniz.
- Güvenlik açısından, açık portları kullanırken dikkatli olun ve yalnızca güvenilir kaynaklarla bağlantı kurun.
- Farklı protokoller arasında geçiş yaparken, uygun seçenekleri kullanarak bağlantı türünü belirttiğinizden emin olun.