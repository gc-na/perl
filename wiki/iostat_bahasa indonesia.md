# [Linux] C Shell (csh) iostat Penggunaan: Memantau statistik I/O sistem

## Overview
Perintah `iostat` digunakan untuk memantau statistik input/output (I/O) dari sistem. Ini memberikan informasi tentang penggunaan CPU dan aktivitas perangkat penyimpanan, membantu administrator sistem dalam menganalisis kinerja sistem.

## Usage
Berikut adalah sintaks dasar dari perintah `iostat`:

```csh
iostat [options] [arguments]
```

## Common Options
- `-c`: Menampilkan statistik CPU.
- `-d`: Menampilkan statistik perangkat penyimpanan.
- `-x`: Menampilkan statistik perangkat dengan informasi yang lebih mendetail.
- `-t`: Menampilkan waktu dan tanggal saat statistik diambil.
- `interval`: Menentukan interval waktu dalam detik untuk pengambilan data berulang.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `iostat`:

1. Menampilkan statistik dasar CPU dan perangkat penyimpanan:
   ```csh
   iostat
   ```

2. Menampilkan statistik CPU saja:
   ```csh
   iostat -c
   ```

3. Menampilkan statistik perangkat penyimpanan dengan detail:
   ```csh
   iostat -d -x
   ```

4. Menampilkan statistik setiap 5 detik:
   ```csh
   iostat 5
   ```

5. Menampilkan statistik dengan waktu dan tanggal:
   ```csh
   iostat -t
   ```

## Tips
- Gunakan opsi `-x` untuk mendapatkan informasi lebih mendetail tentang perangkat penyimpanan, yang sangat berguna untuk analisis kinerja.
- Perhatikan penggunaan CPU dan I/O secara bersamaan untuk mendapatkan gambaran lengkap tentang kinerja sistem.
- Simpan output `iostat` ke dalam file untuk analisis lebih lanjut dengan menggunakan redirection:
  ```csh
  iostat -x > iostat_output.txt
  ```