# [Sistem Operasi] C Shell (csh) nl: Menampilkan nomor baris pada file teks

## Overview
Perintah `nl` digunakan untuk menambahkan nomor baris pada file teks. Ini sangat berguna untuk memudahkan referensi dan navigasi dalam dokumen yang panjang.

## Usage
Berikut adalah sintaks dasar dari perintah `nl`:

```csh
nl [options] [arguments]
```

## Common Options
- `-b` : Menentukan cara penomoran baris. Misalnya, `-b a` untuk menomori semua baris.
- `-f` : Mengatur penomoran baris untuk setiap file baru.
- `-h` : Menentukan header yang akan ditampilkan sebelum nomor baris.
- `-n` : Mengatur format nomor baris. Misalnya, `-n ln` untuk menampilkan nomor baris dalam format left justified.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `nl`:

1. Menampilkan nomor baris pada file teks:
   ```csh
   nl file.txt
   ```

2. Menomori semua baris dalam file:
   ```csh
   nl -b a file.txt
   ```

3. Menggunakan format nomor baris yang berbeda:
   ```csh
   nl -n rn file.txt
   ```

4. Menampilkan nomor baris dengan header:
   ```csh
   nl -h "Header:" file.txt
   ```

## Tips
- Gunakan opsi `-b` untuk menyesuaikan penomoran baris sesuai kebutuhan dokumen Anda.
- Cobalah menggabungkan beberapa opsi untuk mendapatkan hasil yang diinginkan.
- Selalu periksa hasil output untuk memastikan nomor baris ditampilkan dengan benar.