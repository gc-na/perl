# [Sistem Operasi] C Shell (csh) expr Penggunaan: Menghitung dan Memanipulasi Ekspresi

## Overview
Perintah `expr` dalam C Shell (csh) digunakan untuk mengevaluasi ekspresi aritmatika, logika, dan string. Ini sangat berguna untuk melakukan perhitungan sederhana dan manipulasi string dalam skrip shell.

## Usage
Berikut adalah sintaks dasar dari perintah `expr`:

```csh
expr [options] [arguments]
```

## Common Options
- `+` : Menjumlahkan dua angka.
- `-` : Mengurangi angka kedua dari angka pertama.
- `*` : Mengalikan dua angka.
- `/` : Membagi angka pertama dengan angka kedua.
- `%` : Menghitung sisa dari pembagian dua angka.
- `=` : Membandingkan dua nilai untuk kesetaraan.
- `!=` : Membandingkan dua nilai untuk ketidaksetaraan.

## Common Examples
Berikut adalah beberapa contoh penggunaan `expr`:

1. **Menjumlahkan dua angka:**
   ```csh
   expr 5 + 3
   ```
   Output: `8`

2. **Mengurangi angka:**
   ```csh
   expr 10 - 4
   ```
   Output: `6`

3. **Mengalikan dua angka:**
   ```csh
   expr 7 \* 6
   ```
   Output: `42`

4. **Membagi angka:**
   ```csh
   expr 20 / 4
   ```
   Output: `5`

5. **Menghitung sisa pembagian:**
   ```csh
   expr 10 % 3
   ```
   Output: `1`

6. **Membandingkan dua nilai:**
   ```csh
   expr 5 = 5
   ```
   Output: `1` (true)

7. **Membandingkan untuk ketidaksetaraan:**
   ```csh
   expr 5 != 3
   ```
   Output: `1` (true)

## Tips
- Selalu gunakan tanda backslash (`\`) sebelum tanda bintang (`*`) untuk menghindari kesalahan dalam interpretasi shell.
- Gunakan `expr` dalam skrip untuk membuat perhitungan dinamis berdasarkan input pengguna.
- Ingat bahwa `expr` hanya dapat menangani bilangan bulat, jadi untuk perhitungan pecahan, pertimbangkan menggunakan bahasa pemrograman lain atau alat yang lebih canggih.