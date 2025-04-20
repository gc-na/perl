# [Sistem Operasi] C Shell (csh) fc <Penggunaan setara>: Mengedit dan menjalankan perintah sebelumnya

## Overview
Perintah `fc` dalam C Shell (csh) digunakan untuk mengedit dan menjalankan perintah yang telah dilaksanakan sebelumnya. Ia membolehkan pengguna untuk mengakses dan memodifikasi perintah yang tersimpan dalam sejarah terminal.

## Usage
Berikut adalah sintaks asas untuk perintah `fc`:

```
fc [options] [arguments]
```

## Common Options
- `-l`: Menyenaraikan perintah yang telah dijalankan dalam sejarah.
- `-e`: Menentukan editor yang akan digunakan untuk mengedit perintah.
- `-n`: Menyembunyikan nombor perintah dalam senarai.
- `-r`: Membalikkan urutan perintah yang disenaraikan.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `fc`:

1. **Menyenaraikan perintah yang telah dijalankan:**
   ```csh
   fc -l
   ```

2. **Mengedit perintah terakhir menggunakan editor lalai:**
   ```csh
   fc
   ```

3. **Mengedit perintah tertentu (contohnya, perintah ke-3):**
   ```csh
   fc 3
   ```

4. **Menggunakan editor `vim` untuk mengedit perintah terakhir:**
   ```csh
   fc -e vim
   ```

5. **Menyenaraikan perintah tanpa nombor:**
   ```csh
   fc -ln
   ```

## Tips
- Gunakan `fc` untuk memperbaiki kesalahan kecil dalam perintah yang baru sahaja dijalankan tanpa perlu menaip semula.
- Pilih editor yang anda selesa untuk mengedit perintah, seperti `nano` atau `vim`, dengan menggunakan pilihan `-e`.
- Sentiasa semak senarai perintah yang telah dijalankan sebelum menggunakan `fc` untuk memastikan anda mengedit perintah yang betul.