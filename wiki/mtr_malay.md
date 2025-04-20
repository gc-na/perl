# [Sistem Pengendalian] C Shell (csh) mtr Penggunaan: Menyemak laluan rangkaian

## Overview
Perintah `mtr` (My Traceroute) digunakan untuk mendiagnosis dan memantau laluan rangkaian dari komputer anda ke alamat IP atau nama domain tertentu. Ia menggabungkan fungsi `ping` dan `traceroute`, memberikan maklumat tentang masa perjalanan dan kehilangan paket di setiap hop dalam laluan rangkaian.

## Usage
Berikut adalah sintaks asas untuk perintah `mtr`:

```
mtr [options] [arguments]
```

## Common Options
- `-r`: Menghasilkan laporan ringkas dan keluar setelah selesai.
- `-c <count>`: Menentukan bilangan paket yang akan dihantar.
- `-i <interval>`: Menetapkan selang masa antara pengiriman paket.
- `-p`: Menunjukkan nombor port yang digunakan untuk sambungan.
- `-w`: Menggunakan mod lebar untuk output yang lebih mudah dibaca.

## Common Examples
Berikut adalah beberapa contoh penggunaan `mtr`:

1. Menjalankan `mtr` ke alamat IP tertentu:
   ```bash
   mtr 8.8.8.8
   ```

2. Menghasilkan laporan ringkas:
   ```bash
   mtr -r 8.8.8.8
   ```

3. Menghantar 10 paket ke nama domain:
   ```bash
   mtr -c 10 www.google.com
   ```

4. Menetapkan selang masa 1 saat antara paket:
   ```bash
   mtr -i 1 8.8.8.8
   ```

5. Menggunakan mod lebar untuk output:
   ```bash
   mtr -w 8.8.8.8
   ```

## Tips
- Sentiasa gunakan `-r` untuk mendapatkan laporan ringkas jika anda hanya memerlukan hasil tanpa interaksi berterusan.
- Gunakan `-c` untuk mengawal jumlah paket yang dihantar, terutamanya jika anda ingin mengelakkan beban rangkaian yang berlebihan.
- Perhatikan waktu perjalanan dan kehilangan paket untuk mengenal pasti masalah dalam rangkaian.