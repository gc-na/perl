# [Sistem Operasi] C Shell (csh) cp Penggunaan: Menyalin Fail

## Overview
Perintah `cp` dalam C Shell (csh) digunakan untuk menyalin fail dan direktori dari satu lokasi ke lokasi lain. Ia membolehkan pengguna untuk membuat salinan fail tanpa mengubah fail asal.

## Usage
Berikut adalah sintaks asas untuk perintah `cp`:

```
cp [options] [arguments]
```

## Common Options
- `-i`: Meminta pengesahan sebelum menimpa fail yang sedia ada.
- `-r`: Menyalin direktori secara rekursif.
- `-u`: Menyalin hanya jika fail sumber lebih baru daripada fail destinasi atau jika fail destinasi tidak wujud.
- `-v`: Menunjukkan maklumat tentang fail yang sedang disalin.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `cp`:

1. Menyalin fail tunggal:
   ```csh
   cp fail1.txt fail2.txt
   ```

2. Menyalin direktori secara rekursif:
   ```csh
   cp -r direktori1 direktori2
   ```

3. Menyalin fail dengan pengesahan:
   ```csh
   cp -i fail1.txt fail2.txt
   ```

4. Menyalin fail hanya jika fail sumber lebih baru:
   ```csh
   cp -u fail1.txt fail2.txt
   ```

5. Menyalin fail dan menunjukkan maklumat:
   ```csh
   cp -v fail1.txt fail2.txt
   ```

## Tips
- Sentiasa gunakan pilihan `-i` jika anda tidak mahu menimpa fail secara tidak sengaja.
- Untuk menyalin direktori, ingat untuk menggunakan pilihan `-r`.
- Periksa fail yang disalin dengan pilihan `-v` untuk memastikan semuanya berjalan dengan baik.