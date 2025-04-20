# [Linux] C Shell (csh) finger Penggunaan: Menunjukkan maklumat pengguna

## Overview
Perintah `finger` digunakan untuk mendapatkan maklumat tentang pengguna yang sedang log masuk ke sistem. Ia memberikan maklumat seperti nama pengguna, waktu log masuk, dan status pengguna.

## Usage
Berikut adalah sintaks asas untuk perintah `finger`:

```
finger [options] [arguments]
```

## Common Options
- `-l`: Menunjukkan maklumat pengguna dalam format yang lebih terperinci.
- `-m`: Mengabaikan kes apabila mencari nama pengguna.
- `-s`: Menunjukkan maklumat ringkas tentang pengguna.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `finger`:

1. Menunjukkan maklumat semua pengguna yang sedang log masuk:
   ```csh
   finger
   ```

2. Menunjukkan maklumat terperinci untuk pengguna tertentu:
   ```csh
   finger -l username
   ```

3. Menunjukkan maklumat ringkas untuk pengguna tertentu:
   ```csh
   finger -s username
   ```

4. Mencari pengguna tanpa menghiraukan kes:
   ```csh
   finger -m UserName
   ```

## Tips
- Gunakan `finger` secara berkala untuk memantau pengguna yang sedang log masuk ke sistem.
- Kombinasikan `finger` dengan perintah lain seperti `grep` untuk mencari pengguna tertentu dalam senarai yang panjang.
- Pastikan perkhidmatan `finger` diaktifkan pada sistem anda, kerana beberapa sistem mungkin tidak mengaktifkannya secara lalai.