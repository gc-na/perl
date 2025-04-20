# [Sistem Operasi] C Shell (csh) fdisk Penggunaan: Mengelola partisi disk

## Overview
Perintah `fdisk` digunakan untuk mengelola partisi disk pada sistem operasi berbasis Unix. Dengan `fdisk`, pengguna dapat membuat, menghapus, dan mengubah ukuran partisi, serta melihat informasi tentang partisi yang ada.

## Usage
Berikut adalah sintaks dasar dari perintah `fdisk`:

```csh
fdisk [options] [arguments]
```

## Common Options
- `-l` : Menampilkan daftar semua partisi yang ada pada disk.
- `-n` : Membuat partisi baru.
- `-d` : Menghapus partisi yang sudah ada.
- `-u` : Mengatur ukuran partisi dalam sektor.

## Common Examples
Berikut adalah beberapa contoh penggunaan `fdisk`:

1. **Menampilkan daftar partisi:**
   ```csh
   fdisk -l
   ```

2. **Membuat partisi baru:**
   ```csh
   fdisk /dev/sda
   ```
   Setelah menjalankan perintah ini, ikuti instruksi untuk membuat partisi baru.

3. **Menghapus partisi:**
   ```csh
   fdisk /dev/sda
   ```
   Setelah menjalankan perintah ini, pilih opsi untuk menghapus partisi yang diinginkan.

4. **Mengubah ukuran partisi:**
   ```csh
   fdisk /dev/sda
   ```
   Pilih partisi yang ingin diubah ukurannya dan ikuti instruksi yang diberikan.

## Tips
- Selalu cadangkan data penting sebelum melakukan perubahan pada partisi.
- Gunakan `fdisk` dengan hati-hati, karena kesalahan dapat menyebabkan kehilangan data.
- Periksa dokumentasi tambahan dengan menjalankan `man fdisk` untuk informasi lebih lanjut tentang opsi dan penggunaannya.