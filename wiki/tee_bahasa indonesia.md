# [Sistem Operasi] C Shell (csh) tee Penggunaan: Menyalin dan Menampilkan Output

## Overview
Perintah `tee` dalam C Shell (csh) digunakan untuk membaca dari input standar dan menulis ke output standar serta satu atau lebih file. Ini berguna untuk melihat output dari suatu perintah sambil juga menyimpannya ke dalam file.

## Usage
Berikut adalah sintaks dasar dari perintah `tee`:

```csh
tee [options] [arguments]
```

## Common Options
- `-a` : Menambahkan output ke file yang sudah ada, bukan menimpanya.
- `-i` : Mengabaikan sinyal interrupt (SIGINT).

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `tee`:

1. Menyimpan output dari perintah `ls` ke dalam file `daftar.txt`:
   ```csh
   ls | tee daftar.txt
   ```

2. Menyimpan output sambil menampilkan di layar dan menambahkan ke file `log.txt`:
   ```csh
   echo "Menjalankan skrip..." | tee -a log.txt
   ```

3. Menggunakan `tee` untuk menyimpan hasil dari perintah `grep`:
   ```csh
   cat file.txt | grep "pola" | tee hasil.txt
   ```

## Tips
- Gunakan opsi `-a` jika Anda ingin menambahkan output ke file tanpa menghapus isi sebelumnya.
- Pastikan Anda memiliki izin untuk menulis ke file yang dituju agar tidak terjadi error.
- `tee` sangat berguna dalam skrip untuk mencatat log sambil tetap menampilkan output di terminal.