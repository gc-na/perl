# [Linux] C Shell (csh) update-rc.d: Mengelola skrip inisialisasi sistem

## Overview
Perintah `update-rc.d` digunakan untuk mengelola skrip inisialisasi sistem pada distribusi Linux yang menggunakan sistem init. Perintah ini memungkinkan pengguna untuk menambahkan, menghapus, atau mengubah prioritas skrip inisialisasi yang dijalankan saat booting.

## Usage
Berikut adalah sintaks dasar dari perintah `update-rc.d`:

```csh
update-rc.d [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `update-rc.d`:

- `defaults`: Menambahkan skrip dengan prioritas default.
- `remove`: Menghapus skrip dari direktori inisialisasi.
- `enable`: Mengaktifkan skrip inisialisasi.
- `disable`: Menonaktifkan skrip inisialisasi.
- `start <N>`: Menentukan urutan skrip untuk dijalankan saat booting.
- `stop <N>`: Menentukan urutan skrip untuk dihentikan saat shutdown.

## Common Examples
Berikut adalah beberapa contoh penggunaan `update-rc.d`:

1. **Menambahkan skrip inisialisasi dengan prioritas default:**
   ```csh
   update-rc.d myscript defaults
   ```

2. **Menghapus skrip inisialisasi:**
   ```csh
   update-rc.d myscript remove
   ```

3. **Mengaktifkan skrip inisialisasi:**
   ```csh
   update-rc.d myscript enable
   ```

4. **Menonaktifkan skrip inisialisasi:**
   ```csh
   update-rc.d myscript disable
   ```

5. **Menentukan urutan skrip saat booting:**
   ```csh
   update-rc.d myscript start 20 2 3 4 5 . stop 20 0 1 6 .
   ```

## Tips
- Pastikan untuk memeriksa apakah skrip inisialisasi Anda memiliki izin eksekusi sebelum menambahkannya.
- Gunakan opsi `remove` dengan hati-hati, karena ini akan menghapus skrip dari semua runlevel.
- Selalu lakukan backup pada skrip inisialisasi sebelum melakukan perubahan untuk menghindari masalah saat booting.