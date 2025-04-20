# [Sistem Operasi] C Shell (csh) nslookup: [mendapatkan maklumat DNS]

## Overview
Perintah `nslookup` digunakan untuk mendapatkan maklumat DNS (Domain Name System) tentang nama domain atau alamat IP. Ia membolehkan pengguna untuk menyemak rekod DNS dan membantu dalam penyelesaian masalah berkaitan rangkaian.

## Usage
Sintaks asas untuk menggunakan `nslookup` adalah seperti berikut:

```
nslookup [options] [arguments]
```

## Common Options
- `-type=TYPE` : Menentukan jenis rekod DNS yang ingin dicari, seperti A, MX, atau CNAME.
- `-debug` : Mengaktifkan mod debug untuk mendapatkan maklumat terperinci tentang proses pencarian.
- `-timeout=SECONDS` : Menetapkan masa tamat untuk menunggu respons dari pelayan DNS.

## Common Examples
Berikut adalah beberapa contoh penggunaan `nslookup`:

1. **Mendapatkan alamat IP untuk nama domain:**
   ```
   nslookup example.com
   ```

2. **Mencari rekod MX untuk domain:**
   ```
   nslookup -type=MX example.com
   ```

3. **Menggunakan pelayan DNS tertentu:**
   ```
   nslookup example.com 8.8.8.8
   ```

4. **Mengaktifkan mod debug:**
   ```
   nslookup -debug example.com
   ```

## Tips
- Gunakan `nslookup` untuk menyemak jika nama domain telah dikonfigurasi dengan betul dalam DNS.
- Sentiasa periksa pelayan DNS yang digunakan jika anda tidak menerima hasil yang dijangkakan.
- Untuk maklumat lebih lanjut tentang rekod DNS, gunakan pilihan `-type` untuk menentukan jenis rekod yang spesifik.