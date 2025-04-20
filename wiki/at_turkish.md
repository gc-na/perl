# [Linux] C Shell (csh) at: Zamanlanmış görevleri yürütme

## Overview
`at` komutu, belirli bir zamanda bir komut veya bir komut dosyasını çalıştırmak için kullanılır. Kullanıcılar, belirli bir tarih ve saatte çalıştırılacak görevleri zamanlayabilirler.

## Usage
Temel sözdizimi şu şekildedir:
```
at [options] [arguments]
```

## Common Options
- `-f <file>`: Belirtilen dosyadaki komutları çalıştırır.
- `-l`: Zamanlanmış görevlerin listesini gösterir.
- `-d <job_id>`: Belirtilen iş kimliğine sahip zamanlanmış görevi iptal eder.
- `-m`: Görev tamamlandığında e-posta bildirimi gönderir.

## Common Examples
Aşağıda `at` komutunun bazı pratik örnekleri bulunmaktadır:

1. **Bir komutu belirli bir zamanda çalıştırma:**
   ```bash
   echo "backup.sh" | at 15:00
   ```
   Bu komut, `backup.sh` dosyasını her gün saat 15:00'te çalıştırır.

2. **Bir dosyadaki komutları çalıştırma:**
   ```bash
   at -f myscript.sh 09:00
   ```
   Bu komut, `myscript.sh` dosyasındaki komutları her gün saat 09:00'da çalıştırır.

3. **Zamanlanmış görevlerin listesini görüntüleme:**
   ```bash
   at -l
   ```
   Bu komut, mevcut zamanlanmış görevlerin listesini gösterir.

4. **Bir zamanlanmış görevi iptal etme:**
   ```bash
   at -d 2
   ```
   Bu komut, iş kimliği 2 olan zamanlanmış görevi iptal eder.

## Tips
- `at` komutunu kullanmadan önce, sisteminizde `atd` hizmetinin çalıştığından emin olun.
- Zamanlama yaparken, tarih ve saat formatına dikkat edin; `at` komutu, sistem saatine göre çalışır.
- Görevlerinizi takip etmek için düzenli olarak `at -l` komutunu kullanarak zamanlanmış görevlerinizi kontrol edin.