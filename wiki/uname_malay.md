# [Linux] C Shell (csh) uname Penggunaan: Menunjukkan maklumat sistem

## Overview
Perintah `uname` dalam C Shell (csh) digunakan untuk mendapatkan maklumat mengenai sistem operasi yang sedang digunakan. Ia memberikan informasi seperti nama kernel, nama mesin, dan versi sistem.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `uname`:

```
uname [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan umum untuk perintah `uname`:

- `-a`: Menunjukkan semua maklumat sistem.
- `-s`: Menunjukkan nama kernel.
- `-n`: Menunjukkan nama mesin.
- `-r`: Menunjukkan versi kernel.
- `-v`: Menunjukkan maklumat versi tambahan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `uname`:

1. Menunjukkan semua maklumat sistem:
   ```csh
   uname -a
   ```

2. Menunjukkan nama kernel:
   ```csh
   uname -s
   ```

3. Menunjukkan versi kernel:
   ```csh
   uname -r
   ```

4. Menunjukkan nama mesin:
   ```csh
   uname -n
   ```

## Tips
- Gunakan `uname -a` untuk mendapatkan gambaran keseluruhan sistem dengan cepat.
- Pilihan `-v` dapat memberikan maklumat tambahan yang berguna tentang versi kernel.
- Pastikan untuk menjalankan perintah ini dalam terminal untuk mendapatkan maklumat yang tepat mengenai sistem anda.