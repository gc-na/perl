# [Sistem Operasi] C Shell (csh) diff Penggunaan: Membandingkan file

## Overview
Perintah `diff` digunakan untuk membandingkan dua file teks dan menampilkan perbedaan di antara keduanya. Ini sangat berguna untuk melihat perubahan yang telah dilakukan pada file atau untuk membandingkan versi yang berbeda dari dokumen.

## Usage
Berikut adalah sintaks dasar dari perintah `diff`:

```csh
diff [options] [file1] [file2]
```

## Common Options
- `-u`: Menampilkan perbedaan dalam format unified, yang lebih mudah dibaca.
- `-c`: Menampilkan perbedaan dalam format context, memberikan lebih banyak konteks di sekitar perubahan.
- `-i`: Mengabaikan perbedaan dalam huruf besar/kecil.
- `-w`: Mengabaikan semua spasi putih dalam perbandingan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `diff`:

1. Membandingkan dua file teks sederhana:
   ```csh
   diff file1.txt file2.txt
   ```

2. Menggunakan opsi unified untuk tampilan yang lebih jelas:
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
- Selalu gunakan opsi `-u` untuk hasil yang lebih mudah dibaca saat membandingkan file.
- Jika Anda bekerja dengan banyak file, pertimbangkan untuk menggunakan `diff -r` untuk membandingkan direktori secara rekursif.
- Simpan hasil perbandingan ke dalam file dengan menggunakan redirection, misalnya: `diff file1.txt file2.txt > hasil.txt`.