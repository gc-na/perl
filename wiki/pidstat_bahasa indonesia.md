# [Linux] C Shell (csh) pidstat: Mengawasi Statistik Proses

## Overview
Perintah `pidstat` digunakan untuk mengawasi statistik penggunaan sumber daya sistem oleh proses yang berjalan. Ini memberikan informasi tentang penggunaan CPU, memori, dan I/O untuk proses tertentu, sehingga membantu dalam pemantauan dan analisis performa sistem.

## Usage
Sintaks dasar dari perintah `pidstat` adalah sebagai berikut:

```
pidstat [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `pidstat`:

- `-h`: Menampilkan output dalam format yang lebih mudah dibaca.
- `-r`: Menampilkan statistik penggunaan memori.
- `-u`: Menampilkan statistik penggunaan CPU.
- `-p [pid]`: Menentukan ID proses tertentu untuk dipantau.
- `-t`: Menampilkan statistik untuk semua thread dalam proses.

## Common Examples
Berikut adalah beberapa contoh penggunaan `pidstat`:

1. **Menampilkan statistik penggunaan CPU untuk semua proses:**
   ```bash
   pidstat -u
   ```

2. **Menampilkan statistik penggunaan memori untuk proses tertentu dengan ID 1234:**
   ```bash
   pidstat -r -p 1234
   ```

3. **Menampilkan statistik untuk semua thread dalam proses dengan ID 5678:**
   ```bash
   pidstat -t -p 5678
   ```

4. **Menampilkan statistik penggunaan CPU setiap 5 detik:**
   ```bash
   pidstat -u 5
   ```

## Tips
- Gunakan opsi `-h` untuk membuat output lebih mudah dibaca, terutama saat memantau banyak proses.
- Kombinasikan opsi `-r` dan `-u` untuk mendapatkan gambaran lengkap tentang penggunaan sumber daya oleh proses.
- Pertimbangkan untuk menjalankan `pidstat` dalam skrip pemantauan untuk analisis jangka panjang.