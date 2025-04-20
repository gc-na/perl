# [Sistem Operasi] C Shell (csh) head <Mengambil baris awal dari fail>: Mengambil baris pertama dari fail teks

## Overview
Perintah `head` dalam C Shell digunakan untuk memaparkan beberapa baris pertama dari satu atau lebih fail teks. Ia berguna untuk melihat kandungan awal fail tanpa perlu membuka keseluruhan fail.

## Usage
Sintaks asas untuk perintah `head` adalah seperti berikut:

```
head [options] [arguments]
```

## Common Options
- `-n [number]`: Menentukan bilangan baris yang ingin dipaparkan. Contohnya, `-n 5` akan memaparkan 5 baris pertama.
- `-q`: Tidak memaparkan nama fail sebelum output, berguna apabila memaparkan beberapa fail.
- `-c [number]`: Memaparkan bilangan byte tertentu dari fail.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `head`:

1. Memaparkan 10 baris pertama dari fail `data.txt`:
   ```csh
   head data.txt
   ```

2. Memaparkan 5 baris pertama dari fail `log.txt`:
   ```csh
   head -n 5 log.txt
   ```

3. Memaparkan 20 byte pertama dari fail `file.bin`:
   ```csh
   head -c 20 file.bin
   ```

4. Memaparkan 3 baris pertama dari beberapa fail:
   ```csh
   head -n 3 file1.txt file2.txt
   ```

## Tips
- Gunakan `head` bersama dengan `tail` untuk mendapatkan baris tengah dari fail.
- Jika anda tidak menyatakan bilangan baris, `head` secara default akan memaparkan 10 baris pertama.
- Untuk memeriksa fail besar, `head` adalah cara yang cepat untuk mendapatkan gambaran awal tentang kandungan fail tersebut.