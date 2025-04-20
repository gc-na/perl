# [Sistem Operasi] C Shell (csh) gunzip: Mengurangkan saiz fail

## Overview
Perintah `gunzip` digunakan untuk mengurangkan saiz fail yang telah dimampatkan menggunakan algoritma gzip. Ia mengembalikan fail kepada bentuk asalnya, membolehkan pengguna mengakses data yang telah dimampatkan.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `gunzip`:

```
gunzip [options] [arguments]
```

## Common Options
- `-c`: Mengeluarkan hasil ke standard output tanpa mengubah fail asal.
- `-f`: Memaksa penggantian fail yang sedia ada.
- `-k`: Menyimpan fail asal semasa mengurangkan saiz fail.
- `-r`: Mengurangkan saiz semua fail dalam direktori secara rekursif.

## Common Examples
Berikut adalah beberapa contoh penggunaan `gunzip`:

1. Mengurangkan saiz fail tunggal:
   ```csh
   gunzip fail.txt.gz
   ```

2. Mengeluarkan hasil ke standard output:
   ```csh
   gunzip -c fail.txt.gz > fail.txt
   ```

3. Memaksa penggantian fail yang sedia ada:
   ```csh
   gunzip -f fail.txt.gz
   ```

4. Menyimpan fail asal semasa mengurangkan saiz:
   ```csh
   gunzip -k fail.txt.gz
   ```

5. Mengurangkan saiz semua fail dalam direktori:
   ```csh
   gunzip -r direktori/
   ```

## Tips
- Sentiasa semak ruang simpanan sebelum menggunakan `gunzip`, kerana proses ini memerlukan ruang tambahan untuk fail yang tidak dimampatkan.
- Gunakan pilihan `-k` jika anda ingin mengekalkan fail asal sebagai sandaran.
- Untuk mengelakkan kehilangan data, pastikan anda mempunyai salinan fail penting sebelum menggunakan pilihan `-f`.