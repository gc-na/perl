# [Sistem Operasi] C Shell (csh) stat <Penggunaan setara>: Menunjukkan maklumat tentang fail

## Overview
Perintah `stat` digunakan untuk memaparkan maklumat terperinci mengenai fail atau direktori dalam sistem fail. Ia memberikan data seperti saiz, tarikh dan masa terakhir diubah, serta hak akses fail.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `stat`:

```csh
stat [options] [arguments]
```

## Common Options
- `-f`: Menunjukkan maklumat dalam format yang lebih ringkas.
- `-L`: Mengikuti pautan simbolik untuk mendapatkan maklumat fail yang ditunjuk.
- `-c`: Menggunakan format khusus untuk output yang ditentukan oleh pengguna.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `stat`:

1. Menunjukkan maklumat lengkap tentang fail:
    ```csh
    stat myfile.txt
    ```

2. Menunjukkan maklumat dalam format ringkas:
    ```csh
    stat -f myfile.txt
    ```

3. Mengikuti pautan simbolik:
    ```csh
    stat -L symlink.txt
    ```

4. Menggunakan format khusus untuk output:
    ```csh
    stat -c '%s bytes, %y' myfile.txt
    ```

## Tips
- Gunakan pilihan `-f` jika anda hanya memerlukan maklumat ringkas untuk banyak fail.
- Untuk fail yang mempunyai pautan simbolik, ingat untuk menggunakan pilihan `-L` agar maklumat yang tepat dapat diperoleh.
- Anda boleh menggabungkan beberapa pilihan untuk mendapatkan output yang lebih sesuai dengan keperluan anda.