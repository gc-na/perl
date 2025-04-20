# [Sistem Operasi] C Shell (csh) ps Penggunaan: Menampilkan proses yang sedang berjalan

## Overview
Perintah `ps` dalam C Shell (csh) digunakan untuk menampilkan senarai proses yang sedang berjalan pada sistem. Ia memberikan maklumat tentang proses-proses ini, termasuk ID proses (PID), status, dan penggunaan sumber.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `ps`:

```
ps [options] [arguments]
```

## Common Options
- `-e` : Menampilkan semua proses yang sedang berjalan.
- `-f` : Menampilkan proses dalam format penuh, termasuk maklumat tambahan seperti pengguna dan waktu.
- `-u [user]` : Menampilkan proses yang dimiliki oleh pengguna tertentu.
- `-l` : Menampilkan proses dalam format panjang dengan lebih banyak maklumat.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `ps`:

1. Menampilkan semua proses yang sedang berjalan:
    ```csh
    ps -e
    ```

2. Menampilkan proses dalam format penuh:
    ```csh
    ps -f
    ```

3. Menampilkan proses yang dimiliki oleh pengguna tertentu:
    ```csh
    ps -u username
    ```

4. Menampilkan proses dalam format panjang:
    ```csh
    ps -l
    ```

## Tips
- Gunakan `ps -ef` untuk mendapatkan maklumat lengkap tentang semua proses dalam satu perintah.
- Kombinasikan `ps` dengan `grep` untuk mencari proses tertentu. Contohnya:
    ```csh
    ps -e | grep nama_proses
    ```
- Ingat bahawa output `ps` adalah snapshot pada masa tertentu, jadi untuk memantau proses secara berterusan, pertimbangkan untuk menggunakan perintah `top`.