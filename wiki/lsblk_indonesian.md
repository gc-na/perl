# [Linux] C Shell (csh) lsblk Penggunaan: Menampilkan informasi tentang perangkat blok

## Overview
Perintah `lsblk` digunakan untuk menampilkan informasi tentang perangkat blok di sistem Linux. Ini termasuk disk, partisi, dan perangkat penyimpanan lainnya. Dengan `lsblk`, pengguna dapat melihat struktur perangkat penyimpanan dan bagaimana mereka terhubung.

## Usage
Sintaks dasar dari perintah `lsblk` adalah sebagai berikut:

```
lsblk [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `lsblk`:

- `-a` : Menampilkan semua perangkat, termasuk yang tidak terpasang.
- `-f` : Menampilkan informasi sistem file.
- `-l` : Menampilkan output dalam format daftar.
- `-o` : Menentukan kolom yang ingin ditampilkan.
- `-p` : Menampilkan nama perangkat lengkap.

## Common Examples
Berikut adalah beberapa contoh penggunaan `lsblk`:

1. Menampilkan semua perangkat blok:
   ```bash
   lsblk
   ```

2. Menampilkan semua perangkat termasuk yang tidak terpasang:
   ```bash
   lsblk -a
   ```

3. Menampilkan informasi sistem file untuk setiap perangkat:
   ```bash
   lsblk -f
   ```

4. Menampilkan output dalam format daftar:
   ```bash
   lsblk -l
   ```

5. Menampilkan kolom tertentu, misalnya nama dan ukuran:
   ```bash
   lsblk -o NAME,SIZE
   ```

## Tips
- Gunakan opsi `-f` untuk mendapatkan informasi tambahan tentang sistem file, seperti tipe dan label.
- Untuk melihat perangkat yang terpasang dan informasi lebih detail, pertimbangkan untuk menggunakan `lsblk -o +MOUNTPOINT`.
- Jika Anda ingin menyimpan output ke dalam file, Anda dapat menggunakan pengalihan output, misalnya:
  ```bash
  lsblk > daftar_perangkat.txt
  ```