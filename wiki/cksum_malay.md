# [Sistem Pengendalian] C Shell (csh) cksum: Mengira checksum fail

## Overview
Perintah `cksum` dalam C Shell (csh) digunakan untuk mengira dan memaparkan checksum (nilai hash) bagi fail. Nilai ini berguna untuk memeriksa integriti fail dan memastikan bahawa fail tidak telah diubah atau rosak.

## Usage
Sintaks asas untuk menggunakan perintah `cksum` adalah seperti berikut:

```
cksum [options] [arguments]
```

## Common Options
- `-a` : Menentukan algoritma checksum yang digunakan.
- `-b` : Mengira checksum bagi fail binari.
- `-h` : Menunjukkan maklumat bantuan tentang perintah ini.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `cksum`:

1. Mengira checksum bagi satu fail:
   ```csh
   cksum fail.txt
   ```

2. Mengira checksum bagi beberapa fail sekaligus:
   ```csh
   cksum fail1.txt fail2.txt
   ```

3. Mengira checksum bagi fail binari:
   ```csh
   cksum -b fail.bin
   ```

4. Menggunakan pilihan bantuan untuk mendapatkan maklumat lanjut:
   ```csh
   cksum -h
   ```

## Tips
- Sentiasa semak checksum fail selepas memindahkan atau menyalin untuk memastikan integriti data.
- Gunakan `cksum` berserta skrip lain untuk automasi proses pemeriksaan fail.
- Simpan nilai checksum dalam fail berasingan untuk rujukan masa depan.