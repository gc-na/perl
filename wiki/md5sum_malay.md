# [Sistem Operasi] C Shell (csh) md5sum Penggunaan: Mengira checksum MD5

## Overview
Perintah `md5sum` digunakan untuk mengira dan memaparkan checksum MD5 bagi fail. Ia sering digunakan untuk memastikan integriti fail dengan membandingkan checksum yang dihasilkan dengan checksum asal.

## Usage
Sintaks asas untuk perintah `md5sum` adalah seperti berikut:

```
md5sum [options] [arguments]
```

## Common Options
- `-b` : Mengira checksum untuk fail binari.
- `-c` : Menggunakan fail yang mengandungi checksum untuk mengesahkan fail.
- `-t` : Mengira checksum untuk fail teks.

## Common Examples
Berikut adalah beberapa contoh penggunaan `md5sum`:

1. Mengira checksum MD5 untuk fail:
   ```bash
   md5sum nama_fail.txt
   ```

2. Menyimpan checksum ke dalam fail:
   ```bash
   md5sum nama_fail.txt > checksum.md5
   ```

3. Mengesahkan fail menggunakan fail checksum:
   ```bash
   md5sum -c checksum.md5
   ```

4. Mengira checksum untuk fail binari:
   ```bash
   md5sum -b nama_fail.bin
   ```

## Tips
- Sentiasa simpan checksum asal selepas mengira untuk tujuan pengesahan di masa hadapan.
- Gunakan `-c` untuk memudahkan pengesahan banyak fail sekaligus.
- Pastikan anda menggunakan `md5sum` pada fail yang tidak diubah untuk mendapatkan hasil yang tepat.