# [Sistem Operasi] C Shell (csh) uniq Penggunaan: Menghapus baris duplikat dari file

## Overview
Perintah `uniq` dalam C Shell (csh) digunakan untuk menghapus baris yang duplikat dari file atau output. Perintah ini sangat berguna ketika Anda ingin menampilkan hanya satu salinan dari setiap baris yang sama.

## Usage
Berikut adalah sintaks dasar dari perintah `uniq`:

```bash
uniq [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `uniq`:

- `-c`: Menghitung jumlah kemunculan setiap baris.
- `-d`: Menampilkan hanya baris yang muncul lebih dari sekali.
- `-u`: Menampilkan hanya baris yang unik, yaitu yang muncul sekali.
- `-i`: Mengabaikan perbedaan huruf besar dan kecil saat membandingkan baris.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan perintah `uniq`:

1. Menghapus baris duplikat dari file:
   ```bash
   uniq file.txt
   ```

2. Menghitung jumlah kemunculan setiap baris:
   ```bash
   uniq -c file.txt
   ```

3. Menampilkan hanya baris yang muncul lebih dari sekali:
   ```bash
   uniq -d file.txt
   ```

4. Menampilkan hanya baris yang unik:
   ```bash
   uniq -u file.txt
   ```

5. Mengabaikan perbedaan huruf besar dan kecil:
   ```bash
   uniq -i file.txt
   ```

## Tips
- Pastikan untuk mengurutkan file sebelum menggunakan `uniq`, karena `uniq` hanya menghapus duplikat yang berurutan. Anda dapat menggunakan perintah `sort` untuk mengurutkan file terlebih dahulu.
- Gunakan opsi `-c` untuk mendapatkan informasi lebih lanjut tentang seberapa sering setiap baris muncul, yang bisa sangat membantu dalam analisis data.
- Kombinasikan `uniq` dengan perintah lain menggunakan pipe (`|`) untuk memproses output dari perintah sebelumnya, seperti `sort` dan `grep`.