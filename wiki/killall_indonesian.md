# [Sistem Operasi] C Shell (csh) killall Penggunaan: Menghentikan semua proses dengan nama tertentu

## Overview
Perintah `killall` digunakan untuk menghentikan semua proses yang berjalan dengan nama tertentu. Ini sangat berguna ketika Anda ingin menghentikan beberapa instance dari aplikasi yang sama tanpa harus mencari dan menghentikan setiap proses secara manual.

## Usage
Berikut adalah sintaks dasar dari perintah `killall`:

```
killall [options] [arguments]
```

## Common Options
- `-9`: Mengirim sinyal SIGKILL untuk menghentikan proses secara paksa.
- `-v`: Menampilkan informasi lebih lanjut tentang proses yang dihentikan.
- `-i`: Meminta konfirmasi sebelum menghentikan setiap proses.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `killall`:

1. Menghentikan semua proses dengan nama `firefox`:
   ```csh
   killall firefox
   ```

2. Menghentikan semua proses dengan nama `gedit` dan menampilkan informasi:
   ```csh
   killall -v gedit
   ```

3. Menghentikan semua proses dengan nama `myapp` secara paksa:
   ```csh
   killall -9 myapp
   ```

4. Meminta konfirmasi sebelum menghentikan proses `vlc`:
   ```csh
   killall -i vlc
   ```

## Tips
- Selalu pastikan untuk memeriksa nama proses yang ingin Anda hentikan agar tidak menghentikan proses yang salah.
- Gunakan opsi `-v` untuk mendapatkan umpan balik tentang proses yang dihentikan, terutama saat bekerja dengan banyak proses.
- Jika Anda tidak yakin tentang proses yang sedang berjalan, gunakan perintah `ps` untuk melihat daftar proses sebelum menggunakan `killall`.