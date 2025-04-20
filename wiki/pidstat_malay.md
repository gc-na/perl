# [Sistem Pengendalian] C Shell (csh) pidstat: [memantau statistik proses]

## Overview
Perintah `pidstat` digunakan untuk memantau statistik penggunaan sumber daya oleh proses yang sedang berjalan di sistem. Ia memberikan maklumat terperinci tentang penggunaan CPU, memori, dan sumber lain bagi setiap proses yang ditentukan.

## Usage
Sintaks asas bagi perintah `pidstat` adalah seperti berikut:

```
pidstat [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `pidstat` beserta penjelasan ringkas:

- `-p <pid>`: Menentukan ID proses yang ingin dipantau.
- `-r`: Menunjukkan penggunaan memori untuk proses.
- `-u`: Menunjukkan penggunaan CPU untuk proses.
- `-h`: Mengabaikan baris tajuk dalam output.
- `-t`: Menunjukkan statistik untuk semua thread dalam proses.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `pidstat`:

1. Memantau penggunaan CPU untuk semua proses:
   ```bash
   pidstat -u
   ```

2. Memantau penggunaan memori untuk proses tertentu dengan ID 1234:
   ```bash
   pidstat -r -p 1234
   ```

3. Memantau semua thread dalam proses dengan ID 5678:
   ```bash
   pidstat -t -p 5678
   ```

4. Memantau penggunaan CPU setiap 2 saat:
   ```bash
   pidstat -u 2
   ```

## Tips
- Gunakan pilihan `-h` jika anda tidak memerlukan baris tajuk dalam output untuk menjadikan output lebih ringkas.
- Untuk pemantauan berterusan, pertimbangkan untuk menggunakan `pidstat` dalam skrip untuk mengumpul data secara berkala.
- Sentiasa semak ID proses yang aktif menggunakan perintah `ps` sebelum menggunakan `pidstat` untuk memastikan anda memantau proses yang betul.