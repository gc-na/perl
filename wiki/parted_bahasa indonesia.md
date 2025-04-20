# [Sistem Operasi] C Shell (csh) parted Penggunaan: Mengelola Partisi Disk

## Overview
Perintah `parted` digunakan untuk mengelola partisi pada disk. Dengan `parted`, pengguna dapat membuat, menghapus, dan mengubah ukuran partisi dengan mudah. Ini sangat berguna untuk mengatur ruang penyimpanan pada sistem operasi.

## Usage
Berikut adalah sintaks dasar dari perintah `parted`:

```csh
parted [options] [arguments]
```

## Common Options
- `-l` : Menampilkan daftar semua disk dan partisi yang tersedia.
- `mkpart` : Membuat partisi baru.
- `rm` : Menghapus partisi yang ada.
- `resizepart` : Mengubah ukuran partisi yang sudah ada.
- `print` : Menampilkan informasi tentang partisi yang ada.

## Common Examples
Berikut adalah beberapa contoh penggunaan `parted`:

1. **Menampilkan daftar partisi:**
   ```csh
   parted -l
   ```

2. **Membuat partisi baru:**
   ```csh
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

3. **Menghapus partisi:**
   ```csh
   parted /dev/sda rm 1
   ```

4. **Mengubah ukuran partisi:**
   ```csh
   parted /dev/sda resizepart 1 200MiB
   ```

5. **Menampilkan informasi partisi:**
   ```csh
   parted /dev/sda print
   ```

## Tips
- Selalu pastikan untuk melakukan backup data sebelum mengubah partisi.
- Gunakan `print` untuk memeriksa struktur partisi sebelum melakukan perubahan.
- Hati-hati saat menggunakan perintah `rm`, karena menghapus partisi dapat mengakibatkan kehilangan data.