# [Sistem Operasi] C Shell (csh) nohup: Menjalankan proses tanpa terganggu

## Overview
Perintah `nohup` (no hang up) digunakan untuk menjalankan proses di latar belakang yang tidak akan terhenti meskipun sesi terminal ditutup. Ini sangat berguna untuk menjalankan skrip atau aplikasi yang memerlukan waktu lama tanpa harus tetap terhubung ke terminal.

## Usage
Berikut adalah sintaks dasar dari perintah `nohup`:

```
nohup [options] [arguments]
```

## Common Options
- `&` : Menjalankan proses di latar belakang.
- `-o` : Menentukan file output untuk log.
- `-h` : Menampilkan bantuan tentang penggunaan `nohup`.

## Common Examples
Berikut adalah beberapa contoh penggunaan `nohup`:

1. Menjalankan skrip di latar belakang:
   ```csh
   nohup ./myscript.sh &
   ```

2. Menjalankan perintah dan menyimpan output ke file:
   ```csh
   nohup mylongrunningcommand > output.log &
   ```

3. Menjalankan perintah dengan output error terpisah:
   ```csh
   nohup mycommand > output.log 2> error.log &
   ```

4. Menjalankan perintah tanpa output ke terminal:
   ```csh
   nohup mycommand >/dev/null 2>&1 &
   ```

## Tips
- Selalu periksa file output untuk memastikan proses berjalan dengan baik.
- Gunakan `jobs` untuk memeriksa proses yang berjalan di latar belakang.
- Pastikan untuk menambahkan `&` di akhir perintah untuk menjalankannya di latar belakang.