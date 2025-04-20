# [Sistem Operasi] C Shell (csh) curl Penggunaan: Mengambil dan menghantar data melalui URL

## Overview
Perintah `curl` digunakan untuk mengambil dan menghantar data melalui URL. Ia menyokong pelbagai protokol seperti HTTP, HTTPS, FTP, dan banyak lagi. `curl` sering digunakan dalam skrip dan automasi untuk berinteraksi dengan API atau memuat turun fail.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `curl`:

```
curl [options] [arguments]
```

## Common Options
- `-X, --request <command>`: Menentukan jenis permintaan HTTP yang ingin digunakan, seperti GET, POST, PUT, DELETE.
- `-d, --data <data>`: Menghantar data sebagai permintaan POST.
- `-H, --header <header>`: Menambah header khusus pada permintaan.
- `-o, --output <file>`: Menyimpan output ke dalam fail yang ditentukan.
- `-I, --head`: Mengambil hanya header dari URL tanpa isi.

## Common Examples
Berikut adalah beberapa contoh penggunaan `curl`:

1. **Mengambil halaman web:**
   ```bash
   curl http://example.com
   ```

2. **Menghantar data menggunakan POST:**
   ```bash
   curl -X POST -d "name=John&age=30" http://example.com/api
   ```

3. **Menyimpan output ke dalam fail:**
   ```bash
   curl -o output.html http://example.com
   ```

4. **Mengambil hanya header dari URL:**
   ```bash
   curl -I http://example.com
   ```

5. **Menambah header khusus:**
   ```bash
   curl -H "Authorization: Bearer token" http://example.com/api
   ```

## Tips
- Sentiasa semak dokumentasi untuk pilihan tambahan yang mungkin berguna untuk keperluan khusus anda.
- Gunakan `-v` untuk mengaktifkan mod verbose jika anda ingin melihat butiran lebih lanjut tentang permintaan dan respons.
- Untuk menguji API, pertimbangkan untuk menggunakan `-H` untuk menambah header yang diperlukan seperti token pengesahan.