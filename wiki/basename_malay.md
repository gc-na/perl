# [Sistem Operasi] C Shell (csh) basename Penggunaan: Mengambil nama fail tanpa laluan

## Overview
Perintah `basename` digunakan untuk mengekstrak nama fail dari laluan penuh. Ia membuang semua direktori dan hanya mengekalkan nama fail itu sendiri, yang berguna dalam skrip dan pengendalian fail.

## Usage
Berikut adalah sintaks asas untuk perintah `basename`:

```
basename [options] [arguments]
```

## Common Options
- `-a`: Mengambil beberapa nama fail dan mengembalikan setiap nama fail tanpa laluan.
- `-s`: Menghilangkan akhiran tertentu dari nama fail.
- `--help`: Menunjukkan bantuan untuk perintah ini.

## Common Examples
Berikut adalah beberapa contoh penggunaan `basename`:

1. Mengambil nama fail dari laluan penuh:
   ```csh
   basename /home/user/documents/file.txt
   ```
   Output: `file.txt`

2. Mengambil nama fail tanpa akhiran tertentu:
   ```csh
   basename /home/user/documents/file.txt .txt
   ```
   Output: `file`

3. Mengambil nama fail dari beberapa laluan:
   ```csh
   basename -a /home/user/documents/file1.txt /home/user/documents/file2.txt
   ```
   Output:
   ```
   file1.txt
   file2.txt
   ```

## Tips
- Gunakan `basename` dalam skrip untuk memudahkan pengendalian fail.
- Sentiasa pastikan laluan yang diberikan adalah betul untuk mengelakkan ralat.
- Anda boleh menggabungkan `basename` dengan perintah lain untuk pemprosesan fail yang lebih kompleks.