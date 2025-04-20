# [Linux] C Shell (csh) trap Penggunaan: Mengendalikan sinyal dalam skrip

## Overview
Perintah `trap` dalam C Shell (csh) digunakan untuk menangkap dan mengendalikan sinyal yang diterima oleh skrip. Ini membolehkan pengguna untuk menjalankan perintah tertentu apabila sinyal tertentu diterima, seperti ketika skrip dihentikan secara tidak sengaja.

## Usage
Berikut adalah sintaks asas untuk perintah `trap`:

```csh
trap [options] [arguments]
```

## Common Options
- `signal`: Menentukan sinyal yang ingin ditangkap (contoh: `INT`, `TERM`).
- `command`: Perintah yang akan dijalankan apabila sinyal ditangkap.

## Common Examples
1. **Menangkap Sinyal INT (Ctrl+C)**

   Dalam contoh ini, apabila pengguna menekan Ctrl+C, skrip akan mencetak mesej dan keluar dengan selamat.

   ```csh
   trap 'echo "Sinyal INT diterima, keluar..."' INT
   while (1)
       echo "Skrip sedang berjalan..."
       sleep 1
   end
   ```

2. **Menangkap Sinyal TERM**

   Skrip ini akan menangkap sinyal TERM dan mencetak mesej sebelum keluar.

   ```csh
   trap 'echo "Sinyal TERM diterima, menutup skrip..."' TERM
   while (1)
       echo "Skrip masih aktif..."
       sleep 1
   end
   ```

3. **Menggunakan trap untuk pembersihan**

   Dalam contoh ini, kita menggunakan `trap` untuk menghapus fail sementara apabila skrip dihentikan.

   ```csh
   trap 'rm -f /tmp/mytempfile; echo "Fail sementara dibuang."' EXIT
   touch /tmp/mytempfile
   echo "Skrip sedang berjalan. Fail sementara telah dibuat."
   sleep 10
   ```

## Tips
- Sentiasa gunakan `trap` untuk memastikan sumber daya dibersihkan dengan betul apabila skrip dihentikan.
- Uji skrip anda dengan pelbagai sinyal untuk memastikan bahawa `trap` berfungsi seperti yang diharapkan.
- Gunakan `trap` dengan berhati-hati, kerana menangkap sinyal yang salah boleh mengganggu aliran normal skrip.