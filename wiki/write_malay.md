# [Linux] C Shell (csh) write penggunaan: Menghantar mesej kepada pengguna lain

## Overview
Perintah `write` dalam C Shell (csh) digunakan untuk menghantar mesej secara langsung kepada pengguna lain yang sedang log masuk ke sistem. Ia membolehkan komunikasi yang cepat dan mudah antara pengguna dalam persekitaran terminal.

## Usage
Berikut adalah sintaks asas untuk perintah `write`:

```
write [options] [user] [tty]
```

## Common Options
- `-n`: Menghantar mesej tanpa menunggu pengesahan daripada penerima.
- `-h`: Menunjukkan bantuan ringkas tentang penggunaan perintah.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `write`:

1. Menghantar mesej kepada pengguna tertentu:
   ```csh
   write john
   Hello John, how are you?
   ```

2. Menghantar mesej kepada pengguna yang sedang menggunakan tty tertentu:
   ```csh
   write jane tty2
   Don't forget our meeting at 3 PM!
   ```

3. Menghantar mesej tanpa menunggu pengesahan:
   ```csh
   write -n alice
   Please check your email.
   ```

## Tips
- Pastikan pengguna yang ingin dihubungi sedang log masuk dan tidak dalam keadaan "mesg n" yang menghalang penerimaan mesej.
- Gunakan perintah `who` untuk melihat senarai pengguna yang sedang log masuk dan tty mereka sebelum menghantar mesej.
- Untuk menghentikan penghantaran mesej, tekan `Ctrl + C`.