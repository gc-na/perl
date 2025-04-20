# [Sistem Operasi] C Shell (csh) sha512sum: Mengira checksum SHA-512

## Overview
Perintah `sha512sum` digunakan untuk mengira dan memaparkan checksum SHA-512 bagi fail. Ini berguna untuk memastikan integriti data dengan membandingkan checksum yang dihasilkan dengan checksum yang diketahui.

## Usage
Sintaks asas bagi perintah `sha512sum` adalah seperti berikut:

```
sha512sum [options] [arguments]
```

## Common Options
- `-b`: Mengira checksum dalam mod binari.
- `-c`: Memeriksa checksum yang telah disimpan dalam fail.
- `-h`: Memaparkan maklumat bantuan tentang perintah ini.
- `--tag`: Menghasilkan output dalam format tag.

## Common Examples
Berikut adalah beberapa contoh penggunaan `sha512sum`:

1. Mengira checksum bagi satu fail:
   ```bash
   sha512sum fail.txt
   ```

2. Mengira checksum bagi beberapa fail sekaligus:
   ```bash
   sha512sum fail1.txt fail2.txt
   ```

3. Menyimpan checksum ke dalam fail:
   ```bash
   sha512sum fail.txt > checksum.txt
   ```

4. Memeriksa checksum dari fail yang disimpan:
   ```bash
   sha512sum -c checksum.txt
   ```

## Tips
- Sentiasa simpan checksum yang dihasilkan untuk memudahkan pemeriksaan integriti di masa hadapan.
- Gunakan pilihan `-b` jika anda bekerja dengan fail binari untuk mendapatkan hasil yang tepat.
- Pastikan anda menggunakan versi terbaru `sha512sum` untuk mendapatkan ciri dan keselamatan terkini.