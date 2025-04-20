# [Sistem Operasi] C Shell (csh) du: Menghitung ukuran direktori dan file

## Overview
Perintah `du` (disk usage) digunakan untuk menghitung dan menampilkan ukuran dari file dan direktori di sistem file. Ini sangat berguna untuk mengetahui seberapa banyak ruang disk yang digunakan oleh file atau direktori tertentu.

## Usage
Berikut adalah sintaks dasar dari perintah `du`:

```
du [options] [arguments]
```

## Common Options
- `-h`: Menampilkan ukuran dalam format yang lebih mudah dibaca (misalnya, KB, MB).
- `-s`: Menampilkan total ukuran dari direktori tanpa menampilkan ukuran subdirektori.
- `-a`: Menampilkan ukuran dari semua file, bukan hanya direktori.
- `-c`: Menampilkan total ukuran di akhir output.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `du`:

1. Menampilkan ukuran dari direktori saat ini:
   ```csh
   du
   ```

2. Menampilkan ukuran dalam format yang lebih mudah dibaca:
   ```csh
   du -h
   ```

3. Menampilkan total ukuran dari direktori tertentu:
   ```csh
   du -sh /path/to/directory
   ```

4. Menampilkan ukuran dari semua file dan direktori di dalam direktori saat ini:
   ```csh
   du -a
   ```

5. Menampilkan ukuran dari direktori dan total ukuran di akhir:
   ```csh
   du -ch /path/to/directory
   ```

## Tips
- Gunakan opsi `-h` untuk memudahkan pemahaman ukuran file, terutama jika Anda bekerja dengan file besar.
- Kombinasikan opsi `-s` dan `-h` untuk mendapatkan total ukuran yang mudah dibaca dari direktori besar.
- Periksa ukuran direktori secara berkala untuk mengelola ruang disk dengan lebih baik.