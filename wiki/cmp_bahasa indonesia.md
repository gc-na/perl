# [Sistem Operasi] C Shell (csh) cmp Penggunaan: Membandingkan file biner

## Overview
Perintah `cmp` digunakan untuk membandingkan dua file biner dan menentukan apakah mereka identik atau tidak. Jika file berbeda, `cmp` akan menunjukkan lokasi pertama di mana perbedaan terjadi.

## Usage
Berikut adalah sintaks dasar dari perintah `cmp`:

```bash
cmp [options] [arguments]
```

## Common Options
- `-l`: Menampilkan byte yang berbeda dalam format oktal.
- `-s`: Menyembunyikan output dan hanya mengembalikan status keluar.
- `-i OFFSET`: Mengabaikan sejumlah byte dari awal file.
- `-n N`: Hanya membandingkan N byte pertama dari file.

## Common Examples
Berikut adalah beberapa contoh penggunaan `cmp`:

1. Membandingkan dua file:
   ```bash
   cmp file1.bin file2.bin
   ```

2. Menggunakan opsi `-s` untuk hanya mendapatkan status keluar:
   ```bash
   cmp -s file1.bin file2.bin
   ```

3. Menampilkan byte yang berbeda dalam format oktal:
   ```bash
   cmp -l file1.bin file2.bin
   ```

4. Mengabaikan beberapa byte dari awal file:
   ```bash
   cmp -i 10 file1.bin file2.bin
   ```

5. Membandingkan hanya N byte pertama dari file:
   ```bash
   cmp -n 100 file1.bin file2.bin
   ```

## Tips
- Gunakan opsi `-s` jika Anda hanya ingin mengetahui apakah file berbeda tanpa melihat detailnya.
- Opsi `-l` sangat berguna untuk debugging ketika Anda perlu mengetahui perbedaan spesifik antara file.
- Pastikan untuk memeriksa status keluar dari `cmp` untuk menentukan apakah file identik (status 0) atau berbeda (status 1).