# [Sistem Operasi] C Shell (csh) script Penggunaan: Merekam sesi terminal

## Overview
Perintah `script` digunakan untuk merekam sesi terminal ke dalam sebuah file. Ini berguna untuk menyimpan semua output yang dihasilkan selama sesi, termasuk perintah yang dijalankan dan hasilnya. Dengan menggunakan `script`, pengguna dapat membuat catatan dari sesi terminal untuk keperluan dokumentasi atau analisis.

## Usage
Berikut adalah sintaks dasar dari perintah `script`:

```csh
script [options] [arguments]
```

## Common Options
- `-a`: Menambahkan output ke file yang sudah ada, bukan menimpa file tersebut.
- `-f`: Menampilkan output secara langsung ke layar saat merekam.
- `-q`: Menjalankan perintah dalam mode senyap, tanpa menampilkan pesan pembuka dan penutup.
- `-t`: Merekam waktu yang dibutuhkan untuk setiap perintah yang dijalankan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `script`:

1. **Merekam sesi ke file default (`typescript`)**:
   ```csh
   script
   ```
   Ini akan mulai merekam sesi terminal ke dalam file bernama `typescript`.

2. **Merekam sesi dengan nama file khusus**:
   ```csh
   script mysession.log
   ```
   Ini akan merekam sesi ke dalam file `mysession.log`.

3. **Menambahkan output ke file yang sudah ada**:
   ```csh
   script -a mysession.log
   ```
   Ini akan menambahkan output sesi ke file `mysession.log` yang sudah ada.

4. **Merekam sesi dengan tampilan langsung**:
   ```csh
   script -f
   ```
   Ini akan merekam sesi dan menampilkan output secara langsung di layar.

5. **Merekam waktu eksekusi perintah**:
   ```csh
   script -t mysession.log
   ```
   Ini akan merekam sesi dan juga mencatat waktu yang dibutuhkan untuk setiap perintah.

## Tips
- Gunakan opsi `-a` jika Anda ingin merekam beberapa sesi ke dalam file yang sama tanpa kehilangan data sebelumnya.
- Pastikan untuk menghentikan sesi dengan perintah `exit` untuk menyimpan hasil rekaman dengan benar.
- Periksa file hasil rekaman setelah sesi untuk memastikan semua output yang diinginkan telah terekam.