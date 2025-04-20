# [Sistem Operasi] C Shell (csh) iotop Penggunaan: Memantau penggunaan I/O proses

## Overview
Perintah `iotop` digunakan untuk memantau penggunaan input/output (I/O) oleh proses yang sedang berjalan dalam sistem. Ia memberikan gambaran yang jelas tentang proses mana yang menggunakan sumber I/O terbanyak, membantu pengguna dalam mengesan masalah berkaitan dengan prestasi sistem.

## Usage
Sintaks asas untuk menggunakan `iotop` adalah seperti berikut:

```
iotop [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan umum untuk `iotop` beserta penjelasan ringkas:

- `-o` : Hanya menunjukkan proses yang sedang melakukan operasi I/O.
- `-b` : Mod batch, sesuai untuk output ke fail.
- `-n NUM` : Menentukan bilangan iterasi yang akan dijalankan.
- `-d SEC` : Menentukan selang masa (dalam saat) antara setiap kemas kini.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `iotop`:

1. **Menjalankan iotop dalam mod interaktif:**
   ```bash
   iotop
   ```

2. **Menjalankan iotop hanya untuk proses yang melakukan I/O:**
   ```bash
   iotop -o
   ```

3. **Menjalankan iotop dalam mod batch dan menyimpan output ke fail:**
   ```bash
   iotop -b -n 5 > output.txt
   ```

4. **Menjalankan iotop dengan selang masa 2 saat antara kemas kini:**
   ```bash
   iotop -d 2
   ```

## Tips
- Gunakan pilihan `-o` untuk menumpukan perhatian kepada proses yang aktif melakukan I/O, ini akan membantu dalam mendiagnosis masalah prestasi.
- Dalam mod batch, anda boleh mengarahkan output ke fail untuk analisis kemudian.
- Sentiasa jalankan `iotop` dengan hak akses yang sesuai (seperti root) untuk mendapatkan maklumat lengkap tentang semua proses.