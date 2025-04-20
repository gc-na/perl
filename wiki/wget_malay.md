# [Sistem Operasi] C Shell (csh) wget Penggunaan: Memuat turun fail dari web

## Overview
Perintah `wget` adalah alat yang digunakan untuk memuat turun fail dari internet. Ia menyokong pelbagai protokol seperti HTTP, HTTPS, dan FTP, menjadikannya sangat berguna untuk mendapatkan data dari pelbagai sumber dalam talian.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `wget`:

```
wget [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa yang boleh digunakan dengan `wget`:

- `-O [file]`: Menyimpan fail yang dimuat turun dengan nama yang ditentukan.
- `-q`: Mengaktifkan mod senyap, yang mengurangkan output ke skrin.
- `-r`: Memuat turun secara rekursif, termasuk semua fail yang berkaitan.
- `-c`: Menyambung semula muat turun yang terputus.
- `--limit-rate=[rate]`: Menghadkan kelajuan muat turun.

## Common Examples
Berikut adalah beberapa contoh praktikal menggunakan `wget`:

1. Memuat turun fail dari URL tertentu:
   ```bash
   wget http://example.com/file.zip
   ```

2. Menyimpan fail dengan nama yang berbeza:
   ```bash
   wget -O myfile.zip http://example.com/file.zip
   ```

3. Memuat turun secara rekursif:
   ```bash
   wget -r http://example.com/directory/
   ```

4. Menyambung semula muat turun yang terputus:
   ```bash
   wget -c http://example.com/largefile.zip
   ```

5. Menghadkan kelajuan muat turun:
   ```bash
   wget --limit-rate=200k http://example.com/file.zip
   ```

## Tips
- Sentiasa semak URL sebelum memuat turun untuk memastikan ia sah.
- Gunakan pilihan `-q` jika anda tidak mahu output yang banyak di skrin.
- Untuk muat turun yang besar, pertimbangkan untuk menggunakan pilihan `-c` untuk mengelakkan kehilangan kemajuan jika sambungan terputus.