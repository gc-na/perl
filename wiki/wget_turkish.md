# [Linux] C Shell (csh) wget Kullanımı: Dosya indirme aracı

## Genel Bakış
`wget`, web üzerinden dosya indirmek için kullanılan güçlü bir komut satırı aracıdır. HTTP, HTTPS ve FTP protokollerini destekleyerek, kullanıcıların dosyaları kolayca indirmesine olanak tanır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```bash
wget [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-O [dosya_adı]`: İndirilen dosyayı belirtilen adla kaydeder.
- `-c`: Kesilen bir indirmeyi devam ettirir.
- `-q`: Sessiz modda çalışır, yalnızca hata mesajları gösterilir.
- `--limit-rate=[hız]`: İndirme hızını sınırlar.
- `-r`: Dizinleri ve alt dizinleri indirir (rekürsif).

## Yaygın Örnekler
Aşağıda `wget` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. Basit bir dosya indirme:
   ```bash
   wget https://example.com/dosya.zip
   ```

2. İndirilen dosyayı özel bir adla kaydetme:
   ```bash
   wget -O yeni_dosya.zip https://example.com/dosya.zip
   ```

3. Kesilen bir indirmeyi devam ettirme:
   ```bash
   wget -c https://example.com/büyük_dosya.zip
   ```

4. İndirme hızını sınırlama:
   ```bash
   wget --limit-rate=200k https://example.com/dosya.zip
   ```

5. Rekürsif indirme:
   ```bash
   wget -r https://example.com/dizin/
   ```

## İpuçları
- İndirme işlemlerini arka planda gerçekleştirmek için `-b` seçeneğini kullanabilirsiniz.
- İndirilen dosyaların doğruluğunu kontrol etmek için `--no-check-certificate` seçeneğini kullanarak SSL sertifika hatalarını göz ardı edebilirsiniz.
- İndirme işlemlerini zamanlamak için `cron` ile birlikte `wget` kullanmayı düşünebilirsiniz.