# [Sistem Operasi] C Shell (csh) umask: Mengatur izin file secara default

## Overview
Perintah `umask` digunakan untuk mengatur izin file default yang diterapkan pada file dan direktori baru yang dibuat oleh pengguna. Dengan mengatur umask, Anda dapat mengontrol akses terhadap file dan direktori yang baru dibuat.

## Usage
Sintaks dasar dari perintah umask adalah sebagai berikut:

```csh
umask [options] [arguments]
```

## Common Options
- `-S`: Menampilkan umask dalam format simbolik.
- `-p`: Menampilkan umask saat ini tanpa mengubahnya.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah umask:

1. **Menampilkan umask saat ini:**
   ```csh
   umask
   ```

2. **Mengatur umask menjadi 022:**
   ```csh
   umask 022
   ```

3. **Menampilkan umask dalam format simbolik:**
   ```csh
   umask -S
   ```

4. **Mengatur umask menjadi 007:**
   ```csh
   umask 007
   ```

## Tips
- Pastikan untuk memeriksa umask Anda sebelum membuat file baru untuk memastikan izin yang tepat.
- Gunakan umask yang lebih ketat (misalnya, 027) untuk meningkatkan keamanan file Anda.
- Ingat bahwa umask hanya mempengaruhi file dan direktori yang baru dibuat, bukan yang sudah ada.