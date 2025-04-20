# [Sistem Operasi] C Shell (csh) command `echo`: Mencetak teks ke skrin

## Overview
Perintah `echo` dalam C Shell digunakan untuk mencetak teks atau nilai ke skrin. Ia sering digunakan dalam skrip untuk memberikan maklumat kepada pengguna atau untuk mengesahkan nilai pembolehubah.

## Usage
Sintaks asas untuk perintah `echo` adalah seperti berikut:

```
echo [options] [string]
```

## Common Options
- `-n`: Tidak mencetak newline di akhir output.
- `-e`: Mengaktifkan pengendalian karakter khas seperti `\n` (newline) dan `\t` (tab).
- `-E`: Menonaktifkan pengendalian karakter khas (ini adalah pilihan lalai).

## Common Examples
1. Mencetak teks biasa:
   ```csh
   echo "Hello, World!"
   ```

2. Mencetak tanpa newline:
   ```csh
   echo -n "Hello, "
   echo "World!"
   ```

3. Menggunakan karakter khas:
   ```csh
   echo -e "Baris pertama\nBaris kedua"
   ```

4. Mencetak nilai pembolehubah:
   ```csh
   set name = "Ali"
   echo "Nama saya adalah $name"
   ```

## Tips
- Gunakan `-n` jika anda ingin mencetak beberapa baris tanpa ruang kosong di antara mereka.
- Untuk mencetak karakter khas, pastikan untuk menggunakan pilihan `-e`.
- Sentiasa gunakan tanda petik untuk mengelakkan masalah dengan ruang atau karakter khas dalam teks yang ingin dicetak.