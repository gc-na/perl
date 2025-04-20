# [Sistem Operasi] C Shell (csh) pr: Mencetak file dengan format yang teratur

## Overview
Perintah `pr` dalam C Shell (csh) digunakan untuk memformat dan mencetak isi file teks. Perintah ini sangat berguna untuk menyiapkan dokumen agar lebih mudah dibaca, terutama saat mencetak atau menampilkan di layar.

## Usage
Berikut adalah sintaks dasar dari perintah `pr`:

```
pr [options] [arguments]
```

## Common Options
- `-l [number]` : Menentukan jumlah baris per halaman.
- `-w [number]` : Menentukan lebar halaman dalam karakter.
- `-t` : Mengabaikan header dan footer saat mencetak.
- `-s` : Mengatur jarak antar kolom.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `pr`:

1. Mencetak file dengan format default:
   ```csh
   pr file.txt
   ```

2. Mencetak file dengan 50 baris per halaman:
   ```csh
   pr -l 50 file.txt
   ```

3. Mencetak file dengan lebar halaman 80 karakter:
   ```csh
   pr -w 80 file.txt
   ```

4. Mencetak beberapa file sekaligus:
   ```csh
   pr file1.txt file2.txt
   ```

5. Mencetak file tanpa header dan footer:
   ```csh
   pr -t file.txt
   ```

## Tips
- Selalu periksa format file sebelum mencetak untuk memastikan hasil yang diinginkan.
- Gunakan opsi `-s` untuk mengatur jarak antar kolom jika mencetak beberapa file agar lebih rapi.
- Cobalah mencetak ke file lain dengan menggunakan redirection (`>`) jika ingin menyimpan hasil format tanpa mencetak langsung ke printer.