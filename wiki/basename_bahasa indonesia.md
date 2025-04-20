# [Sistem Operasi] C Shell (csh) basename Penggunaan: Menghapus jalur dari nama file

## Overview
Perintah `basename` dalam C Shell digunakan untuk menghapus jalur direktori dari nama file, sehingga hanya menyisakan nama file itu sendiri. Ini berguna ketika Anda ingin mendapatkan nama file tanpa informasi jalur yang menyertainya.

## Usage
Berikut adalah sintaks dasar dari perintah `basename`:

```
basename [options] [arguments]
```

## Common Options
- `-a`: Menghapus semua jalur dari setiap argumen yang diberikan dan mengembalikan nama file.
- `-s`: Menghapus sufiks tertentu dari nama file.
- `-z`: Mengabaikan argumen kosong.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `basename`:

1. Mengambil nama file dari jalur lengkap:
   ```csh
   basename /home/user/document.txt
   ```
   Output: `document.txt`

2. Menghapus sufiks dari nama file:
   ```csh
   basename /home/user/document.txt .txt
   ```
   Output: `document`

3. Menggunakan opsi `-a` untuk menghapus jalur dari beberapa file:
   ```csh
   basename -a /home/user/file1.txt /home/user/file2.txt
   ```
   Output:
   ```
   file1.txt
   file2.txt
   ```

4. Mengabaikan argumen kosong:
   ```csh
   basename -z ""
   ```
   Output: (tidak ada output)

## Tips
- Gunakan `basename` dalam skrip untuk memproses nama file secara otomatis.
- Kombinasikan `basename` dengan perintah lain untuk mengelola file dengan lebih efisien.
- Selalu periksa apakah jalur yang diberikan valid untuk menghindari hasil yang tidak diinginkan.