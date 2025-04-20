# [Sistem Operasi] C Shell (csh) awk Penggunaan: Memproses dan menganalisis teks

## Overview
Perintah `awk` adalah alat yang kuat untuk memproses dan menganalisis teks. Ia digunakan untuk membaca dan memanipulasi data dalam format teks, seperti fail teks dan output dari perintah lain. `awk` membolehkan pengguna untuk melakukan operasi seperti pencarian, penggantian, dan pengiraan dengan mudah.

## Usage
Sintaks asas untuk menggunakan `awk` adalah seperti berikut:

```csh
awk [options] [arguments]
```

## Common Options
Beberapa pilihan umum untuk `awk` termasuk:

- `-F`: Menetapkan pemisah medan (field separator) yang digunakan untuk memisahkan data.
- `-v`: Menggunakan pembolehubah untuk menyimpan nilai yang boleh digunakan dalam skrip `awk`.
- `-f`: Menggunakan fail untuk menyimpan skrip `awk` yang lebih kompleks.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `awk`:

1. **Mencetak medan tertentu dari fail:**
   ```csh
   awk '{print $1}' fail.txt
   ```
   Contoh ini mencetak medan pertama dari setiap baris dalam `fail.txt`.

2. **Menggunakan pemisah medan:**
   ```csh
   awk -F, '{print $2}' fail.csv
   ```
   Dalam contoh ini, `awk` menggunakan koma sebagai pemisah medan dan mencetak medan kedua dari setiap baris dalam `fail.csv`.

3. **Menghitung jumlah baris dalam fail:**
   ```csh
   awk 'END {print NR}' fail.txt
   ```
   Ini mencetak jumlah keseluruhan baris dalam `fail.txt`.

4. **Menapis baris berdasarkan syarat:**
   ```csh
   awk '$3 > 50 {print $1, $2}' fail.txt
   ```
   Dalam contoh ini, `awk` mencetak medan pertama dan kedua dari baris di mana medan ketiga lebih besar daripada 50.

## Tips
- Gunakan pemisah medan yang sesuai untuk data anda agar `awk` dapat memproses dengan tepat.
- Simpan skrip `awk` yang lebih kompleks dalam fail dan gunakan pilihan `-f` untuk menjalankannya.
- Manfaatkan pembolehubah dengan pilihan `-v` untuk meningkatkan fleksibiliti skrip anda.