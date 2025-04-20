# [Sistem Operasi] C Shell (csh) who penggunaan: Menampilkan pengguna yang sedang masuk

## Overview
Perintah `who` digunakan untuk menampilkan daftar pengguna yang saat ini sedang masuk ke sistem. Informasi yang ditampilkan termasuk nama pengguna, terminal yang digunakan, waktu masuk, dan alamat IP atau hostname dari mana pengguna terhubung.

## Usage
Berikut adalah sintaks dasar dari perintah `who`:

```
who [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `who`:

- `-a`: Menampilkan semua informasi yang tersedia, termasuk pengguna yang tidak aktif.
- `-b`: Menampilkan waktu terakhir sistem di-reboot.
- `-q`: Menampilkan hanya nama pengguna yang sedang masuk dan jumlah total pengguna.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `who`:

1. Menampilkan daftar pengguna yang sedang masuk:
   ```csh
   who
   ```

2. Menampilkan semua informasi pengguna dan status:
   ```csh
   who -a
   ```

3. Menampilkan waktu terakhir sistem di-reboot:
   ```csh
   who -b
   ```

4. Menampilkan hanya nama pengguna yang sedang masuk dan jumlah total pengguna:
   ```csh
   who -q
   ```

## Tips
- Gunakan opsi `-a` untuk mendapatkan informasi lebih lengkap tentang pengguna dan status sistem.
- Perintah `who` dapat digunakan bersama dengan perintah lain seperti `grep` untuk mencari pengguna tertentu.
- Untuk memantau aktivitas pengguna secara real-time, pertimbangkan untuk menggunakan perintah `w` yang memberikan informasi lebih detail tentang aktivitas pengguna.