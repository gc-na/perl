# [Sistem Operasi] C Shell (csh) groupmod <Mengelola grup pengguna>: Mengubah atribut grup pengguna

## Overview
Perintah `groupmod` digunakan untuk mengubah atribut dari grup pengguna yang sudah ada di sistem. Dengan menggunakan perintah ini, Anda dapat mengubah nama grup atau GID (Group ID) grup yang ada.

## Usage
Berikut adalah sintaks dasar dari perintah `groupmod`:

```csh
groupmod [options] [arguments]
```

## Common Options
- `-n, --new-name NEW_GROUP`: Mengubah nama grup menjadi `NEW_GROUP`.
- `-g, --gid GID`: Mengubah GID grup menjadi nilai yang ditentukan.
- `-o, --non-unique`: Mengizinkan penggunaan GID yang tidak unik.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `groupmod`:

1. **Mengubah nama grup**:
   ```csh
   groupmod -n nama_baru nama_lama
   ```

2. **Mengubah GID grup**:
   ```csh
   groupmod -g 1001 nama_grup
   ```

3. **Mengubah nama grup dan GID**:
   ```csh
   groupmod -n nama_baru -g 1002 nama_lama
   ```

4. **Mengizinkan GID tidak unik**:
   ```csh
   groupmod -o -g 1001 nama_grup
   ```

## Tips
- Pastikan Anda memiliki hak akses yang cukup untuk menjalankan perintah `groupmod`, biasanya Anda perlu menjadi pengguna dengan hak istimewa (root).
- Selalu periksa grup yang ada sebelum melakukan perubahan untuk menghindari konflik nama atau GID.
- Gunakan perintah `getent group` untuk melihat daftar grup dan atributnya sebelum mengubahnya.