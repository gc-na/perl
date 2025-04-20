# [Linux] C Shell (csh) resize2fs: Mengubah saiz sistem fail

## Overview
Perintah `resize2fs` digunakan untuk mengubah saiz sistem fail ext2, ext3, atau ext4. Ia membolehkan pengguna menyesuaikan saiz sistem fail untuk memenuhi keperluan penyimpanan yang berubah-ubah.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `resize2fs`:

```
resize2fs [options] [arguments]
```

## Common Options
- `-f`: Memaksa pengubahsuaian saiz walaupun sistem fail tidak berada dalam keadaan yang sesuai.
- `-p`: Menunjukkan kemajuan semasa proses pengubahsuaian saiz.
- `-s`: Mengubah saiz sistem fail kepada saiz yang ditentukan tanpa mengubah saiz partition.
- `-M`: Mengubah saiz sistem fail kepada saiz minimum yang diperlukan.

## Common Examples
Berikut adalah beberapa contoh penggunaan `resize2fs`:

1. Mengubah saiz sistem fail kepada saiz maksimum yang dibenarkan:
   ```bash
   resize2fs /dev/sda1
   ```

2. Mengubah saiz sistem fail kepada saiz tertentu, contohnya 20G:
   ```bash
   resize2fs /dev/sda1 20G
   ```

3. Memaksa pengubahsuaian saiz walaupun terdapat amaran:
   ```bash
   resize2fs -f /dev/sda1
   ```

4. Menunjukkan kemajuan semasa proses pengubahsuaian:
   ```bash
   resize2fs -p /dev/sda1
   ```

## Tips
- Pastikan untuk melakukan backup data penting sebelum mengubah saiz sistem fail.
- Gunakan perintah `df -h` untuk memeriksa penggunaan ruang sebelum dan selepas pengubahsuaian.
- Sentiasa pastikan sistem fail tidak sedang digunakan semasa proses pengubahsuaian untuk mengelakkan kerosakan data.