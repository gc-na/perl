# [Sistem Operasi] C Shell (csh) tcpdump Penggunaan: Menangkap dan menganalisis paket rangkaian

## Overview
Perintah `tcpdump` adalah alat yang digunakan untuk menangkap dan menganalisis paket data yang melalui rangkaian. Ia sangat berguna untuk penyelesaian masalah rangkaian dan pemantauan trafik.

## Usage
Sintaks asas untuk menggunakan `tcpdump` adalah seperti berikut:
```
tcpdump [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan umum untuk `tcpdump` beserta penjelasan ringkas:

- `-i <interface>`: Menentukan antaramuka rangkaian yang ingin dipantau.
- `-n`: Mengelakkan penukaran alamat IP kepada nama host.
- `-v`: Menunjukkan maklumat yang lebih terperinci.
- `-c <count>`: Menangkap hanya sejumlah paket yang ditentukan.
- `-w <file>`: Menyimpan hasil tangkapan ke dalam fail.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `tcpdump`:

1. Menangkap semua paket pada antaramuka rangkaian:
   ```bash
   tcpdump -i eth0
   ```

2. Menangkap paket tanpa menukarkan alamat IP kepada nama host:
   ```bash
   tcpdump -i eth0 -n
   ```

3. Menangkap hanya 10 paket:
   ```bash
   tcpdump -i eth0 -c 10
   ```

4. Menyimpan hasil tangkapan ke dalam fail:
   ```bash
   tcpdump -i eth0 -w output.pcap
   ```

5. Menangkap paket HTTP:
   ```bash
   tcpdump -i eth0 port 80
   ```

## Tips
- Sentiasa gunakan pilihan `-n` untuk mempercepatkan proses tangkapan, terutama pada rangkaian yang besar.
- Gunakan pilihan `-v` atau `-vv` untuk mendapatkan maklumat yang lebih terperinci tentang paket yang ditangkap.
- Simpan hasil tangkapan ke dalam fail menggunakan pilihan `-w` untuk analisis lebih lanjut menggunakan alat lain seperti Wireshark.