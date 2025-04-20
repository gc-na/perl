# [Sistem Operasi] C Shell (csh) expr Penggunaan: Menghitung ekspresi

## Overview
Perintah `expr` dalam C Shell (csh) digunakan untuk mengevaluasi ekspresi aritmatika, string, dan logika. Ini memungkinkan pengguna untuk melakukan operasi dasar seperti penjumlahan, pengurangan, dan perbandingan.

## Usage
Sintaks dasar dari perintah `expr` adalah sebagai berikut:

```
expr [options] [arguments]
```

## Common Options
- `+` : Menjumlahkan dua angka.
- `-` : Mengurangi angka kedua dari angka pertama.
- `*` : Mengalikan dua angka.
- `/` : Membagi angka pertama dengan angka kedua.
- `%` : Menghitung sisa dari pembagian dua angka.
- `=` : Membandingkan dua nilai untuk kesamaan.
- `!=` : Membandingkan dua nilai untuk ketidaksamaan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `expr`:

1. **Penjumlahan dua angka:**
   ```csh
   expr 5 + 3
   ```
   Output: `8`

2. **Pengurangan dua angka:**
   ```csh
   expr 10 - 4
   ```
   Output: `6`

3. **Perkalian dua angka:**
   ```csh
   expr 7 \* 6
   ```
   Output: `42`

4. **Pembagian dua angka:**
   ```csh
   expr 20 / 4
   ```
   Output: `5`

5. **Menghitung sisa dari pembagian:**
   ```csh
   expr 10 % 3
   ```
   Output: `1`

6. **Perbandingan kesamaan:**
   ```csh
   expr 5 = 5
   ```
   Output: `1` (true)

7. **Perbandingan ketidaksamaan:**
   ```csh
   expr 5 != 3
   ```
   Output: `1` (true)

## Tips
- Pastikan untuk menggunakan karakter escape (`\`) sebelum tanda `*` untuk menghindari konflik dengan shell.
- Gunakan tanda kurung untuk mengelompokkan ekspresi yang lebih kompleks agar hasilnya sesuai dengan yang diharapkan.
- `expr` hanya dapat digunakan untuk operasi dasar; untuk operasi yang lebih kompleks, pertimbangkan menggunakan bahasa pemrograman lain atau alat yang lebih kuat.