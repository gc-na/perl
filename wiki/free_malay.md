# [Sistem Operasi] C Shell (csh) free: Menunjukkan penggunaan memori sistem

## Overview
Perintah `free` digunakan untuk memaparkan penggunaan memori dalam sistem Linux. Ia memberikan gambaran tentang jumlah memori yang digunakan, tersedia, dan juga memori swap yang digunakan oleh sistem.

## Usage
Berikut adalah sintaks asas untuk perintah `free`:

```
free [options] [arguments]
```

## Common Options
- `-h`: Menunjukkan penggunaan memori dalam format yang lebih mudah dibaca (human-readable).
- `-m`: Menunjukkan penggunaan memori dalam megabait.
- `-g`: Menunjukkan penggunaan memori dalam gigabait.
- `-s [seconds]`: Mengemas kini paparan penggunaan memori setiap beberapa saat yang ditentukan.

## Common Examples
1. Menunjukkan penggunaan memori dalam format yang mudah dibaca:
   ```bash
   free -h
   ```

2. Menunjukkan penggunaan memori dalam megabait:
   ```bash
   free -m
   ```

3. Menunjukkan penggunaan memori dalam gigabait:
   ```bash
   free -g
   ```

4. Mengemas kini paparan penggunaan memori setiap 5 saat:
   ```bash
   free -s 5
   ```

## Tips
- Gunakan pilihan `-h` untuk mendapatkan paparan yang lebih mudah difahami, terutamanya jika anda tidak biasa dengan unit memori.
- Perintah `free` boleh digabungkan dengan perintah lain menggunakan `watch` untuk memantau penggunaan memori secara berterusan:
   ```bash
   watch free -h
   ```
- Sentiasa periksa penggunaan memori sebelum menjalankan aplikasi berat untuk memastikan sistem anda mempunyai sumber yang mencukupi.