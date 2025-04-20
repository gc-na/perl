# [Sistem Pengendalian] C Shell (csh) host: [mendapatkan maklumat DNS]

## Overview
Perintah `host` digunakan untuk mendapatkan maklumat DNS (Domain Name System) mengenai nama host atau alamat IP. Ia membolehkan pengguna untuk menyemak peta antara nama domain dan alamat IP, serta mendapatkan maklumat lain yang berkaitan dengan DNS.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `host`:

```csh
host [options] [arguments]
```

## Common Options
- `-a`: Menunjukkan semua maklumat yang tersedia untuk nama host.
- `-t type`: Menentukan jenis rekod DNS yang ingin dicari (contoh: A, MX, TXT).
- `-v`: Mengaktifkan mod verbose untuk maklumat tambahan semasa menjalankan perintah.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `host`:

1. **Mendapatkan alamat IP untuk nama host:**
   ```csh
   host example.com
   ```

2. **Mendapatkan maklumat semua rekod untuk nama host:**
   ```csh
   host -a example.com
   ```

3. **Mencari rekod MX (Mail Exchange) untuk domain:**
   ```csh
   host -t MX example.com
   ```

4. **Mendapatkan maklumat DNS dengan mod verbose:**
   ```csh
   host -v example.com
   ```

## Tips
- Sentiasa gunakan pilihan `-v` jika anda memerlukan maklumat tambahan untuk penyelesaian masalah DNS.
- Ketahui jenis rekod DNS yang anda perlukan sebelum menjalankan perintah untuk mendapatkan hasil yang lebih tepat.
- Gunakan perintah ini secara berkala untuk memeriksa status dan kesihatan domain anda.