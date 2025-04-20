# [Sistem Operasi] C Shell (csh) dirname Penggunaan: Mengambil nama direktori dari jalan fail

## Overview
Perintah `dirname` digunakan untuk mendapatkan nama direktori dari jalan fail yang diberikan. Ia mengeluarkan bahagian direktori dari jalan fail, membuang nama fail itu sendiri.

## Usage
Sintaks asas bagi perintah `dirname` adalah seperti berikut:

```
dirname [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `dirname` beserta penjelasan ringkas:

- `-z` : Mengeluarkan hasil dalam format null-terminated.
- `--help` : Memaparkan maklumat bantuan tentang penggunaan `dirname`.
- `--version` : Menunjukkan versi perintah `dirname`.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `dirname`:

1. Mengambil nama direktori dari jalan fail:
   ```csh
   dirname /home/user/documents/file.txt
   ```
   Output: `/home/user/documents`

2. Mengambil nama direktori dari jalan fail yang tidak lengkap:
   ```csh
   dirname ./file.txt
   ```
   Output: `.`

3. Mengambil nama direktori dari jalan fail yang mengandungi spasi:
   ```csh
   dirname "/home/user/My Documents/file.txt"
   ```
   Output: `/home/user/My Documents`

## Tips
- Pastikan untuk menggunakan petikan jika jalan fail mengandungi spasi.
- Gunakan `dirname` dalam skrip untuk memudahkan pengendalian fail dan direktori.
- Gabungkan `dirname` dengan perintah lain seperti `find` untuk memproses banyak fail sekaligus.