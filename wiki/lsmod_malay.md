# [Linux] C Shell (csh) lsmod: Memaparkan modul terpasang

## Overview
Perintah `lsmod` digunakan untuk memaparkan senarai modul kernel yang sedang dipasang pada sistem Linux. Ia memberikan maklumat tentang modul yang aktif dan membantu pengguna memahami lebih lanjut tentang komponen yang sedang berfungsi dalam kernel.

## Usage
Sintaks asas untuk menggunakan perintah `lsmod` adalah seperti berikut:

```csh
lsmod [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `lsmod` beserta penjelasan ringkas:

- `-h`, `--help`: Menunjukkan bantuan dan maklumat tentang penggunaan perintah.
- `-v`, `--version`: Menunjukkan versi perintah `lsmod`.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `lsmod`:

1. **Menampilkan semua modul yang dipasang:**

   ```csh
   lsmod
   ```

2. **Menampilkan bantuan untuk perintah lsmod:**

   ```csh
   lsmod --help
   ```

3. **Menampilkan versi lsmod:**

   ```csh
   lsmod --version
   ```

## Tips
- Gunakan `lsmod` secara berkala untuk memantau modul yang sedang aktif, terutamanya selepas memasang perisian baru.
- Jika anda ingin mendapatkan maklumat lebih terperinci tentang modul tertentu, pertimbangkan untuk menggunakan perintah `modinfo` bersama nama modul tersebut.
- Pastikan anda menjalankan perintah ini dengan hak akses yang sesuai jika anda ingin melihat semua modul yang dipasang.