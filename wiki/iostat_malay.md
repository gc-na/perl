# [Linux] C Shell (csh) iostat Penggunaan: Memantau statistik I/O

## Overview
Perintah `iostat` digunakan untuk memantau statistik input/output (I/O) sistem. Ia memberikan maklumat tentang penggunaan CPU dan statistik I/O untuk peranti penyimpanan, membantu pengguna memahami prestasi sistem.

## Usage
Sintaks asas bagi perintah `iostat` adalah seperti berikut:

```csh
iostat [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan umum untuk `iostat` beserta penjelasan ringkas:

- `-c`: Menunjukkan statistik penggunaan CPU sahaja.
- `-d`: Menunjukkan statistik I/O untuk peranti penyimpanan.
- `-x`: Menunjukkan maklumat tambahan untuk peranti, termasuk statistik penggunaan.
- `-t`: Menunjukkan waktu dan tarikh dalam output.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `iostat`:

1. Menunjukkan statistik CPU dan I/O secara asas:
   ```csh
   iostat
   ```

2. Menunjukkan hanya statistik penggunaan CPU:
   ```csh
   iostat -c
   ```

3. Menunjukkan statistik I/O untuk semua peranti:
   ```csh
   iostat -d
   ```

4. Menunjukkan maklumat tambahan untuk peranti:
   ```csh
   iostat -x
   ```

5. Menunjukkan statistik dengan waktu dan tarikh:
   ```csh
   iostat -t
   ```

## Tips
- Gunakan pilihan `-x` untuk mendapatkan maklumat yang lebih terperinci tentang prestasi peranti penyimpanan.
- Jalankan `iostat` secara berkala untuk memantau perubahan dalam statistik I/O semasa penggunaan sistem.
- Pertimbangkan untuk menggabungkan `iostat` dengan perintah lain seperti `grep` untuk menapis output yang relevan.