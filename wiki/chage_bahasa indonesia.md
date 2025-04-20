# [Linux] C Shell (csh) chage Penggunaan: Mengelola Kebijakan Kata Sandi Pengguna

## Overview
Perintah `chage` digunakan untuk mengelola kebijakan kata sandi pengguna di sistem Linux. Dengan `chage`, administrator dapat mengatur masa berlaku kata sandi, kapan pengguna harus mengubah kata sandi mereka, dan informasi terkait lainnya.

## Usage
Berikut adalah sintaks dasar dari perintah `chage`:

```bash
chage [options] [arguments]
```

## Common Options
- `-l`: Menampilkan informasi tentang kebijakan kata sandi pengguna.
- `-m`: Mengatur jumlah hari minimum sebelum kata sandi dapat diubah.
- `-M`: Mengatur jumlah hari maksimum sebelum kata sandi harus diubah.
- `-I`: Mengatur jumlah hari setelah kata sandi kedaluwarsa sebelum akun dinonaktifkan.
- `-E`: Mengatur tanggal kedaluwarsa akun pengguna.

## Common Examples
Berikut adalah beberapa contoh penggunaan `chage`:

1. Menampilkan informasi kebijakan kata sandi untuk pengguna `john`:
   ```bash
   chage -l john
   ```

2. Mengatur agar pengguna `alice` harus mengubah kata sandi mereka setiap 30 hari:
   ```bash
   chage -M 30 alice
   ```

3. Mengatur agar pengguna `bob` tidak dapat mengubah kata sandi mereka selama 10 hari setelah pengaturan awal:
   ```bash
   chage -m 10 bob
   ```

4. Mengatur tanggal kedaluwarsa akun pengguna `charlie` pada 31 Desember 2023:
   ```bash
   chage -E 2023-12-31 charlie
   ```

## Tips
- Selalu periksa kebijakan kata sandi yang ada sebelum mengubahnya untuk memastikan tidak mengganggu pengguna.
- Gunakan opsi `-l` untuk memverifikasi pengaturan setelah melakukan perubahan.
- Pastikan untuk memberikan pemberitahuan kepada pengguna jika mereka diharuskan untuk mengubah kata sandi mereka.