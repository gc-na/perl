# [Sistem Operasi] C Shell (csh) wget Penggunaan: Mengunduh file dari internet

## Overview
Perintah `wget` adalah alat yang digunakan untuk mengunduh file dari web. Ia mendukung berbagai protokol seperti HTTP, HTTPS, dan FTP, serta dapat digunakan untuk mengunduh file secara rekursif dan mengelola unduhan yang terputus.

## Usage
Berikut adalah sintaks dasar dari perintah `wget`:

```
wget [options] [arguments]
```

## Common Options
- `-O [file]`: Menentukan nama file output yang akan disimpan.
- `-c`: Melanjutkan unduhan yang terputus.
- `-r`: Mengunduh file secara rekursif.
- `-p`: Mengunduh semua elemen halaman web yang diperlukan untuk menampilkan halaman secara lengkap.
- `--limit-rate=[rate]`: Membatasi kecepatan unduhan.

## Common Examples
Berikut adalah beberapa contoh penggunaan `wget`:

1. **Mengunduh file tunggal:**
   ```bash
   wget http://example.com/file.zip
   ```

2. **Mengunduh file dengan nama tertentu:**
   ```bash
   wget -O myfile.zip http://example.com/file.zip
   ```

3. **Melanjutkan unduhan yang terputus:**
   ```bash
   wget -c http://example.com/largefile.zip
   ```

4. **Mengunduh seluruh situs web secara rekursif:**
   ```bash
   wget -r http://example.com/
   ```

5. **Mengunduh halaman web beserta semua elemen yang diperlukan:**
   ```bash
   wget -p http://example.com/page.html
   ```

## Tips
- Selalu gunakan opsi `-c` jika Anda mengunduh file besar untuk menghindari kehilangan data jika koneksi terputus.
- Gunakan opsi `--limit-rate` untuk menghindari penggunaan bandwidth yang berlebihan saat mengunduh.
- Jika Anda mengunduh banyak file, pertimbangkan untuk menggunakan opsi `-r` dengan hati-hati agar tidak membebani server.