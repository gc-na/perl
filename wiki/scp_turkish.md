# [Linux] C Shell (csh) scp Kullanımı: Dosya transferi için güvenli bir yöntem

## Genel Bakış
`scp` (Secure Copy Protocol), ağ üzerinden dosyaları güvenli bir şekilde kopyalamak için kullanılan bir komuttur. SSH (Secure Shell) protokolünü kullanarak, dosyaların bir makineden diğerine şifreli bir bağlantı üzerinden transfer edilmesini sağlar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```
scp [seçenekler] [kaynak] [hedef]
```

## Yaygın Seçenekler
- `-r`: Klasörleri ve içindeki dosyaları rekürsif olarak kopyalar.
- `-P`: Hedef sunucunun port numarasını belirtir (büyük P).
- `-p`: Dosya zaman damgalarını ve izinlerini korur.
- `-q`: Kopyalama işlemi sırasında herhangi bir çıktı göstermez.

## Yaygın Örnekler
1. Yerel bir dosyayı uzak bir sunucuya kopyalamak:
   ```bash
   scp dosya.txt kullanıcı@sunucu:/hedef/klasör/
   ```

2. Uzak bir sunucudan yerel bir makineye dosya kopyalamak:
   ```bash
   scp kullanıcı@sunucu:/uzak/dosya.txt /yerel/klasör/
   ```

3. Bir klasörü ve içindeki tüm dosyaları uzak bir sunucuya kopyalamak:
   ```bash
   scp -r /yerel/klasör/ kullanıcı@sunucu:/hedef/
   ```

4. Belirli bir port üzerinden dosya kopyalamak:
   ```bash
   scp -P 2222 dosya.txt kullanıcı@sunucu:/hedef/klasör/
   ```

## İpuçları
- Dosya transferi yapmadan önce, hedef sunucuda gerekli izinlere sahip olduğunuzdan emin olun.
- Büyük dosyalar transfer edilirken, bağlantının kesilmemesi için `-C` seçeneği ile sıkıştırma kullanabilirsiniz.
- Dosya transferi sırasında ilerlemeyi görmek için `-v` (verbose) seçeneğini kullanabilirsiniz.