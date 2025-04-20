# [Sistem Pengendalian] C Shell (csh) nohup: Menjalankan proses tanpa gangguan

## Overview
Perintah `nohup` dalam C Shell digunakan untuk menjalankan proses yang tidak akan terhenti walaupun sesi terminal ditutup. Ini berguna untuk menjalankan skrip atau aplikasi yang memerlukan waktu lama tanpa perlu bimbang tentang kehilangan kemajuan jika anda log keluar.

## Usage
Sintaks asas untuk perintah `nohup` adalah seperti berikut:

```
nohup [options] [arguments]
```

## Common Options
- `&` : Menjalankan proses di latar belakang.
- `-h` : Menunjukkan bantuan mengenai penggunaan `nohup`.
- `-v` : Menunjukkan versi `nohup`.

## Common Examples
Berikut adalah beberapa contoh penggunaan `nohup`:

1. Menjalankan skrip shell di latar belakang:
   ```csh
   nohup ./myscript.sh &
   ```

2. Menjalankan perintah `ping` dan menyimpan output ke dalam fail:
   ```csh
   nohup ping google.com > output.txt &
   ```

3. Menjalankan aplikasi Python tanpa gangguan:
   ```csh
   nohup python myapp.py &
   ```

## Tips
- Sentiasa gunakan `&` untuk menjalankan proses di latar belakang jika anda ingin terus menggunakan terminal.
- Semak fail `nohup.out` untuk melihat output proses yang dijalankan jika tidak ditentukan output lain.
- Gunakan `disown` selepas menjalankan `nohup` untuk memastikan proses tidak terikat dengan sesi terminal.