# [Linux] C Shell (csh) screen: Mengurus sesi terminal

## Overview
Perintah `screen` membolehkan pengguna untuk mengurus sesi terminal secara berasingan. Ia membolehkan anda menjalankan aplikasi dalam sesi yang berbeza dan mengaksesnya semula walaupun anda terputus dari sesi tersebut.

## Usage
Berikut adalah sintaks asas untuk perintah `screen`:

```
screen [options] [arguments]
```

## Common Options
- `-S [nama]`: Menetapkan nama untuk sesi baru.
- `-d -r`: Memutuskan sesi yang sedang berjalan dan menyambung semula.
- `-list`: Menunjukkan senarai sesi yang sedang berjalan.
- `-L`: Mengaktifkan log untuk sesi yang sedang berjalan.

## Common Examples
Berikut adalah beberapa contoh penggunaan `screen`:

1. **Mencipta sesi baru dengan nama tertentu:**
   ```bash
   screen -S sesi_saya
   ```

2. **Menyambung semula ke sesi yang terputus:**
   ```bash
   screen -d -r sesi_saya
   ```

3. **Menunjukkan senarai sesi yang sedang berjalan:**
   ```bash
   screen -list
   ```

4. **Mengaktifkan log untuk sesi baru:**
   ```bash
   screen -L
   ```

## Tips
- Sentiasa beri nama pada sesi anda untuk memudahkan pengurusan.
- Gunakan pintasan keyboard `Ctrl + A` diikuti dengan `D` untuk memutuskan sesi tanpa menutup aplikasi yang sedang berjalan.
- Simpan log sesi anda untuk rujukan masa depan dengan menggunakan pilihan `-L`.