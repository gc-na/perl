# [Sistem Operasi] C Shell (csh) wget Penggunaan: Mengunduh file dari internet

## Overview
Perintah `wget` adalah alat baris perintah yang digunakan untuk mengunduh file dari web. Ini mendukung berbagai protokol seperti HTTP, HTTPS, dan FTP, dan memungkinkan pengguna untuk mengunduh file secara langsung ke sistem mereka.

## Usage
Berikut adalah sintaks dasar dari perintah `wget`:

```csh
wget [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `wget`:

- `-O <file>`: Menentukan nama file output yang diinginkan.
- `-c`: Melanjutkan unduhan yang terputus.
- `-q`: Menjalankan wget dalam mode diam (quiet), tanpa output ke layar.
- `--limit-rate=<rate>`: Membatasi kecepatan unduhan.
- `-r`: Mengunduh secara rekursif, termasuk semua file yang terkait.

## Common Examples
Berikut adalah beberapa contoh penggunaan `wget`:

1. **Mengunduh file tunggal:**
   ```csh
   wget https://example.com/file.zip
   ```

2. **Mengunduh file dengan nama yang berbeda:**
   ```csh
   wget -O myfile.zip https://example.com/file.zip
   ```

3. **Melanjutkan unduhan yang terputus:**
   ```csh
   wget -c https://example.com/file.zip
   ```

4. **Mengunduh secara rekursif:**
   ```csh
   wget -r https://example.com/directory/
   ```

5. **Membatasi kecepatan unduhan:**
   ```csh
   wget --limit-rate=200k https://example.com/file.zip
   ```

## Tips
- Selalu periksa URL yang ingin Anda unduh untuk memastikan keamanannya.
- Gunakan opsi `-q` jika Anda ingin menjalankan unduhan dalam mode diam, terutama saat mengunduh banyak file.
- Jika Anda sering mengunduh file dari situs yang sama, pertimbangkan untuk menggunakan opsi `-r` untuk mengunduh seluruh direktori.