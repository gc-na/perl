# [Sistem Operasi] C Shell (csh) who Penggunaan: Menampilkan pengguna yang sedang masuk

## Overview
Perintah `who` digunakan untuk menampilkan daftar pengguna yang sedang masuk ke sistem. Ini memberikan informasi tentang nama pengguna, terminal yang mereka gunakan, waktu masuk, dan alamat IP atau hostname jika tersedia.

## Usage
Berikut adalah sintaks dasar dari perintah `who`:

```
who [options] [arguments]
```

## Common Options
Beberapa opsi umum untuk perintah `who` meliputi:

- `-a`: Menampilkan semua informasi yang tersedia, termasuk pengguna yang tidak aktif.
- `-b`: Menampilkan waktu terakhir sistem di-boot.
- `-q`: Menampilkan hanya jumlah pengguna yang sedang masuk dan nama pengguna mereka.
- `-H`: Menampilkan header kolom untuk output.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `who`:

1. Menampilkan daftar pengguna yang sedang masuk:
   ```csh
   who
   ```

2. Menampilkan semua informasi pengguna, termasuk yang tidak aktif:
   ```csh
   who -a
   ```

3. Menampilkan waktu terakhir sistem di-boot:
   ```csh
   who -b
   ```

4. Menampilkan hanya jumlah pengguna yang sedang masuk:
   ```csh
   who -q
   ```

5. Menampilkan output dengan header kolom:
   ```csh
   who -H
   ```

## Tips
- Gunakan opsi `-H` untuk memudahkan pembacaan output, terutama jika Anda bekerja dengan banyak pengguna.
- Kombinasikan `who` dengan perintah lain seperti `grep` untuk mencari pengguna tertentu.
- Periksa secara berkala siapa yang sedang masuk ke sistem untuk keamanan dan manajemen pengguna yang lebih baik.