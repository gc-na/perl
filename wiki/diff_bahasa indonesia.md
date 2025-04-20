# [Sistem Operasi] C Shell (csh) diff Penggunaan: Membandingkan file teks

## Overview
Perintah `diff` digunakan untuk membandingkan dua file teks dan menampilkan perbedaan di antara keduanya. Ini sangat berguna untuk melihat perubahan yang dilakukan pada file, terutama dalam pengembangan perangkat lunak atau saat mengelola dokumen.

## Usage
Berikut adalah sintaks dasar untuk menggunakan perintah `diff`:

```csh
diff [options] [file1] [file2]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `diff`:

- `-u`: Menampilkan perbedaan dalam format unified, yang lebih mudah dibaca.
- `-c`: Menampilkan perbedaan dalam format context, memberikan konteks lebih banyak di sekitar perubahan.
- `-i`: Mengabaikan perbedaan dalam huruf besar/kecil.
- `-w`: Mengabaikan semua spasi putih saat membandingkan.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan perintah `diff`:

1. Membandingkan dua file teks sederhana:
   ```csh
   diff file1.txt file2.txt
   ```

2. Menampilkan perbedaan dalam format unified:
   ```csh
   diff -u file1.txt file2.txt
   ```

3. Mengabaikan perbedaan huruf besar/kecil:
   ```csh
   diff -i file1.txt file2.txt
   ```

4. Menampilkan perbedaan dengan konteks:
   ```csh
   diff -c file1.txt file2.txt
   ```

## Tips
- Selalu gunakan opsi `-u` untuk output yang lebih bersih dan mudah dibaca.
- Jika Anda bekerja dengan banyak file, pertimbangkan untuk menggunakan `diff` dalam kombinasi dengan perintah lain seperti `find` untuk membandingkan file dalam direktori.
- Simpan hasil perbandingan ke dalam file dengan menggunakan redirection:
  ```csh
  diff file1.txt file2.txt > hasil_diff.txt
  ```