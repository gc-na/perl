# [Sistem Operasi] C Shell (csh) uniq Penggunaan: Menghapus baris duplikat

## Overview
Perintah `uniq` dalam C Shell (csh) digunakan untuk menghapus baris yang duplikat dari file atau output. Perintah ini sangat berguna ketika Anda ingin mendapatkan daftar unik dari data yang mungkin memiliki entri yang sama.

## Usage
Sintaks dasar dari perintah `uniq` adalah sebagai berikut:

```
uniq [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `uniq`:

- `-c`: Menghitung jumlah kemunculan setiap baris unik.
- `-d`: Menampilkan hanya baris yang muncul lebih dari sekali.
- `-u`: Menampilkan hanya baris yang unik (tidak muncul lebih dari sekali).
- `-i`: Mengabaikan perbedaan antara huruf besar dan kecil saat membandingkan baris.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan perintah `uniq`:

1. Menghapus baris duplikat dari file:
   ```csh
   uniq file.txt
   ```

2. Menghitung jumlah kemunculan setiap baris unik:
   ```csh
   uniq -c file.txt
   ```

3. Menampilkan hanya baris yang muncul lebih dari sekali:
   ```csh
   uniq -d file.txt
   ```

4. Menampilkan hanya baris yang unik:
   ```csh
   uniq -u file.txt
   ```

5. Mengabaikan perbedaan huruf besar dan kecil:
   ```csh
   uniq -i file.txt
   ```

## Tips
- Pastikan untuk mengurutkan file sebelum menggunakan `uniq`, karena perintah ini hanya menghapus duplikat yang berurutan.
- Anda dapat menggabungkan `uniq` dengan perintah lain seperti `sort` untuk mendapatkan hasil yang lebih baik. Contoh:
  ```csh
  sort file.txt | uniq
  ```
- Gunakan opsi `-c` untuk mendapatkan informasi lebih lanjut tentang seberapa sering setiap baris muncul, yang dapat membantu dalam analisis data.