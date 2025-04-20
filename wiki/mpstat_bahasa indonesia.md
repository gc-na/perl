# [Sistem Operasi] C Shell (csh) mpstat Penggunaan: Memantau Statistik CPU

## Overview
Perintah `mpstat` digunakan untuk menampilkan statistik penggunaan CPU pada sistem. Ini memberikan informasi tentang penggunaan CPU secara keseluruhan dan per CPU secara individual, yang berguna untuk analisis kinerja sistem.

## Usage
Berikut adalah sintaks dasar dari perintah `mpstat`:

```
mpstat [options] [arguments]
```

## Common Options
- `-P ALL` : Menampilkan statistik untuk semua CPU.
- `-u` : Menampilkan penggunaan CPU dalam persentase.
- `-w` : Menampilkan informasi tentang waktu menunggu.
- `-h` : Menampilkan bantuan tentang penggunaan perintah.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `mpstat`:

1. Menampilkan statistik CPU untuk semua prosesor:
   ```bash
   mpstat -P ALL
   ```

2. Menampilkan penggunaan CPU dalam persentase:
   ```bash
   mpstat -u
   ```

3. Menampilkan statistik CPU setiap 5 detik:
   ```bash
   mpstat 5
   ```

4. Menampilkan informasi waktu menunggu:
   ```bash
   mpstat -w
   ```

## Tips
- Gunakan opsi `-P ALL` untuk mendapatkan gambaran lengkap tentang penggunaan CPU di semua inti.
- Jalankan `mpstat` dalam interval waktu tertentu untuk memantau perubahan penggunaan CPU secara real-time.
- Kombinasikan `mpstat` dengan perintah lain seperti `grep` untuk menyaring informasi yang relevan.