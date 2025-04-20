# [Sistem Operasi] C Shell (csh) top penggunaan: Menampilkan proses yang berjalan

## Overview
Perintah `top` digunakan untuk menampilkan informasi tentang proses yang sedang berjalan di sistem. Ini memberikan gambaran real-time mengenai penggunaan CPU, memori, dan sumber daya lainnya oleh proses-proses tersebut.

## Usage
Berikut adalah sintaks dasar dari perintah `top`:

```
top [options] [arguments]
```

## Common Options
- `-d <delay>`: Mengatur interval pembaruan dalam detik.
- `-n <number>`: Menentukan jumlah pembaruan yang akan ditampilkan sebelum keluar.
- `-u <user>`: Menampilkan hanya proses yang dimiliki oleh pengguna tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `top`:

1. Menjalankan `top` dengan pembaruan setiap 5 detik:
   ```csh
   top -d 5
   ```

2. Menampilkan `top` hanya untuk proses yang dimiliki oleh pengguna "john":
   ```csh
   top -u john
   ```

3. Menjalankan `top` dan keluar setelah 10 pembaruan:
   ```csh
   top -n 10
   ```

## Tips
- Gunakan `q` untuk keluar dari tampilan `top`.
- Tekan `h` saat dalam tampilan `top` untuk melihat bantuan dan daftar pintasan keyboard.
- Perhatikan kolom penggunaan CPU dan memori untuk mengidentifikasi proses yang mungkin mempengaruhi kinerja sistem.