# [Linux] C Shell (csh) cmp Penggunaan: Membandingkan dua fail

## Overview
Perintah `cmp` dalam C Shell (csh) digunakan untuk membandingkan dua fail dan menunjukkan perbezaan antara mereka. Ia berguna untuk mengesan perubahan dalam fail teks atau binari.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `cmp`:

```
cmp [options] [arguments]
```

## Common Options
- `-l`: Menunjukkan byte yang berbeza dalam format octal.
- `-s`: Tidak menghasilkan output, hanya mengembalikan status keluar.
- `-i`: Menentukan byte yang ingin dibandingkan dari permulaan fail.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `cmp`:

1. **Membandingkan dua fail:**
   ```csh
   cmp fail1.txt fail2.txt
   ```

2. **Menggunakan pilihan -s untuk menyemak sama ada fail adalah sama tanpa output:**
   ```csh
   cmp -s fail1.txt fail2.txt
   ```

3. **Menunjukkan perbezaan dalam format octal:**
   ```csh
   cmp -l fail1.bin fail2.bin
   ```

4. **Membandingkan dari byte tertentu:**
   ```csh
   cmp -i 10 fail1.txt fail2.txt
   ```

## Tips
- Gunakan pilihan `-s` jika anda hanya ingin tahu sama ada fail adalah sama tanpa melihat perbezaan.
- Untuk fail binari, pilihan `-l` memberikan maklumat yang lebih terperinci tentang perbezaan.
- Sentiasa semak status keluar perintah untuk menentukan sama ada fail adalah sama (status 0) atau berbeza (status 1).