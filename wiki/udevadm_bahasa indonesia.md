# [Linux] C Shell (csh) udevadm Penggunaan: Mengelola perangkat di sistem

## Overview
Perintah `udevadm` digunakan untuk mengelola dan memantau perangkat di sistem Linux. Ini adalah alat yang berinteraksi dengan sistem udev, yang bertanggung jawab untuk mengelola perangkat keras dan memberikan informasi tentang perangkat yang terhubung ke sistem.

## Usage
Sintaks dasar dari perintah `udevadm` adalah sebagai berikut:

```
udevadm [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum untuk `udevadm` beserta penjelasannya:

- `info`: Menampilkan informasi tentang perangkat tertentu.
- `trigger`: Memicu aturan udev untuk perangkat yang ada.
- `settle`: Menunggu hingga semua perangkat udev selesai diproses.
- `control`: Mengontrol daemon udev.

## Common Examples
Berikut adalah beberapa contoh penggunaan `udevadm`:

1. Menampilkan informasi tentang perangkat tertentu:
   ```bash
   udevadm info --query=all --name=/dev/sda
   ```

2. Memicu aturan udev untuk semua perangkat:
   ```bash
   udevadm trigger
   ```

3. Menunggu hingga semua perangkat selesai diproses:
   ```bash
   udevadm settle
   ```

4. Mengontrol daemon udev:
   ```bash
   udevadm control --reload-rules
   ```

## Tips
- Selalu gunakan opsi `info` untuk mendapatkan informasi lengkap tentang perangkat sebelum melakukan perubahan.
- Gunakan `trigger` dengan hati-hati, karena dapat memicu banyak aturan dan mempengaruhi banyak perangkat.
- Pastikan untuk menjalankan `udevadm control --reload-rules` setelah mengedit file aturan udev agar perubahan diterapkan.