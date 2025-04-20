# [Sistem Operasi] C Shell (csh) hostname: Menampilkan atau mengatur nama host

## Overview
Perintah `hostname` dalam C Shell (csh) digunakan untuk menampilkan atau mengatur nama host dari sistem yang sedang digunakan. Nama host adalah identitas unik yang diberikan kepada komputer dalam jaringan.

## Usage
Berikut adalah sintaks dasar dari perintah `hostname`:

```
hostname [options] [arguments]
```

## Common Options
- `-s`: Menampilkan hanya nama host singkat.
- `-f`: Menampilkan nama host lengkap (fully qualified domain name).
- `-i`: Menampilkan alamat IP dari nama host.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `hostname`:

1. Menampilkan nama host saat ini:
   ```csh
   hostname
   ```

2. Menampilkan nama host singkat:
   ```csh
   hostname -s
   ```

3. Menampilkan nama host lengkap:
   ```csh
   hostname -f
   ```

4. Menampilkan alamat IP dari nama host:
   ```csh
   hostname -i
   ```

5. Mengatur nama host baru:
   ```csh
   hostname new-hostname
   ```

## Tips
- Pastikan Anda memiliki hak akses yang cukup untuk mengubah nama host.
- Setelah mengubah nama host, Anda mungkin perlu me-restart layanan jaringan agar perubahan diterapkan.
- Gunakan opsi `-f` untuk memastikan Anda mendapatkan nama host lengkap yang diperlukan untuk konfigurasi jaringan.