# [Sistem Operasi] C Shell (csh) script Penggunaan: Merekam sesi terminal

## Overview
Perintah `script` dalam C Shell (csh) digunakan untuk merekam sesi terminal ke dalam sebuah file. Ini sangat berguna untuk mencatat perintah yang dijalankan dan output yang dihasilkan selama sesi, sehingga Anda dapat mereview atau membagikannya nanti.

## Usage
Berikut adalah sintaks dasar dari perintah `script`:

```csh
script [options] [arguments]
```

## Common Options
- `-a`: Menambahkan output ke file yang sudah ada, alih-alih menimpa file tersebut.
- `-f`: Menampilkan output ke terminal secara langsung, sambil tetap merekamnya.
- `-q`: Menjalankan perintah tanpa menampilkan pesan pembuka.
- `-t`: Merekam waktu eksekusi perintah dalam sesi.

## Common Examples
Berikut beberapa contoh penggunaan perintah `script`:

1. **Merekam sesi terminal ke dalam file default (`typescript`)**:
   ```csh
   script
   ```

2. **Merekam sesi dan menyimpan output ke file tertentu**:
   ```csh
   script mysession.txt
   ```

3. **Merekam sesi dan menambahkan output ke file yang sudah ada**:
   ```csh
   script -a mysession.txt
   ```

4. **Merekam sesi dengan menampilkan output ke terminal**:
   ```csh
   script -f mysession.txt
   ```

5. **Merekam waktu eksekusi perintah dalam sesi**:
   ```csh
   script -t mysession.txt
   ```

## Tips
- Pastikan untuk keluar dari sesi dengan perintah `exit` agar file rekaman selesai dengan benar.
- Gunakan opsi `-q` jika Anda ingin merekam tanpa gangguan dari pesan pembuka.
- Periksa file hasil rekaman setelah sesi untuk memastikan semua perintah dan output tercatat dengan baik.