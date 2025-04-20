# [Linux] C Shell (csh) diff <Perbandingan fail>: Membandingkan kandungan fail

## Overview
Perintah `diff` digunakan untuk membandingkan kandungan dua fail teks dan menunjukkan perbezaan antara mereka. Ia sangat berguna untuk pengaturcara dan penulis dokumen yang ingin melihat perubahan yang telah dibuat pada fail.

## Usage
Sintaks asas untuk perintah `diff` adalah seperti berikut:

```csh
diff [options] [arguments]
```

## Common Options
- `-u`: Menunjukkan perbezaan dalam format "unified", yang lebih mudah dibaca.
- `-c`: Menunjukkan perbezaan dalam format "context", memberikan lebih banyak konteks di sekeliling perbezaan.
- `-i`: Mengabaikan perbezaan dalam huruf besar dan kecil.
- `-w`: Mengabaikan ruang kosong semasa perbandingan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `diff`:

1. **Membandingkan dua fail:**
   ```csh
   diff fail1.txt fail2.txt
   ```

2. **Membandingkan dua fail dengan format unified:**
   ```csh
   diff -u fail1.txt fail2.txt
   ```

3. **Membandingkan dua fail dan mengabaikan huruf besar dan kecil:**
   ```csh
   diff -i fail1.txt fail2.txt
   ```

4. **Membandingkan dua fail dengan mengabaikan ruang kosong:**
   ```csh
   diff -w fail1.txt fail2.txt
   ```

## Tips
- Sentiasa gunakan pilihan `-u` untuk mendapatkan output yang lebih mudah dibaca.
- Jika anda bekerja dengan fail yang besar, pertimbangkan untuk menggunakan `diff` bersama dengan `less` untuk meneliti hasilnya dengan lebih mudah:
  ```csh
  diff -u fail1.txt fail2.txt | less
  ```
- Untuk menyimpan hasil perbandingan ke dalam fail, anda boleh menggunakan pengalihan output:
  ```csh
  diff fail1.txt fail2.txt > perbandingan.txt
  ```