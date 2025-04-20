# [Sistem Operasi] C Shell (csh) mpstat Penggunaan: Memantau Statistik CPU

## Overview
Perintah `mpstat` digunakan untuk menampilkan statistik penggunaan CPU secara real-time. Ini memberikan informasi tentang aktivitas CPU, termasuk penggunaan waktu idle, sistem, dan pengguna, yang sangat berguna untuk analisis kinerja sistem.

## Usage
Berikut adalah sintaks dasar dari perintah `mpstat`:

```csh
mpstat [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `mpstat`:

- `-P ALL`: Menampilkan statistik untuk semua CPU.
- `-u`: Menampilkan penggunaan CPU dalam persentase.
- `-h`: Menampilkan output dalam format yang lebih mudah dibaca.
- `interval`: Menentukan interval waktu (dalam detik) untuk pengambilan data berulang.

## Common Examples
Berikut adalah beberapa contoh penggunaan `mpstat`:

1. Menampilkan statistik CPU untuk semua prosesor:
   ```csh
   mpstat -P ALL
   ```

2. Menampilkan penggunaan CPU setiap 5 detik:
   ```csh
   mpstat 5
   ```

3. Menampilkan penggunaan CPU dengan format yang lebih mudah dibaca:
   ```csh
   mpstat -h
   ```

4. Mengambil statistik CPU untuk prosesor tertentu (misalnya CPU 0):
   ```csh
   mpstat -P 0
   ```

## Tips
- Gunakan opsi `-P ALL` untuk mendapatkan gambaran menyeluruh tentang semua CPU yang ada di sistem Anda.
- Cobalah mengatur interval yang lebih pendek untuk memantau penggunaan CPU secara lebih dinamis saat menjalankan aplikasi berat.
- Simpan output `mpstat` ke dalam file untuk analisis lebih lanjut dengan menggunakan redirection, misalnya:
  ```csh
  mpstat -P ALL 5 > cpu_stats.txt
  ```