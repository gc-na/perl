# [Sistem Operasi] C Shell (csh) comm: Membandingkan dua file baris

## Overview
Perintah `comm` digunakan untuk membandingkan dua file yang diurutkan dan menampilkan baris yang unik untuk masing-masing file serta baris yang sama di antara keduanya. Ini sangat berguna untuk melihat perbedaan dan kesamaan antara dua set data.

## Usage
Berikut adalah sintaks dasar dari perintah `comm`:

```csh
comm [options] [file1] [file2]
```

## Common Options
- `-1`: Mengabaikan kolom pertama (baris yang hanya ada di file1).
- `-2`: Mengabaikan kolom kedua (baris yang hanya ada di file2).
- `-3`: Mengabaikan kolom ketiga (baris yang ada di kedua file).
- `-i`: Mengabaikan perbedaan antara huruf besar dan huruf kecil saat membandingkan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `comm`:

1. Menampilkan semua perbandingan antara dua file:
   ```csh
   comm file1.txt file2.txt
   ```

2. Menampilkan hanya baris yang ada di `file1.txt`:
   ```csh
   comm -13 file1.txt file2.txt
   ```

3. Menampilkan hanya baris yang ada di `file2.txt`:
   ```csh
   comm -12 file1.txt file2.txt
   ```

4. Mengabaikan perbedaan huruf besar dan huruf kecil:
   ```csh
   comm -i file1.txt file2.txt
   ```

## Tips
- Pastikan kedua file yang akan dibandingkan sudah diurutkan, karena `comm` hanya berfungsi dengan file yang terurut.
- Gunakan opsi `-1`, `-2`, atau `-3` untuk fokus pada bagian tertentu dari perbandingan yang Anda butuhkan.
- Jika Anda sering menggunakan `comm`, pertimbangkan untuk membuat alias di `.cshrc` untuk mempercepat akses ke perintah ini.