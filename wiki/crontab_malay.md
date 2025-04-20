# [Sistem Operasi] C Shell (csh) crontab: Menjadwalkan tugas secara automatik

## Overview
Perintah `crontab` digunakan untuk menjadwalkan tugas-tugas yang akan dilaksanakan secara automatik pada waktu tertentu di sistem operasi. Ia membolehkan pengguna untuk menjalankan skrip atau perintah secara berkala tanpa perlu campur tangan manual.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `crontab`:

```
crontab [options] [arguments]
```

## Common Options
- `-e`: Mengedit crontab semasa pengguna.
- `-l`: Memaparkan crontab semasa pengguna.
- `-r`: Menghapus crontab semasa pengguna.
- `-i`: Meminta pengesahan sebelum menghapus crontab.

## Common Examples
Berikut adalah beberapa contoh praktikal menggunakan `crontab`:

1. **Menjadwalkan skrip untuk dijalankan setiap hari pada jam 2 pagi:**
   ```bash
   0 2 * * * /path/to/script.sh
   ```

2. **Menjalankan perintah untuk mengemas kini sistem setiap Isnin pada jam 3 petang:**
   ```bash
   0 15 * * 1 sudo apt update
   ```

3. **Menjalankan skrip setiap 15 minit:**
   ```bash
   */15 * * * * /path/to/script.sh
   ```

4. **Menghantar e-mel setiap hari pada jam 8 pagi:**
   ```bash
   0 8 * * * echo "Good Morning!" | mail -s "Daily Greeting" user@example.com
   ```

## Tips
- Sentiasa semak log untuk memastikan tugas yang dijadwalkan berjalan dengan baik.
- Gunakan `crontab -l` untuk menyemak semua tugas yang telah dijadwalkan.
- Pastikan skrip yang dijadwalkan mempunyai hak akses yang betul untuk dilaksanakan.
- Gunakan jalur penuh untuk skrip dan perintah untuk mengelakkan masalah dengan lokasi fail.