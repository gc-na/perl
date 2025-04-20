# [Sistem Operasi] C Shell (csh) sed Penggunaan: Mengedit teks secara aliran

## Overview
Perintah `sed` adalah singkatan bagi "stream editor". Ia digunakan untuk memanipulasi dan mengedit teks dalam aliran data. `sed` membolehkan pengguna untuk melakukan pelbagai operasi seperti penggantian, penghapusan, dan penyisipan teks tanpa perlu membuka fail dalam editor teks.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `sed`:

```bash
sed [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `sed`:

- `-e`: Menambah arahan pengeditan.
- `-f`: Mengambil arahan pengeditan dari fail.
- `-i`: Mengedit fail secara langsung (in-place).
- `s/pola/g`: Menggantikan semua kemunculan pola dengan teks baru.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `sed`:

1. **Menggantikan teks dalam fail:**
   ```bash
   sed 's/teks_lama/teks_baru/g' fail.txt
   ```

2. **Mengedit fail secara langsung:**
   ```bash
   sed -i 's/teks_lama/teks_baru/g' fail.txt
   ```

3. **Menghapus baris yang mengandungi pola tertentu:**
   ```bash
   sed '/pola_hapus/d' fail.txt
   ```

4. **Menambah teks pada akhir setiap baris:**
   ```bash
   sed 's/$/teks_tambahan/' fail.txt
   ```

## Tips
- Sentiasa buat salinan fail asal sebelum menggunakan pilihan `-i` untuk mengelakkan kehilangan data.
- Gunakan `-n` untuk menyekat output dan hanya mencetak hasil yang dipilih dengan arahan `p`.
- Uji arahan `sed` anda dengan menggunakan `echo` sebelum menerapkannya pada fail untuk memastikan ia berfungsi seperti yang diharapkan.