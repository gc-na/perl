# [Linux] C Shell (csh) df Penggunaan: Memaparkan penggunaan ruang disk

## Overview
Perintah `df` digunakan untuk memaparkan penggunaan ruang disk pada sistem fail. Ia memberikan maklumat mengenai jumlah ruang yang digunakan dan yang tersedia pada sistem fail yang dipasang.

## Usage
Sintaks asas perintah `df` adalah seperti berikut:

```
df [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk perintah `df`:

- `-h`: Memaparkan saiz dalam format yang mudah dibaca (contoh: KB, MB, GB).
- `-T`: Menunjukkan jenis sistem fail untuk setiap sistem fail yang dipaparkan.
- `-a`: Memaparkan semua sistem fail, termasuk yang tidak digunakan.
- `-i`: Memaparkan penggunaan inode, bukan penggunaan ruang disk.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `df`:

1. Memaparkan penggunaan ruang disk dalam format yang mudah dibaca:
   ```csh
   df -h
   ```

2. Memaparkan jenis sistem fail untuk setiap sistem fail:
   ```csh
   df -T
   ```

3. Memaparkan semua sistem fail, termasuk yang tidak digunakan:
   ```csh
   df -a
   ```

4. Memaparkan penggunaan inode:
   ```csh
   df -i
   ```

## Tips
- Gunakan pilihan `-h` untuk melihat maklumat yang lebih mudah difahami, terutamanya jika anda bekerja dengan sistem fail yang besar.
- Periksa penggunaan inode dengan pilihan `-i` jika anda mengalami masalah dengan fail yang tidak dapat dibuat, kerana ini mungkin disebabkan oleh kehabisan inode.
- Sentiasa semak sistem fail yang tidak digunakan dengan pilihan `-a` untuk memastikan tiada ruang yang terbuang.