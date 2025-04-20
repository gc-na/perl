# [Sistem Pengendalian] C Shell (csh) scp: [salin fail selamat]

## Overview
Perintah `scp` (Secure Copy Protocol) digunakan untuk menyalin fail atau direktori antara komputer secara selamat melalui rangkaian. Ia menggunakan protokol SSH untuk memastikan bahawa data yang dipindahkan adalah selamat dan terjamin.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `scp`:

```csh
scp [options] [source] [destination]
```

## Common Options
- `-r`: Menyalin direktori secara rekursif.
- `-P`: Menentukan nombor port SSH yang akan digunakan (perhatikan huruf besar).
- `-i`: Menentukan fail kunci peribadi untuk pengesahan.
- `-v`: Mengaktifkan mod verbose untuk mendapatkan maklumat lanjut tentang proses pemindahan.

## Common Examples
Berikut adalah beberapa contoh penggunaan `scp`:

1. Menyalin fail dari komputer tempatan ke pelayan jauh:
   ```csh
   scp file.txt user@remote_host:/path/to/destination/
   ```

2. Menyalin fail dari pelayan jauh ke komputer tempatan:
   ```csh
   scp user@remote_host:/path/to/file.txt /local/destination/
   ```

3. Menyalin direktori secara rekursif dari komputer tempatan ke pelayan jauh:
   ```csh
   scp -r /local/directory user@remote_host:/path/to/destination/
   ```

4. Menyalin fail menggunakan port SSH yang berbeza:
   ```csh
   scp -P 2222 file.txt user@remote_host:/path/to/destination/
   ```

## Tips
- Sentiasa gunakan `-v` untuk mendapatkan maklumat tambahan jika anda menghadapi masalah semasa pemindahan.
- Pastikan anda mempunyai kebenaran yang betul untuk menyalin fail ke lokasi yang dituju.
- Gunakan kunci SSH untuk pengesahan yang lebih selamat dan mudah, terutamanya untuk pemindahan yang kerap.