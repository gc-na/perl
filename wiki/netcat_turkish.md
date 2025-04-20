# [Linux] C Shell (csh) netcat Kullanımı: Ağ bağlantıları oluşturma ve veri iletme aracı

## Genel Bakış
Netcat, ağ bağlantıları oluşturmak ve veri iletmek için kullanılan güçlü bir araçtır. TCP ve UDP protokollerini destekler ve genellikle ağ sorunlarını gidermek, veri transferi yapmak veya basit bir sunucu/istemci uygulaması oluşturmak için kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
netcat [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-l`: Dinleme modunu etkinleştirir.
- `-p`: Belirtilen port numarasını kullanır.
- `-u`: UDP protokolünü kullanır.
- `-v`: Ayrıntılı çıktı sağlar.
- `-w`: Zaman aşım süresini ayarlar.

## Yaygın Örnekler
Aşağıda netcat komutunun bazı pratik kullanımları verilmiştir:

### 1. Basit bir TCP sunucusu oluşturma
Aşağıdaki komut, 1234 numaralı portta dinleyen bir TCP sunucusu oluşturur:
```bash
netcat -l -p 1234
```

### 2. TCP istemcisi ile bağlantı kurma
Aşağıdaki komut, 192.168.1.1 IP adresindeki 1234 numaralı porta bağlanır:
```bash
netcat 192.168.1.1 1234
```

### 3. UDP ile veri gönderme
Aşağıdaki komut, 1234 numaralı porta UDP üzerinden veri gönderir:
```bash
echo "Merhaba, dünya!" | netcat -u 192.168.1.1 1234
```

### 4. Dosya transferi
Aşağıdaki komut, bir dosyayı başka bir makineye gönderir:
```bash
netcat -l -p 1234 > alinan_dosya.txt
```
Ve alıcı makinede:
```bash
netcat 192.168.1.1 1234 < gonderilen_dosya.txt
```

## İpuçları
- Netcat'i kullanırken, güvenlik duvarı ayarlarınızı kontrol edin; bazı portlar kapalı olabilir.
- Dinleme modunda çalışırken, istemcilerin bağlanmasına izin vermek için uygun portları açtığınızdan emin olun.
- Netcat ile veri transferi yaparken, veri bütünlüğünü sağlamak için `-w` seçeneği ile zaman aşım süresi ayarlamak faydalı olabilir.