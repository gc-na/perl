# [Linux] C Shell (csh) psql Kullanımı: PostgreSQL veritabanına erişim

## Genel Bakış
`psql`, PostgreSQL veritabanı yönetim sistemi için bir komut satırı arayüzüdür. Kullanıcıların veritabanlarına bağlanmasını, SQL sorguları çalıştırmasını ve veritabanı yönetim görevlerini gerçekleştirmesini sağlar.

## Kullanım
Temel sözdizimi şu şekildedir:
```bash
psql [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-h`: Veritabanı sunucusunun adresini belirtir.
- `-U`: Veritabanı kullanıcı adını tanımlar.
- `-d`: Bağlanılacak veritabanının adını belirtir.
- `-p`: Veritabanı sunucusunun port numarasını tanımlar.
- `-f`: Belirtilen dosyadaki SQL komutlarını çalıştırır.

## Yaygın Örnekler
Aşağıda `psql` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. Belirli bir veritabanına bağlanma:
   ```bash
   psql -h localhost -U kullanici_adi -d veritabani_adi
   ```

2. SQL dosyasını çalıştırma:
   ```bash
   psql -U kullanici_adi -d veritabani_adi -f dosya.sql
   ```

3. Veritabanındaki tabloları listeleme:
   ```bash
   psql -U kullanici_adi -d veritabani_adi -c "\dt"
   ```

4. Belirli bir sorguyu çalıştırma:
   ```bash
   psql -U kullanici_adi -d veritabani_adi -c "SELECT * FROM tablo_adi;"
   ```

## İpuçları
- `psql` oturumunu başlatmadan önce, gerekli kullanıcı adı ve veritabanı bilgilerini doğru girdiğinizden emin olun.
- SQL sorgularınızı test etmek için `-c` seçeneğini kullanarak tek satırlık sorgular çalıştırabilirsiniz.
- Sık kullanılan komutları bir dosyaya kaydedip `-f` seçeneği ile çalıştırarak zaman kazanabilirsiniz.