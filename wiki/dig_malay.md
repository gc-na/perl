# [Sistem Operasi] C Shell (csh) dig Penggunaan: Memeriksa DNS

## Overview
Perintah `dig` digunakan untuk melakukan pencarian DNS (Domain Name System). Ia membolehkan pengguna untuk mendapatkan maklumat tentang nama domain, termasuk alamat IP dan rekod DNS lain.

## Usage
Berikut adalah sintaks asas untuk perintah `dig`:

```
dig [options] [arguments]
```

## Common Options
- `@server` : Menentukan pelayan DNS yang ingin digunakan untuk pencarian.
- `-t type` : Menentukan jenis rekod yang ingin dicari (contohnya, A, MX, TXT).
- `+short` : Mengembalikan hasil dalam format yang lebih ringkas.
- `+trace` : Mengikuti laluan pencarian DNS dari pelayan akar hingga ke pelayan yang memberikan jawapan.

## Common Examples
Berikut adalah beberapa contoh penggunaan `dig`:

1. **Mencari alamat IP untuk nama domain:**
   ```bash
   dig example.com
   ```

2. **Mencari rekod MX (Mail Exchange) untuk domain:**
   ```bash
   dig example.com -t MX
   ```

3. **Menggunakan pelayan DNS tertentu:**
   ```bash
   dig @8.8.8.8 example.com
   ```

4. **Mendapatkan hasil ringkas:**
   ```bash
   dig example.com +short
   ```

5. **Mengikuti laluan pencarian DNS:**
   ```bash
   dig example.com +trace
   ```

## Tips
- Gunakan `+short` untuk mendapatkan jawapan yang lebih mudah dibaca, terutama jika anda hanya memerlukan alamat IP.
- Jika anda sering menggunakan pelayan DNS tertentu, pertimbangkan untuk menambahnya dalam alias untuk kemudahan akses.
- Sentiasa semak jenis rekod yang anda perlukan untuk memastikan anda mendapatkan maklumat yang tepat.