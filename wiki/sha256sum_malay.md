# [Sistem Operasi] C Shell (csh) sha256sum: Mengira checksum SHA-256

## Overview
Perintah `sha256sum` digunakan untuk mengira dan memaparkan checksum SHA-256 bagi fail. Ini berguna untuk memastikan integriti fail dengan membandingkan checksum yang dihasilkan dengan checksum yang diketahui.

## Usage
Berikut adalah sintaks asas bagi perintah `sha256sum`:

```csh
sha256sum [options] [arguments]
```

## Common Options
- `-b` : Mengira checksum bagi fail dalam format binari.
- `-c` : Menggunakan fail checksum untuk mengesahkan fail.
- `-o` : Menentukan fail output untuk menyimpan hasil.
- `--help` : Memaparkan bantuan mengenai penggunaan perintah.

## Common Examples
Berikut adalah beberapa contoh penggunaan `sha256sum`:

1. Mengira checksum bagi fail:
   ```csh
   sha256sum fail.txt
   ```

2. Menyimpan checksum ke dalam fail:
   ```csh
   sha256sum fail.txt > checksum.txt
   ```

3. Mengesahkan fail menggunakan fail checksum:
   ```csh
   sha256sum -c checksum.txt
   ```

4. Mengira checksum bagi beberapa fail sekaligus:
   ```csh
   sha256sum fail1.txt fail2.txt
   ```

## Tips
- Sentiasa simpan fail checksum yang dihasilkan untuk pengesahan masa depan.
- Gunakan pilihan `-c` untuk mengesahkan fail dengan cepat dan mudah.
- Pastikan anda mempunyai akses kepada fail asal untuk membandingkan checksum dengan tepat.