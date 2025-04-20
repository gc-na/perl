# [Sistem Operasi] C Shell (csh) dstat Penggunaan: Memantau sumber daya sistem secara real-time

## Overview
Perintah `dstat` adalah alat yang berguna untuk memantau penggunaan sumber daya sistem secara real-time. Dengan `dstat`, pengguna dapat melihat berbagai statistik seperti penggunaan CPU, memori, disk, dan jaringan dalam satu tampilan yang mudah dibaca.

## Usage
Sintaks dasar untuk menggunakan perintah `dstat` adalah sebagai berikut:

```bash
dstat [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `dstat`:

- `-c`: Menampilkan penggunaan CPU.
- `-d`: Menampilkan statistik disk.
- `-n`: Menampilkan statistik jaringan.
- `-m`: Menampilkan penggunaan memori.
- `-t`: Menampilkan timestamp.

## Common Examples
Berikut adalah beberapa contoh penggunaan `dstat`:

1. Menampilkan penggunaan CPU dan memori:
   ```bash
   dstat -c -m
   ```

2. Menampilkan statistik disk dan jaringan:
   ```bash
   dstat -d -n
   ```

3. Menampilkan semua statistik dengan timestamp:
   ```bash
   dstat -t -c -d -n -m
   ```

4. Menampilkan statistik setiap 2 detik:
   ```bash
   dstat 2
   ```

## Tips
- Gunakan opsi `-t` untuk menambahkan timestamp pada output agar lebih mudah melacak waktu.
- Kombinasikan beberapa opsi untuk mendapatkan gambaran lengkap tentang kinerja sistem Anda.
- Pertimbangkan untuk menyimpan output ke file dengan menggunakan redirection, misalnya `dstat -c -d > output.txt`, agar dapat dianalisis kemudian.