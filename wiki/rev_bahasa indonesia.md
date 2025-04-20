# [Linux] C Shell (csh) rev: Membalikkan teks

## Overview
Perintah `rev` digunakan untuk membalikkan urutan karakter dalam setiap baris teks dari input yang diberikan. Ini berguna dalam berbagai situasi, seperti ketika Anda perlu memanipulasi string atau melakukan pengolahan teks.

## Usage
Berikut adalah sintaks dasar dari perintah `rev`:

```
rev [options] [arguments]
```

## Common Options
- `-` : Membaca dari input standar (stdin) jika tidak ada argumen yang diberikan.
- `-o <file>` : Menyimpan output ke file yang ditentukan.

## Common Examples

1. **Membalikkan teks dari input standar:**
   ```bash
   echo "Hello World" | rev
   ```
   Output:
   ```
   dlroW olleH
   ```

2. **Membalikkan isi file:**
   ```bash
   rev myfile.txt
   ```

3. **Menyimpan hasil balik ke file baru:**
   ```bash
   rev myfile.txt -o reversed.txt
   ```

4. **Membalikkan beberapa baris teks:**
   ```bash
   printf "Line 1\nLine 2\n" | rev
   ```
   Output:
   ```
   1 eniL
   2 eniL
   ```

## Tips
- Gunakan `rev` dalam kombinasi dengan perintah lain menggunakan pipe (`|`) untuk memproses output secara lebih efisien.
- Pastikan untuk memeriksa hasil output jika Anda menggunakan opsi `-o` untuk memastikan data tersimpan dengan benar.