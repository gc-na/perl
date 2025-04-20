# [Sistem Operasi] C Shell (csh) nohup: Menjalankan proses tanpa interupsi

## Overview
Perintah `nohup` digunakan untuk menjalankan proses di latar belakang dan memastikan bahwa proses tersebut tidak terhenti meskipun sesi terminal ditutup. Ini sangat berguna ketika Anda ingin menjalankan skrip atau aplikasi yang memerlukan waktu lama tanpa harus tetap terhubung ke terminal.

## Usage
Sintaks dasar dari perintah `nohup` adalah sebagai berikut:

```
nohup [options] [arguments]
```

## Common Options
- `&` : Menjalankan proses di latar belakang.
- `-h` : Menampilkan bantuan tentang penggunaan `nohup`.
- `-p` : Menghentikan proses yang sedang berjalan.

## Common Examples
Berikut adalah beberapa contoh penggunaan `nohup`:

1. Menjalankan skrip di latar belakang:
   ```csh
   nohup ./myscript.sh &
   ```

2. Menjalankan perintah `ping` dan menyimpan output ke file:
   ```csh
   nohup ping google.com > output.txt &
   ```

3. Menjalankan aplikasi Java di latar belakang:
   ```csh
   nohup java -jar myapp.jar &
   ```

4. Menjalankan perintah dengan output yang diarahkan ke `/dev/null`:
   ```csh
   nohup mylongrunningcommand > /dev/null 2>&1 &
   ```

## Tips
- Selalu arahkan output ke file atau `/dev/null` untuk menghindari penumpukan output di terminal.
- Gunakan `jobs` untuk memeriksa proses yang berjalan di latar belakang.
- Pastikan untuk memeriksa file `nohup.out` (default) untuk melihat output dari proses yang dijalankan dengan `nohup`.