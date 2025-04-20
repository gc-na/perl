# [Sistem Operasi] C Shell (csh) renice: Mengubah keutamaan proses

## Overview
Perintah `renice` digunakan untuk mengubah keutamaan proses yang sedang berjalan dalam sistem. Keutamaan ini menentukan berapa banyak sumber daya CPU yang diberikan kepada proses tersebut. Proses dengan keutamaan yang lebih rendah akan menerima lebih sedikit sumber daya, sementara proses dengan keutamaan yang lebih tinggi akan menerima lebih banyak.

## Usage
Sintaks asas bagi perintah `renice` adalah seperti berikut:

```
renice [options] [arguments]
```

## Common Options
- `-n`: Menetapkan nilai keutamaan baru.
- `-p`: Mengubah keutamaan proses berdasarkan ID proses (PID).
- `-g`: Mengubah keutamaan semua proses dalam kumpulan proses tertentu.
- `-u`: Mengubah keutamaan semua proses yang dimiliki oleh pengguna tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan `renice`:

1. Mengubah keutamaan proses dengan PID 1234 kepada 10:
   ```csh
   renice -n 10 -p 1234
   ```

2. Mengubah keutamaan semua proses milik pengguna "john" kepada 5:
   ```csh
   renice -n 5 -u john
   ```

3. Mengubah keutamaan semua proses dalam kumpulan proses dengan ID 5678 kepada -5:
   ```csh
   renice -n -5 -g 5678
   ```

4. Menetapkan keutamaan proses dengan PID 4321 kepada 0:
   ```csh
   renice -n 0 -p 4321
   ```

## Tips
- Pastikan anda mempunyai hak istimewa yang diperlukan untuk mengubah keutamaan proses yang dimiliki oleh pengguna lain.
- Gunakan nilai keutamaan negatif untuk memberikan lebih banyak sumber daya kepada proses penting.
- Sentiasa semak keutamaan proses selepas menggunakan `renice` untuk memastikan perubahan telah diterapkan dengan betul.