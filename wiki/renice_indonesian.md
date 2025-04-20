# [Sistem Operasi] C Shell (csh) renice: Mengubah prioritas proses

## Overview
Perintah `renice` digunakan untuk mengubah prioritas eksekusi dari proses yang sedang berjalan di sistem. Dengan mengubah prioritas ini, pengguna dapat memberikan lebih banyak atau lebih sedikit sumber daya CPU kepada proses tertentu, yang dapat membantu dalam pengelolaan kinerja sistem.

## Usage
Berikut adalah sintaks dasar dari perintah `renice`:

```csh
renice [options] [arguments]
```

## Common Options
- `-n`: Menentukan nilai prioritas baru. Nilai ini dapat berupa angka negatif (untuk meningkatkan prioritas) atau positif (untuk menurunkan prioritas).
- `-p`: Menggunakan ID proses (PID) untuk menentukan proses yang akan diubah prioritasnya.
- `-g`: Menggunakan ID grup proses untuk mengubah prioritas semua proses dalam grup tersebut.

## Common Examples
Berikut adalah beberapa contoh penggunaan `renice`:

1. Mengubah prioritas proses dengan PID 1234 menjadi 10:
   ```csh
   renice -n 10 -p 1234
   ```

2. Meningkatkan prioritas proses dengan PID 5678 menjadi -5:
   ```csh
   renice -n -5 -p 5678
   ```

3. Mengubah prioritas semua proses dalam grup dengan ID 1001 menjadi 0:
   ```csh
   renice -n 0 -g 1001
   ```

4. Melihat prioritas proses sebelum dan sesudah perubahan:
   ```csh
   ps -o pid,ni,cmd | grep 1234
   renice -n 5 -p 1234
   ps -o pid,ni,cmd | grep 1234
   ```

## Tips
- Gunakan perintah `ps` untuk memeriksa prioritas proses sebelum dan sesudah menggunakan `renice`.
- Hati-hati saat menurunkan prioritas proses penting, karena hal ini dapat mempengaruhi kinerja aplikasi.
- Pastikan Anda memiliki izin yang tepat untuk mengubah prioritas proses yang bukan milik Anda, biasanya memerlukan hak akses root.