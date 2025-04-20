# [Linux] C Shell (csh) tar Penggunaan: Mengarkib dan mengekstrak fail

## Overview
Perintah `tar` digunakan untuk mengarkib dan mengekstrak fail dalam sistem operasi Unix dan Linux. Ia membolehkan pengguna mengumpulkan beberapa fail menjadi satu fail arkib, memudahkan pemindahan dan penyimpanan.

## Usage
Sintaks asas untuk perintah `tar` adalah seperti berikut:

```csh
tar [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan umum untuk perintah `tar`:

- `-c`: Membuat arkib baru.
- `-x`: Mengekstrak fail dari arkib.
- `-f`: Menentukan nama fail arkib.
- `-v`: Menunjukkan proses secara terperinci (verbose).
- `-z`: Menggunakan gzip untuk memampatkan arkib.
- `-j`: Menggunakan bzip2 untuk memampatkan arkib.

## Common Examples

1. **Membuat arkib baru:**
   Untuk mengarkibkan fail `file1.txt` dan `file2.txt` ke dalam `archive.tar`:
   ```csh
   tar -cvf archive.tar file1.txt file2.txt
   ```

2. **Mengekstrak arkib:**
   Untuk mengekstrak semua fail dari `archive.tar`:
   ```csh
   tar -xvf archive.tar
   ```

3. **Membuat arkib mampat:**
   Untuk mengarkib dan memampatkan fail menggunakan gzip:
   ```csh
   tar -czvf archive.tar.gz file1.txt file2.txt
   ```

4. **Mengekstrak arkib mampat:**
   Untuk mengekstrak fail dari `archive.tar.gz`:
   ```csh
   tar -xzvf archive.tar.gz
   ```

## Tips
- Sentiasa gunakan pilihan `-v` untuk melihat proses pengarkiban atau pengekstrakan, ini membantu memastikan semua fail diproses dengan betul.
- Pastikan anda mempunyai hak akses yang mencukupi untuk fail yang ingin diarkibkan atau diekstrak.
- Gunakan pilihan `-f` dengan teliti untuk memastikan anda tidak menimpa fail arkib yang sedia ada tanpa disedari.