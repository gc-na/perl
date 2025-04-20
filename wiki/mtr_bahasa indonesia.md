# [Sistem Operasi] C Shell (csh) mtr Penggunaan: Memeriksa konektivitas jaringan

## Overview
Perintah `mtr` (My Traceroute) adalah alat yang menggabungkan fungsi dari `ping` dan `traceroute`. Ia digunakan untuk menganalisis jalur yang dilalui paket data menuju host tertentu dan mengukur waktu respons dari setiap hop dalam jaringan.

## Usage
Berikut adalah sintaks dasar dari perintah `mtr`:

```bash
mtr [options] [arguments]
```

## Common Options
- `-r`: Menjalankan dalam mode laporan, yang akan menampilkan hasil dalam format yang lebih ringkas.
- `-c <count>`: Menentukan jumlah ping yang akan dikirim sebelum menghentikan.
- `-i <interval>`: Menentukan interval waktu antara pengiriman ping.
- `-p`: Menjalankan dalam mode hanya untuk ping, tanpa traceroute.
- `--report`: Menghasilkan laporan ringkas setelah pengujian selesai.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `mtr`:

1. Menjalankan `mtr` ke sebuah host:
   ```bash
   mtr google.com
   ```

2. Menjalankan `mtr` dengan jumlah ping tertentu:
   ```bash
   mtr -c 10 google.com
   ```

3. Menggunakan `mtr` dalam mode laporan:
   ```bash
   mtr -r google.com
   ```

4. Menentukan interval antara ping:
   ```bash
   mtr -i 1 google.com
   ```

5. Menjalankan `mtr` hanya untuk ping:
   ```bash
   mtr -p google.com
   ```

## Tips
- Gunakan opsi `-r` untuk mendapatkan ringkasan yang lebih mudah dibaca setelah pengujian.
- Cobalah mengubah interval dengan opsi `-i` untuk melihat bagaimana waktu respons bervariasi.
- Jika Anda ingin mengawasi konektivitas secara berkelanjutan, pertimbangkan untuk menjalankan `mtr` tanpa batas waktu dengan menyesuaikan opsi `-c`.