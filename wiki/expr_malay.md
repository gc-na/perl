# [Sistem Operasi] C Shell (csh) expr Penggunaan: Mengira ekspresi

## Overview
Perintah `expr` dalam C Shell (csh) digunakan untuk mengira nilai ekspresi. Ia membolehkan pengguna melakukan operasi aritmetik, membandingkan nilai, dan memanipulasi string.

## Usage
Sintaks asas untuk menggunakan perintah `expr` adalah seperti berikut:

```csh
expr [options] [arguments]
```

## Common Options
- `+` : Menambah dua nombor.
- `-` : Mengurangkan satu nombor dari nombor lain.
- `*` : Mengalikan dua nombor.
- `/` : Membahagikan satu nombor dengan nombor lain.
- `%` : Mengira baki pembahagian.
- `=` : Membandingkan dua nilai untuk kesamaan.
- `!=` : Membandingkan dua nilai untuk ketidaksamaan.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `expr`:

1. **Menambah dua nombor:**
   ```csh
   expr 5 + 3
   ```
   Output: `8`

2. **Mengurangkan nombor:**
   ```csh
   expr 10 - 4
   ```
   Output: `6`

3. **Mengalikan nombor:**
   ```csh
   expr 7 \* 6
   ```
   Output: `42`

4. **Membahagikan nombor:**
   ```csh
   expr 20 / 4
   ```
   Output: `5`

5. **Mengira baki pembahagian:**
   ```csh
   expr 17 % 5
   ```
   Output: `2`

6. **Membandingkan dua nilai:**
   ```csh
   expr 5 = 5
   ```
   Output: `1` (benar)

7. **Membandingkan dua nilai untuk ketidaksamaan:**
   ```csh
   expr 5 != 3
   ```
   Output: `1` (benar)

## Tips
- Sentiasa gunakan `\` sebelum simbol `*` untuk mengelakkan konflik dengan pengendali shell.
- Pastikan untuk menggunakan ruang yang betul di antara argumen dan operator untuk mengelakkan ralat.
- Gunakan `expr` dalam skrip untuk melakukan pengiraan dinamik berdasarkan input pengguna.