# [Linux] C Shell (csh) watch penggunaan: Memantau perintah secara berulang

## Overview
Perintah `watch` dalam C Shell (csh) digunakan untuk menjalankan perintah tertentu secara berulang pada selang waktu yang ditentukan. Ini sangat berguna untuk memantau perubahan dalam output perintah, seperti status sistem atau hasil dari perintah lain.

## Usage
Sintaks asas untuk perintah `watch` adalah seperti berikut:

```
watch [options] [arguments]
```

## Common Options
- `-n <seconds>`: Menentukan selang waktu dalam saat antara setiap pengulangan perintah.
- `-d`: Menyoroti perubahan dalam output antara pengulangan.
- `-t`: Menyembunyikan header yang menunjukkan waktu dan perintah yang sedang dijalankan.

## Common Examples
Berikut adalah beberapa contoh praktikal menggunakan perintah `watch`:

1. Memantau penggunaan memori sistem setiap 2 saat:
   ```csh
   watch -n 2 free -h
   ```

2. Memantau status proses tertentu:
   ```csh
   watch -d ps aux | grep httpd
   ```

3. Memantau direktori untuk perubahan dalam fail:
   ```csh
   watch -n 5 ls -l /path/to/directory
   ```

4. Memantau penggunaan CPU:
   ```csh
   watch -n 1 top -b -n 1
   ```

## Tips
- Gunakan opsi `-d` untuk lebih mudah melihat perubahan dalam output, terutama jika outputnya panjang.
- Sesuaikan selang waktu dengan keperluan anda; tidak perlu terlalu cepat jika tidak ada perubahan yang diharapkan.
- Pastikan perintah yang anda gunakan dalam `watch` tidak memerlukan input interaktif, kerana ini boleh menyebabkan masalah.