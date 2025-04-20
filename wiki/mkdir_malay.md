# [Linux] C Shell (csh) mkdir Penggunaan: Membuat direktori baru

## Overview
Perintah `mkdir` dalam C Shell (csh) digunakan untuk membuat direktori baru dalam sistem fail. Ini adalah alat yang penting untuk mengorganisir fail dan folder dalam struktur yang teratur.

## Usage
Sintaks asas untuk perintah `mkdir` adalah seperti berikut:

```
mkdir [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan umum untuk `mkdir` beserta penjelasan ringkas:

- `-p`: Membuat direktori induk secara automatik jika ia tidak wujud.
- `-m`: Menetapkan hak akses untuk direktori yang baru dibuat.
- `-v`: Menunjukkan maklumat tentang direktori yang sedang dibuat.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `mkdir`:

1. **Membuat direktori baru:**
   ```csh
   mkdir direktori_baru
   ```

2. **Membuat direktori dengan direktori induk:**
   ```csh
   mkdir -p /home/user/direktori_baru/subdirektori
   ```

3. **Membuat direktori dengan hak akses tertentu:**
   ```csh
   mkdir -m 755 direktori_hak_akses
   ```

4. **Menunjukkan maklumat semasa membuat direktori:**
   ```csh
   mkdir -v direktori_info
   ```

## Tips
- Sentiasa gunakan pilihan `-p` jika anda tidak pasti sama ada direktori induk wujud untuk mengelakkan ralat.
- Periksa hak akses yang diperlukan sebelum menggunakan pilihan `-m` untuk memastikan direktori boleh diakses oleh pengguna yang sesuai.
- Gunakan pilihan `-v` untuk mendapatkan maklumat tambahan semasa membuat direktori, terutama dalam skrip automasi.