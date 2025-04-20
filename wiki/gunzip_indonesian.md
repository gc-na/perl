# [Sistem Operasi] C Shell (csh) gunzip Penggunaan: Mengompres dan mengekstrak file gzip

## Overview
Perintah `gunzip` digunakan untuk mengekstrak file yang dikompresi dengan algoritma gzip. Dengan menggunakan `gunzip`, Anda dapat mengembalikan file ke bentuk aslinya setelah dikompresi.

## Usage
Berikut adalah sintaks dasar dari perintah `gunzip`:

```
gunzip [options] [arguments]
```

## Common Options
- `-c`: Menampilkan hasil dekompresi ke output standar (stdout) tanpa menghapus file asli.
- `-f`: Memaksa dekompresi, bahkan jika file sudah ada.
- `-k`: Menyimpan file asli setelah dekompresi.
- `-r`: Mencari dan mendekompresi file dalam direktori secara rekursif.

## Common Examples
Berikut adalah beberapa contoh penggunaan `gunzip`:

1. **Mendekompresi file gzip sederhana:**
   ```csh
   gunzip file.txt.gz
   ```

2. **Menampilkan hasil dekompresi tanpa menghapus file asli:**
   ```csh
   gunzip -c file.txt.gz
   ```

3. **Mendekompresi file dan menyimpan file asli:**
   ```csh
   gunzip -k file.txt.gz
   ```

4. **Mendekompresi semua file gzip dalam direktori:**
   ```csh
   gunzip -r *.gz
   ```

## Tips
- Selalu periksa ruang disk Anda sebelum mendekompresi file besar untuk menghindari masalah kehabisan ruang.
- Gunakan opsi `-k` jika Anda ingin menjaga file asli setelah dekompresi.
- Jika Anda tidak yakin tentang file yang akan didekompresi, gunakan opsi `-c` untuk melihat isi file tanpa menghapusnya.