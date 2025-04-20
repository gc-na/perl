# [Sistem Operasi] C Shell (csh) sha256sum: Menghitung checksum SHA-256

## Overview
Perintah `sha256sum` digunakan untuk menghitung dan memverifikasi checksum SHA-256 dari file. Ini berguna untuk memastikan integritas data dengan membandingkan checksum yang dihasilkan dengan checksum yang diketahui.

## Usage
Sintaks dasar dari perintah ini adalah sebagai berikut:
```
sha256sum [options] [arguments]
```

## Common Options
- `-b`: Menghitung checksum untuk file biner.
- `-c`: Memeriksa checksum dari file yang diberikan.
- `-h`: Menampilkan bantuan tentang penggunaan perintah.
- `--quiet`: Menonaktifkan output yang tidak perlu.

## Common Examples
Berikut adalah beberapa contoh penggunaan `sha256sum`:

1. Menghitung checksum SHA-256 dari sebuah file:
   ```bash
   sha256sum file.txt
   ```

2. Menyimpan checksum ke dalam file:
   ```bash
   sha256sum file.txt > checksum.txt
   ```

3. Memeriksa checksum dari file menggunakan file checksum:
   ```bash
   sha256sum -c checksum.txt
   ```

4. Menghitung checksum untuk file biner:
   ```bash
   sha256sum -b file.bin
   ```

## Tips
- Selalu simpan checksum yang dihasilkan dalam file terpisah untuk memudahkan verifikasi di masa mendatang.
- Gunakan opsi `-c` untuk memeriksa banyak file sekaligus dengan satu perintah.
- Pastikan untuk menggunakan `sha256sum` pada file yang tidak sedang digunakan untuk menghindari hasil yang tidak akurat.