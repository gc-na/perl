# [Sistem Operasi] C Shell (csh) ftp Penggunaan: Menghantar dan menerima fail melalui protokol FTP

## Overview
Perintah `ftp` dalam C Shell (csh) digunakan untuk menghantar dan menerima fail melalui protokol File Transfer Protocol (FTP). Ia membolehkan pengguna untuk berhubung dengan pelayan FTP dan menguruskan pemindahan fail dengan mudah.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `ftp`:

```csh
ftp [options] [arguments]
```

## Common Options
- `-i`: Mengaktifkan mod binari, yang membolehkan pemindahan fail tanpa pengubahsuaian.
- `-v`: Mengaktifkan mod verbose, yang menunjukkan lebih banyak maklumat semasa pemindahan.
- `-n`: Menghalang ftp daripada secara automatik log masuk ke pelayan.
- `-g`: Menghalang penggunaan globbing, membolehkan nama fail dengan karakter khas.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `ftp`:

1. **Menghubungi pelayan FTP:**
   ```csh
   ftp ftp.example.com
   ```

2. **Log masuk dengan nama pengguna dan kata laluan:**
   ```csh
   ftp -n ftp.example.com
   user your_username your_password
   ```

3. **Menghantar fail ke pelayan:**
   ```csh
   put localfile.txt
   ```

4. **Menerima fail dari pelayan:**
   ```csh
   get remotefile.txt
   ```

5. **Menghantar fail dalam mod binari:**
   ```csh
   binary
   put image.png
   ```

## Tips
- Sentiasa gunakan mod binari (`binary`) apabila menghantar fail bukan teks seperti imej atau video untuk mengelakkan kerosakan pada fail.
- Gunakan mod verbose (`-v`) untuk mendapatkan maklumat tambahan semasa pemindahan, yang boleh membantu dalam menyelesaikan masalah.
- Jika anda sering berhubung dengan pelayan yang sama, pertimbangkan untuk menyimpan maklumat log masuk dalam fail `.netrc` untuk kemudahan akses.