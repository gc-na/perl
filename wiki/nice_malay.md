# [Linux] C Shell (csh) nice: Mengubah prioriti proses

## Overview
Perintah `nice` dalam C Shell (csh) digunakan untuk mengubah prioriti proses yang sedang dijalankan. Dengan menggunakan `nice`, pengguna dapat menentukan berapa banyak sumber daya CPU yang akan diberikan kepada proses tertentu, yang membolehkan pengurusan beban kerja yang lebih baik dalam sistem.

## Usage
Sintaks asas untuk menggunakan perintah `nice` adalah seperti berikut:

```
nice [options] [arguments]
```

## Common Options
- `-n` : Menentukan nilai nice yang ingin digunakan. Nilai ini boleh antara -20 (prioriti tertinggi) hingga 19 (prioriti terendah).
- `-h` : Menunjukkan bantuan untuk perintah nice.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `nice`:

1. Menjalankan proses dengan prioriti biasa:
   ```csh
   nice myscript.sh
   ```

2. Menjalankan proses dengan prioriti lebih rendah:
   ```csh
   nice -n 10 myscript.sh
   ```

3. Menjalankan proses dengan prioriti lebih tinggi:
   ```csh
   nice -n -5 myscript.sh
   ```

4. Menjalankan perintah `top` dengan prioriti rendah:
   ```csh
   nice -n 19 top
   ```

## Tips
- Gunakan `nice` untuk menjalankan proses yang tidak memerlukan banyak sumber daya CPU agar tidak mengganggu proses lain yang lebih penting.
- Sentiasa semak nilai nice semasa menjalankan proses untuk memastikan sistem berfungsi dengan baik.
- Jika anda tidak mempunyai hak istimewa untuk menurunkan prioriti proses, anda mungkin perlu menggunakan `sudo` untuk menaikkan prioriti.