# [Sistem Operasi] C Shell (csh) htop: Menampilkan proses sistem secara interaktif

## Overview
Perintah `htop` adalah alat pemantauan sistem yang interaktif dan berbasis teks. Ini memberikan tampilan real-time dari proses yang sedang berjalan di sistem, memungkinkan pengguna untuk melihat penggunaan CPU, memori, dan informasi lainnya dengan cara yang lebih mudah dibandingkan dengan perintah `top`.

## Usage
Berikut adalah sintaks dasar untuk menggunakan perintah `htop`:

```bash
htop [options] [arguments]
```

## Common Options
- `-h`, `--help`: Menampilkan bantuan dan informasi tentang penggunaan `htop`.
- `-s`, `--sort`: Mengurutkan proses berdasarkan kolom tertentu seperti penggunaan CPU atau memori.
- `-p`, `--pid`: Menampilkan hanya proses dengan ID tertentu.
- `-u`, `--user`: Menampilkan hanya proses yang dimiliki oleh pengguna tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan `htop`:

1. Menjalankan `htop` untuk melihat semua proses:
   ```bash
   htop
   ```

2. Menampilkan proses yang diurutkan berdasarkan penggunaan CPU:
   ```bash
   htop -s PERCENT_CPU
   ```

3. Menampilkan hanya proses untuk pengguna tertentu:
   ```bash
   htop -u username
   ```

4. Menampilkan proses dengan ID tertentu:
   ```bash
   htop -p 1234
   ```

## Tips
- Gunakan tombol panah untuk menavigasi antar proses dan tekan `F9` untuk mengakhiri proses yang dipilih.
- Anda dapat menggunakan `F2` untuk mengakses menu pengaturan dan menyesuaikan tampilan `htop` sesuai kebutuhan.
- Untuk memperbarui tampilan secara manual, tekan `F5` untuk mengubah tampilan menjadi pohon proses.