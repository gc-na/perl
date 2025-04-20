# [Linux] C Shell (csh) crontab Kullanımı: Zamanlanmış görevleri yönetme

## Genel Bakış
`crontab` komutu, belirli zaman dilimlerinde otomatik olarak çalıştırılacak görevleri tanımlamak için kullanılır. Bu komut, sistem yöneticileri ve kullanıcılar tarafından, belirli aralıklarla veya belirli zamanlarda çalıştırılması gereken komutları planlamak için yaygın olarak kullanılır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
crontab [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-e`: Kullanıcının crontab dosyasını düzenlemesine olanak tanır.
- `-l`: Kullanıcının mevcut crontab dosyasını listelemesini sağlar.
- `-r`: Kullanıcının crontab dosyasını siler.
- `-i`: `-r` seçeneği ile birlikte kullanıldığında, silme işlemi öncesinde onay ister.

## Yaygın Örnekler
Aşağıda `crontab` komutunun bazı pratik örnekleri bulunmaktadır:

### 1. Crontab Dosyasını Düzenleme
```bash
crontab -e
```
Bu komut, mevcut crontab dosyasını varsayılan metin düzenleyici ile açar.

### 2. Crontab Dosyasını Listeleme
```bash
crontab -l
```
Bu komut, kullanıcının mevcut crontab dosyasındaki zamanlanmış görevleri gösterir.

### 3. Crontab Dosyasını Silme
```bash
crontab -r
```
Bu komut, kullanıcının crontab dosyasını siler. Silme işlemi onay istemez.

### 4. Her Gün Saat 2'de Bir Yedekleme Yapma
```bash
0 2 * * * /path/to/backup/script.sh
```
Bu satır, her gün saat 02:00'de belirtilen yedekleme betiğini çalıştırır.

### 5. Her Hafta Pazartesi Saat 10'da Bir Rapor Gönderme
```bash
0 10 * * 1 /path/to/report/script.sh
```
Bu satır, her hafta pazartesi günü saat 10:00'da belirtilen rapor betiğini çalıştırır.

## İpuçları
- Crontab dosyasını düzenlerken, her satırın doğru bir şekilde zamanlama formatına uyduğundan emin olun.
- Zamanlama ifadelerinde hata yapmamak için, cron zamanlama formatını kontrol edin.
- Komutların çıktısını bir dosyaya yönlendirmek için, komutun sonuna `>> /path/to/logfile.log 2>&1` ekleyebilirsiniz. Bu, hata mesajlarını da içeren bir günlük dosyası oluşturur.
- Zamanlanmış görevlerinizi test etmek için, önce `crontab -l` ile listeleyin ve ardından belirli bir süre bekleyerek çalışıp çalışmadığını kontrol edin.