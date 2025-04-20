# [Sistem Operasi] C Shell (csh) fsck: Memeriksa dan membaiki sistem fail

## Overview
Perintah `fsck` digunakan untuk memeriksa dan membaiki sistem fail pada sistem pengendalian Unix dan Linux. Ia memastikan bahawa sistem fail berfungsi dengan baik dan tiada kerosakan yang boleh menyebabkan kehilangan data.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `fsck`:

```
fsck [options] [arguments]
```

## Common Options
- `-a` : Membaiki kesilapan secara automatik tanpa meminta pengesahan pengguna.
- `-n` : Melakukan pemeriksaan tanpa membaiki sebarang kesilapan.
- `-y` : Menganggap jawapan 'ya' untuk semua soalan yang ditanya semasa proses pemeriksaan.
- `-t` : Menunjukkan masa yang diambil untuk setiap pemeriksaan.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `fsck`:

1. Memeriksa sistem fail secara manual:
   ```bash
   fsck /dev/sda1
   ```

2. Membaiki kesilapan secara automatik:
   ```bash
   fsck -a /dev/sda1
   ```

3. Melakukan pemeriksaan tanpa membaiki:
   ```bash
   fsck -n /dev/sda1
   ```

4. Menganggap 'ya' untuk semua soalan:
   ```bash
   fsck -y /dev/sda1
   ```

## Tips
- Sentiasa buat salinan data penting sebelum menjalankan `fsck`, terutamanya jika anda menggunakan pilihan yang membaiki secara automatik.
- Jalankan `fsck` semasa sistem tidak aktif untuk mengelakkan kerosakan pada sistem fail.
- Gunakan pilihan `-n` terlebih dahulu untuk memeriksa kesilapan tanpa membuat sebarang perubahan, sebelum memutuskan untuk membaiki.