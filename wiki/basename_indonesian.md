# [Sistem Operasi] C Shell (csh) basename Penggunaan: Mengambil nama file tanpa path

## Overview
Perintah `basename` digunakan untuk mengambil nama file dari sebuah path lengkap, menghapus direktori dan ekstensi file jika diinginkan. Ini sangat berguna ketika Anda hanya ingin menampilkan nama file tanpa informasi tambahan dari path.

## Usage
Berikut adalah sintaks dasar dari perintah `basename`:

```
basename [options] [arguments]
```

## Common Options
- `-s, --suffix`: Menghapus sufiks tertentu dari nama file.
- `-a, --multiple`: Mengambil nama dari beberapa file sekaligus.

## Common Examples

1. **Mengambil nama file dari path lengkap:**
   ```csh
   basename /home/user/documents/file.txt
   ```
   Output: `file.txt`

2. **Menghapus ekstensi dari nama file:**
   ```csh
   basename /home/user/documents/file.txt .txt
   ```
   Output: `file`

3. **Mengambil nama dari beberapa file:**
   ```csh
   basename -a /home/user/documents/file1.txt /home/user/documents/file2.txt
   ```
   Output:
   ```
   file1.txt
   file2.txt
   ```

4. **Menghapus sufiks tertentu:**
   ```csh
   basename /home/user/documents/report.pdf .pdf
   ```
   Output: `report`

## Tips
- Gunakan `basename` ketika Anda perlu mengekstrak nama file dari path dalam skrip shell untuk memudahkan pemrosesan file.
- Pertimbangkan untuk menggunakan opsi `-a` jika Anda bekerja dengan beberapa file untuk menghemat waktu dan usaha.
- Pastikan untuk menyertakan sufiks yang benar saat menggunakan opsi `-s` agar hasil yang diinginkan sesuai.