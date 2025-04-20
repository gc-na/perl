# [Linux] C Shell (csh) e2fsck Penggunaan: Memeriksa dan membaiki sistem fail ext2/ext3/ext4

## Overview
Perintah `e2fsck` digunakan untuk memeriksa dan membaiki sistem fail yang menggunakan format ext2, ext3, atau ext4. Ia membantu memastikan integriti dan kesihatan sistem fail, serta membaiki sebarang kesalahan yang mungkin berlaku.

## Usage
Sintaks asas untuk menggunakan `e2fsck` adalah seperti berikut:

```
e2fsck [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `e2fsck` beserta penjelasan ringkas:

- `-p` : Memperbaiki kesalahan secara automatik tanpa meminta pengesahan.
- `-f` : Memaksa pemeriksaan walaupun sistem fail kelihatan bersih.
- `-n` : Melakukan pemeriksaan tanpa membaiki sebarang kesalahan.
- `-c` : Memeriksa blok yang buruk sebelum memulakan pemeriksaan.
- `-y` : Menganggap jawapan 'ya' untuk semua pertanyaan semasa pemeriksaan.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `e2fsck`:

1. Memeriksa sistem fail tanpa membaiki:
   ```bash
   e2fsck /dev/sda1
   ```

2. Memperbaiki sistem fail secara automatik:
   ```bash
   e2fsck -p /dev/sda1
   ```

3. Memaksa pemeriksaan walaupun sistem fail kelihatan bersih:
   ```bash
   e2fsck -f /dev/sda1
   ```

4. Memeriksa dan membaiki sistem fail sambil menganggap semua jawapan 'ya':
   ```bash
   e2fsck -y /dev/sda1
   ```

5. Memeriksa blok yang buruk sebelum pemeriksaan:
   ```bash
   e2fsck -c /dev/sda1
   ```

## Tips
- Sentiasa buat salinan sandaran data penting sebelum menjalankan `e2fsck`, terutamanya jika anda menggunakan pilihan yang membaiki.
- Gunakan pilihan `-n` untuk melakukan pemeriksaan tanpa risiko membaiki, jika anda ingin melihat laporan kesalahan terlebih dahulu.
- Jalankan `e2fsck` semasa sistem tidak aktif untuk mengelakkan sebarang konflik dengan proses lain yang menggunakan sistem fail.