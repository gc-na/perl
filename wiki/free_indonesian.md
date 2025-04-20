# [Sistem Operasi] C Shell (csh) free: Menampilkan informasi penggunaan memori

## Overview
Perintah `free` digunakan untuk menampilkan informasi tentang penggunaan memori di sistem. Ini memberikan gambaran tentang memori fisik dan swap yang tersedia serta yang digunakan, sehingga pengguna dapat memantau kesehatan sistem mereka.

## Usage
Sintaks dasar dari perintah `free` adalah sebagai berikut:

```csh
free [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum untuk perintah `free` beserta penjelasannya:

- `-h`: Menampilkan informasi dalam format yang lebih mudah dibaca (human-readable).
- `-m`: Menampilkan informasi dalam megabyte.
- `-g`: Menampilkan informasi dalam gigabyte.
- `-s <detik>`: Menampilkan pembaruan informasi setiap <detik> detik.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan perintah `free`:

1. Menampilkan informasi penggunaan memori dasar:
   ```csh
   free
   ```

2. Menampilkan informasi dalam format yang lebih mudah dibaca:
   ```csh
   free -h
   ```

3. Menampilkan informasi dalam megabyte:
   ```csh
   free -m
   ```

4. Menampilkan informasi setiap 5 detik:
   ```csh
   free -s 5
   ```

## Tips
- Gunakan opsi `-h` untuk mendapatkan tampilan yang lebih ramah bagi pengguna, terutama jika Anda tidak terbiasa dengan angka besar.
- Perhatikan kolom "available" pada output, yang menunjukkan berapa banyak memori yang dapat digunakan oleh aplikasi baru.
- Kombinasikan perintah `free` dengan perintah lain seperti `watch` untuk memantau penggunaan memori secara real-time.