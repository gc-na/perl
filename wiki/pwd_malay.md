# [Sistem Operasi] C Shell (csh) pwd <Kegunaan>: Menunjukkan direktori kerja semasa

## Overview
Perintah `pwd` (print working directory) digunakan dalam C Shell untuk menunjukkan direktori kerja semasa pengguna. Ia memberikan laluan penuh kepada lokasi di mana pengguna berada dalam sistem fail.

## Usage
Berikut adalah sintaks asas untuk perintah `pwd`:

```
pwd [options] [arguments]
```

## Common Options
- `-L`: Menunjukkan laluan simbolik semasa.
- `-P`: Menunjukkan laluan fizikal, mengabaikan sebarang pautan simbolik.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `pwd`:

1. **Menunjukkan direktori kerja semasa:**
   ```
   pwd
   ```

2. **Menunjukkan laluan fizikal:**
   ```
   pwd -P
   ```

3. **Menunjukkan laluan simbolik:**
   ```
   pwd -L
   ```

## Tips
- Gunakan `pwd` sebelum menjalankan perintah lain untuk memastikan anda berada di direktori yang betul.
- Jika anda menggunakan pautan simbolik, pertimbangkan untuk menggunakan pilihan `-P` untuk mendapatkan laluan fizikal yang tepat.