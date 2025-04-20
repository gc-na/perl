# [Linux] C Shell (csh) groupmod Penggunaan: Mengubah atribut grup pengguna

## Overview
Perintah `groupmod` digunakan untuk mengubah atribut dari grup yang sudah ada di sistem. Dengan menggunakan perintah ini, Anda dapat mengubah nama grup atau GID (Group Identifier) dari grup yang ditentukan.

## Usage
Berikut adalah sintaks dasar dari perintah `groupmod`:

```
groupmod [options] [arguments]
```

## Common Options
- `-n, --new-name <nama_baru>`: Mengubah nama grup menjadi nama baru yang ditentukan.
- `-g, --gid <gid_baru>`: Mengubah GID grup menjadi GID baru yang ditentukan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `groupmod`:

1. **Mengubah nama grup:**
   ```bash
   groupmod -n nama_baru nama_lama
   ```

2. **Mengubah GID grup:**
   ```bash
   groupmod -g 1001 nama_grup
   ```

3. **Mengubah nama dan GID grup secara bersamaan:**
   ```bash
   groupmod -n nama_baru -g 1002 nama_lama
   ```

## Tips
- Pastikan Anda memiliki hak akses yang cukup (biasanya sebagai pengguna root) untuk menjalankan perintah `groupmod`.
- Selalu periksa grup yang ada sebelum melakukan perubahan untuk menghindari konflik nama atau GID.
- Gunakan perintah `getent group` untuk melihat daftar grup dan GID yang ada di sistem Anda.