# [Sistem Operasi] C Shell (csh) dstat Penggunaan: Memantau sumber sistem secara real-time

## Overview
Perintah `dstat` adalah alat yang digunakan untuk memantau sumber sistem secara real-time. Ia menggabungkan beberapa alat pemantauan yang berbeza seperti `vmstat`, `iostat`, dan `netstat` ke dalam satu perintah yang mudah digunakan. Dengan `dstat`, pengguna dapat melihat pelbagai statistik sistem seperti penggunaan CPU, memori, dan I/O disk dalam satu paparan.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `dstat`:

```
dstat [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `dstat` beserta penjelasan ringkas:

- `-c`: Paparkan statistik penggunaan CPU.
- `-d`: Paparkan statistik I/O disk.
- `-n`: Paparkan statistik rangkaian.
- `-m`: Paparkan statistik penggunaan memori.
- `--help`: Tunjukkan bantuan dan pilihan yang tersedia.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `dstat`:

1. **Paparkan penggunaan CPU dan memori:**
   ```bash
   dstat -c -m
   ```

2. **Paparkan statistik I/O disk dan rangkaian:**
   ```bash
   dstat -d -n
   ```

3. **Paparkan semua statistik dengan interval 1 saat:**
   ```bash
   dstat -t --full --time
   ```

4. **Paparkan statistik dengan output dalam format CSV:**
   ```bash
   dstat --output output.csv
   ```

## Tips
- Gunakan pilihan `-t` untuk menambah cap waktu pada output, yang membantu dalam analisis data.
- Jalankan `dstat` dalam terminal yang berasingan agar anda dapat memantau sumber sistem tanpa mengganggu proses lain.
- Eksperimen dengan pelbagai pilihan untuk mendapatkan pandangan yang lebih mendalam tentang prestasi sistem anda.