# [Sistem Operasi] C Shell (csh) history: Mengurus senarai arahan yang telah dijalankan

## Overview
Perintah `history` dalam C Shell (csh) digunakan untuk memaparkan senarai arahan yang telah dijalankan dalam sesi terminal semasa. Ini membolehkan pengguna untuk melihat dan mengulangi arahan yang telah digunakan sebelumnya dengan mudah.

## Usage
Sintaks asas untuk perintah `history` adalah seperti berikut:

```
history [options] [arguments]
```

## Common Options
- `-c`: Menghapuskan semua entri dalam senarai sejarah.
- `-n`: Membaca sejarah dari fail tanpa menulis kembali ke fail.
- `-r`: Membaca sejarah dari fail dan menambahkannya ke senarai sejarah semasa.
- `-w`: Menulis senarai sejarah semasa ke dalam fail.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `history`:

1. **Paparkan senarai sejarah arahan**:
   ```csh
   history
   ```

2. **Hapuskan semua entri dalam sejarah**:
   ```csh
   history -c
   ```

3. **Baca sejarah dari fail**:
   ```csh
   history -r
   ```

4. **Tulis sejarah semasa ke dalam fail**:
   ```csh
   history -w
   ```

5. **Paparkan 10 arahan terakhir**:
   ```csh
   history 10
   ```

## Tips
- Gunakan `!n` untuk menjalankan arahan ke-n dari senarai sejarah.
- Untuk mengulangi arahan terakhir, anda boleh menggunakan `!!`.
- Sentiasa simpan sejarah anda dengan menggunakan `history -w` sebelum menutup sesi terminal untuk memastikan anda tidak kehilangan arahan penting.