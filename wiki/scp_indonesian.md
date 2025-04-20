# [Sistem Operasi] C Shell (csh) scp: [menyalin file secara aman]

## Overview
Perintah `scp` (Secure Copy Protocol) digunakan untuk menyalin file atau direktori antara komputer secara aman melalui protokol SSH. Ini memungkinkan pengguna untuk mentransfer file dengan enkripsi, menjaga keamanan data selama proses transfer.

## Usage
Berikut adalah sintaks dasar dari perintah `scp`:

```bash
scp [options] [source] [destination]
```

## Common Options
- `-r`: Menyalin direktori secara rekursif.
- `-P`: Menentukan port SSH yang digunakan (perhatikan huruf besar).
- `-i`: Menentukan file kunci identitas untuk otentikasi.
- `-v`: Menampilkan informasi proses transfer yang lebih detail (verbose).

## Common Examples
Berikut adalah beberapa contoh penggunaan `scp`:

1. Menyalin file dari lokal ke server:
   ```bash
   scp file.txt user@remote_host:/path/to/destination
   ```

2. Menyalin file dari server ke lokal:
   ```bash
   scp user@remote_host:/path/to/file.txt /local/destination
   ```

3. Menyalin direktori secara rekursif:
   ```bash
   scp -r /local/directory user@remote_host:/path/to/destination
   ```

4. Menyalin file menggunakan port yang berbeda:
   ```bash
   scp -P 2222 file.txt user@remote_host:/path/to/destination
   ```

## Tips
- Selalu pastikan bahwa Anda memiliki izin yang tepat untuk mengakses file yang ingin Anda salin.
- Gunakan opsi `-v` untuk membantu dalam pemecahan masalah jika transfer file tidak berhasil.
- Pertimbangkan untuk menggunakan kunci SSH untuk otentikasi yang lebih aman daripada menggunakan kata sandi.