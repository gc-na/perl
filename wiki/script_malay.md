# [Sistem Operasi] C Shell (csh) skrip Penggunaan: Merekod sesi terminal

## Overview
Perintah `script` dalam C Shell (csh) digunakan untuk merekod sesi terminal ke dalam fail. Ia membolehkan pengguna menyimpan semua output yang dihasilkan semasa sesi terminal untuk rujukan masa depan.

## Usage
Berikut adalah sintaks asas untuk perintah `script`:

```
script [options] [arguments]
```

## Common Options
- `-a`: Menambah output ke dalam fail yang sedia ada, bukannya menimpa.
- `-f`: Menulis output ke fail secara langsung, tanpa menunggu buffer penuh.
- `-q`: Menjalankan perintah tanpa mencetak mesej permulaan dan akhir.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `script`:

1. **Merekod sesi terminal ke dalam fail:**
   ```csh
   script sesi.txt
   ```
   Ini akan mula merekod sesi terminal ke dalam fail `sesi.txt`.

2. **Merekod sesi dan menambah ke fail sedia ada:**
   ```csh
   script -a sesi_lama.txt
   ```
   Ini akan menambah output sesi ke dalam fail `sesi_lama.txt`.

3. **Merekod sesi dengan output langsung:**
   ```csh
   script -f sesi_segera.txt
   ```
   Ini akan merekod sesi ke dalam fail `sesi_segera.txt` dengan output ditulis secara langsung.

4. **Menjalankan perintah tanpa mesej awal dan akhir:**
   ```csh
   script -q sesi_senyap.txt
   ```
   Ini akan merekod sesi ke dalam `sesi_senyap.txt` tanpa mesej permulaan dan akhir.

## Tips
- Sentiasa semak fail output selepas sesi untuk memastikan semua maklumat yang diperlukan telah direkod.
- Gunakan pilihan `-a` jika anda ingin menambah output ke dalam fail yang sudah ada, untuk mengelakkan kehilangan data.
- Pertimbangkan untuk menggunakan pilihan `-f` jika anda bekerja dengan output yang besar dan ingin melihat hasilnya secara langsung.