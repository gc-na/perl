# [Sistem Operasi] C Shell (csh) mpstat Penggunaan: Memantau statistik pemproses

## Overview
Perintah `mpstat` digunakan untuk memantau statistik pemproses pada sistem. Ia memberikan maklumat tentang penggunaan CPU secara keseluruhan dan juga untuk setiap pemproses secara individu.

## Usage
Sintaks asas untuk menggunakan perintah `mpstat` adalah seperti berikut:

```bash
mpstat [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `mpstat` beserta penjelasannya:

- `-P ALL` : Memaparkan statistik untuk semua pemproses.
- `-u` : Menunjukkan penggunaan CPU dalam bentuk peratusan.
- `-h` : Menunjukkan output dalam format yang lebih mudah dibaca.
- `-t` : Menunjukkan cap waktu untuk setiap baris output.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `mpstat`:

1. Menunjukkan statistik pemproses untuk semua pemproses:
   ```bash
   mpstat -P ALL
   ```

2. Menunjukkan penggunaan CPU dalam peratusan:
   ```bash
   mpstat -u
   ```

3. Menunjukkan statistik dengan cap waktu:
   ```bash
   mpstat -t
   ```

4. Menunjukkan statistik pemproses setiap 5 saat:
   ```bash
   mpstat 5
   ```

## Tips
- Gunakan pilihan `-h` untuk mendapatkan output yang lebih mudah dibaca, terutama jika anda bekerja dengan banyak pemproses.
- Perhatikan penggunaan CPU secara berterusan untuk mengesan sebarang masalah prestasi yang mungkin timbul.
- Gabungkan `mpstat` dengan alat pemantauan lain untuk mendapatkan gambaran yang lebih lengkap tentang prestasi sistem anda.