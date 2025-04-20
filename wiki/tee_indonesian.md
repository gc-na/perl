# [Sistem Operasi] C Shell (csh) tee Penggunaan: Menyalin dan Menampilkan Output

## Overview
Perintah `tee` dalam C Shell (csh) digunakan untuk membaca dari input standar dan menulis ke output standar serta satu atau lebih file. Dengan kata lain, `tee` memungkinkan pengguna untuk melihat output dari suatu perintah sambil juga menyimpannya ke dalam file.

## Usage
Sintaks dasar dari perintah `tee` adalah sebagai berikut:

```
tee [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `tee`:

- `-a` : Menambahkan output ke akhir file yang sudah ada, bukan menimpanya.
- `-i` : Mengabaikan sinyal interrupt (SIGINT).

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan perintah `tee`:

1. Menyimpan output perintah ke dalam file:
   ```csh
   ls -l | tee daftar_file.txt
   ```

2. Menyimpan output dan menampilkannya di layar sekaligus:
   ```csh
   echo "Hello, World!" | tee output.txt
   ```

3. Menambahkan output ke file yang sudah ada:
   ```csh
   echo "Baris baru" | tee -a output.txt
   ```

4. Menggunakan `tee` dengan beberapa file:
   ```csh
   echo "Data penting" | tee file1.txt file2.txt
   ```

## Tips
- Gunakan opsi `-a` jika Anda ingin menambahkan data ke file yang sudah ada, agar tidak kehilangan informasi sebelumnya.
- Kombinasikan `tee` dengan perintah lain menggunakan pipe (`|`) untuk mengalirkan output dengan lebih fleksibel.
- Pastikan Anda memiliki izin yang tepat untuk menulis ke file yang dituju agar tidak terjadi kesalahan saat menggunakan `tee`.