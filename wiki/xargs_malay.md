# [Sistem Operasi] C Shell (csh) xargs Penggunaan: Mengendalikan argumen dari input standard

## Overview
Perintah `xargs` digunakan untuk membina dan melaksanakan perintah berdasarkan input yang diterima dari standard input. Ia membolehkan pengguna menghantar argumen ke perintah lain, menjadikannya berguna untuk memproses output dari perintah lain.

## Usage
Sintaks asas untuk menggunakan `xargs` adalah seperti berikut:

```csh
xargs [options] [arguments]
```

## Common Options
- `-n N`: Menghadkan bilangan argumen yang dihantar kepada perintah yang dipanggil kepada N.
- `-d DELIM`: Menetapkan pemisah input kepada DELIM yang ditentukan.
- `-0`: Menganggap input sebagai rentetan null-terminated, berguna untuk fail dengan ruang dalam nama.
- `-p`: Meminta pengesahan sebelum melaksanakan setiap perintah.
- `-I {}`: Menggantikan `{}` dalam perintah dengan argumen yang diterima.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `xargs`:

1. Menghapus semua fail yang dipadankan oleh perintah `find`:

   ```csh
   find . -name "*.tmp" | xargs rm
   ```

2. Menghitung bilangan baris dalam fail yang dipadankan:

   ```csh
   ls *.txt | xargs wc -l
   ```

3. Menggunakan pemisah khusus untuk memproses fail:

   ```csh
   echo "file1.txt,file2.txt,file3.txt" | xargs -d ',' cp {} /destination/
   ```

4. Mengganti nama fail dengan menambah awalan:

   ```csh
   ls *.jpg | xargs -I {} mv {} new_{}
   ```

## Tips
- Sentiasa semak output sebelum melaksanakan perintah yang mengubah fail, terutamanya dengan `rm`.
- Gunakan `-n` untuk mengelakkan masalah dengan perintah yang mempunyai had argumen.
- Jika anda bekerja dengan nama fail yang mungkin mengandungi ruang, pertimbangkan untuk menggunakan `-0` bersama dengan `find` yang menggunakan `-print0`.