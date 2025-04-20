# [Sistem Operasi] C Shell (csh) pr: Mencetak fail teks

## Overview
Perintah `pr` dalam C Shell (csh) digunakan untuk memformat dan mencetak fail teks. Ia membolehkan pengguna mengatur teks dalam bentuk yang lebih mudah dibaca, seperti membahagikan teks kepada beberapa lajur dan menambah tajuk.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `pr`:

```
pr [options] [arguments]
```

## Common Options
- `-h`: Menambah tajuk pada setiap halaman.
- `-l`: Menentukan bilangan baris setiap halaman.
- `-w`: Menentukan lebar halaman.
- `-s`: Menambah ruang kosong antara lajur.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `pr`:

1. **Mencetak fail teks dengan tajuk:**
   ```csh
   pr -h "Tajuk Fail" fail.txt
   ```

2. **Mencetak fail dengan 50 baris setiap halaman:**
   ```csh
   pr -l 50 fail.txt
   ```

3. **Mencetak fail dalam dua lajur:**
   ```csh
   pr -s -2 fail.txt
   ```

4. **Mencetak fail dengan lebar halaman 80:**
   ```csh
   pr -w 80 fail.txt
   ```

## Tips
- Gunakan pilihan `-h` untuk menambah tajuk yang jelas pada dokumen anda.
- Sesuaikan bilangan baris menggunakan pilihan `-l` untuk memastikan teks tidak terlalu padat.
- Eksperimen dengan pilihan lajur untuk meningkatkan keterbacaan dokumen.
- Sentiasa semak hasil cetakan dengan mencetak ke fail terlebih dahulu sebelum mencetak secara fizikal.