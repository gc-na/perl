# [Linux] C Shell (csh) sort Penggunaan: Mengatur baris dalam fail teks

## Overview
Perintah `sort` digunakan untuk mengatur baris dalam fail teks. Ia menyusun baris berdasarkan urutan abjad atau numerik, menjadikannya lebih mudah untuk dibaca dan dianalisis.

## Usage
Sintaks asas untuk perintah `sort` adalah seperti berikut:

```csh
sort [options] [arguments]
```

## Common Options
- `-r`: Mengatur dalam urutan terbalik.
- `-n`: Mengatur secara numerik.
- `-k`: Menentukan kunci pengurutan berdasarkan kolom tertentu.
- `-u`: Menghapus baris yang duplikat.
- `-o`: Menyimpan output ke dalam fail.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `sort`:

1. Mengatur fail teks secara abjad:
   ```csh
   sort fail.txt
   ```

2. Mengatur fail teks secara terbalik:
   ```csh
   sort -r fail.txt
   ```

3. Mengatur secara numerik:
   ```csh
   sort -n nombor.txt
   ```

4. Mengatur berdasarkan kolom kedua:
   ```csh
   sort -k 2 fail.txt
   ```

5. Menghapus baris yang duplikat dan menyimpan ke dalam fail baru:
   ```csh
   sort -u fail.txt -o fail_unik.txt
   ```

## Tips
- Sentiasa gunakan pilihan `-o` untuk menyimpan hasil pengurutan ke dalam fail baru agar tidak kehilangan data asal.
- Gunakan pilihan `-k` untuk mengatur berdasarkan kolom tertentu, terutamanya dalam fail yang mempunyai beberapa kolom.
- Untuk fail besar, pertimbangkan untuk menggunakan pilihan `-S` untuk menetapkan saiz memori yang digunakan oleh `sort`.