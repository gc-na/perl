# [Sistem Operasi] C Shell (csh) fdisk: Mengurus partisi cakera

## Overview
Perintah `fdisk` digunakan untuk mengurus partisi cakera pada sistem operasi. Ia membolehkan pengguna untuk mencipta, menghapus, dan mengubah saiz partisi cakera dengan mudah.

## Usage
Berikut adalah sintaks asas untuk perintah `fdisk`:

```
fdisk [options] [arguments]
```

## Common Options
- `-l`: Menyenaraikan semua partisi yang ada pada sistem.
- `-n`: Mencipta partisi baru.
- `-d`: Menghapuskan partisi yang sedia ada.
- `-s`: Menunjukkan saiz partisi tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `fdisk`:

1. **Menyenaraikan semua partisi:**
   ```csh
   fdisk -l
   ```

2. **Mencipta partisi baru:**
   ```csh
   fdisk -n /dev/sda
   ```

3. **Menghapuskan partisi:**
   ```csh
   fdisk -d /dev/sda1
   ```

4. **Menunjukkan saiz partisi tertentu:**
   ```csh
   fdisk -s /dev/sda1
   ```

## Tips
- Sentiasa buat salinan data penting sebelum mengubah partisi untuk mengelakkan kehilangan data.
- Gunakan `fdisk -l` untuk memeriksa keadaan partisi sebelum melakukan sebarang perubahan.
- Pastikan anda mempunyai hak akses yang diperlukan untuk menjalankan perintah ini, biasanya sebagai pengguna root.