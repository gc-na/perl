# [Sistem Operasi] C Shell (csh) pwd: Menampilkan direktori kerja saat ini

## Overview
Perintah `pwd` (print working directory) digunakan dalam C Shell untuk menampilkan jalur direktori kerja saat ini. Ini sangat berguna untuk mengetahui di mana Anda berada dalam sistem file.

## Usage
Sintaks dasar dari perintah `pwd` adalah sebagai berikut:

```
pwd [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `pwd`:

- `-L`: Menampilkan jalur direktori logis, mengikuti symlink.
- `-P`: Menampilkan jalur direktori fisik, tanpa mengikuti symlink.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `pwd`:

1. Menampilkan jalur direktori kerja saat ini:
   ```csh
   pwd
   ```

2. Menampilkan jalur direktori fisik:
   ```csh
   pwd -P
   ```

3. Menampilkan jalur direktori logis:
   ```csh
   pwd -L
   ```

## Tips
- Gunakan `pwd` secara berkala untuk memastikan Anda berada di direktori yang tepat sebelum menjalankan perintah lain.
- Jika Anda bekerja dengan symlink, pertimbangkan untuk menggunakan opsi `-P` untuk mendapatkan jalur fisik yang akurat.
- Menggabungkan `pwd` dengan perintah lain dalam skrip dapat membantu dalam debugging dan memastikan jalur yang benar digunakan.