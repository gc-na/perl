# [Sistem Operasi] C Shell (csh) stat <Mengambil informasi status file>: Mengambil informasi tentang file dan direktori

## Overview
Perintah `stat` digunakan untuk menampilkan informasi status dari file atau direktori. Informasi yang diberikan mencakup ukuran file, waktu akses, waktu modifikasi, dan izin akses.

## Usage
Berikut adalah sintaks dasar dari perintah `stat`:

```csh
stat [options] [arguments]
```

## Common Options
- `-c` : Menentukan format output yang ingin ditampilkan.
- `-f` : Menampilkan informasi file dalam format yang lebih ringkas.
- `-L` : Mengikuti tautan simbolik dan menampilkan informasi tentang file yang ditunjuk.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `stat`:

1. Menampilkan informasi status dari sebuah file:
   ```csh
   stat namafile.txt
   ```

2. Menampilkan informasi dengan format khusus:
   ```csh
   stat -c '%s %y' namafile.txt
   ```

3. Menampilkan informasi dari tautan simbolik:
   ```csh
   stat -L tautan_simbolik
   ```

4. Menampilkan informasi status dari semua file dalam direktori:
   ```csh
   stat *
   ```

## Tips
- Gunakan opsi `-c` untuk menyesuaikan output agar lebih mudah dibaca sesuai kebutuhan Anda.
- Periksa izin akses file untuk memastikan Anda memiliki hak yang diperlukan sebelum mencoba mengakses atau memodifikasi file.
- Jika Anda bekerja dengan tautan simbolik, ingatlah untuk menggunakan opsi `-L` agar mendapatkan informasi tentang file yang sebenarnya ditunjuk oleh tautan tersebut.