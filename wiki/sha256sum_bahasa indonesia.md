# [Sistem Operasi] C Shell (csh) sha256sum: Menghitung checksum SHA-256

## Overview
Perintah `sha256sum` digunakan untuk menghasilkan nilai checksum SHA-256 dari file. Nilai checksum ini berguna untuk memverifikasi integritas file, memastikan bahwa file tidak telah diubah atau rusak.

## Usage
Berikut adalah sintaks dasar dari perintah `sha256sum`:

```csh
sha256sum [options] [arguments]
```

## Common Options
- `-b`: Menghitung checksum untuk file biner.
- `-c`: Memeriksa checksum dari file yang telah dihitung sebelumnya.
- `-o <file>`: Menyimpan output ke dalam file yang ditentukan.
- `--quiet`: Menonaktifkan output yang tidak perlu saat memeriksa checksum.

## Common Examples
Berikut adalah beberapa contoh penggunaan `sha256sum`:

1. Menghitung checksum SHA-256 dari sebuah file:
    ```csh
    sha256sum file.txt
    ```

2. Menghitung checksum untuk file biner:
    ```csh
    sha256sum -b file.bin
    ```

3. Memeriksa checksum dari file yang telah dihitung sebelumnya:
    ```csh
    sha256sum -c checksum.txt
    ```

4. Menyimpan output checksum ke dalam file:
    ```csh
    sha256sum file.txt -o output.txt
    ```

## Tips
- Selalu simpan checksum yang dihasilkan untuk referensi di masa mendatang, terutama untuk file penting.
- Gunakan opsi `-c` untuk memverifikasi file yang diunduh dari internet agar memastikan keasliannya.
- Jika bekerja dengan banyak file, pertimbangkan untuk menggunakan wildcard (`*`) untuk menghitung checksum secara massal. Misalnya:
    ```csh
    sha256sum *.txt
    ```