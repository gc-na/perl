# [Linux] C Shell (csh) sed Penggunaan: Mengedit teks secara otomatis

## Overview
Perintah `sed` (stream editor) digunakan untuk mengedit teks secara otomatis dalam aliran data. Ini memungkinkan pengguna untuk melakukan berbagai operasi, seperti pencarian dan penggantian, pada teks tanpa harus membuka file secara manual.

## Usage
Berikut adalah sintaks dasar untuk menggunakan perintah `sed`:

```bash
sed [options] [arguments]
```

## Common Options
- `-e`: Menentukan ekspresi pengeditan.
- `-i`: Mengedit file secara langsung (in-place).
- `-n`: Menonaktifkan output otomatis, hanya menampilkan hasil yang ditentukan.
- `s`: Menggunakan perintah substitusi untuk mengganti teks.

## Common Examples
Berikut adalah beberapa contoh penggunaan `sed`:

1. **Mengganti teks dalam file:**
   Mengganti semua kemunculan "lama" dengan "baru" dalam file `contoh.txt`.
   ```bash
   sed -i 's/lama/baru/g' contoh.txt
   ```

2. **Menampilkan baris tertentu:**
   Menampilkan baris ke-2 hingga ke-4 dari file `contoh.txt`.
   ```bash
   sed -n '2,4p' contoh.txt
   ```

3. **Menghapus baris yang mengandung teks tertentu:**
   Menghapus semua baris yang mengandung kata "hapus" dari file `contoh.txt`.
   ```bash
   sed -i '/hapus/d' contoh.txt
   ```

4. **Menambahkan teks di akhir setiap baris:**
   Menambahkan " - selesai" di akhir setiap baris dalam file `contoh.txt`.
   ```bash
   sed -i 's/$/ - selesai/' contoh.txt
   ```

## Tips
- Selalu buat salinan file sebelum menggunakan opsi `-i` untuk menghindari kehilangan data.
- Gunakan `-n` bersama dengan perintah `p` untuk menampilkan hanya hasil yang relevan.
- Cobalah perintah `sed` di terminal sebelum mengedit file untuk memastikan bahwa perintah berfungsi seperti yang diharapkan.