# [Sistem Operasi] C Shell (csh) xz: Mengompres dan mendekompres fail

## Overview
Perintah `xz` digunakan untuk mengompres dan mendekompres fail menggunakan algoritma pemampatan yang berkesan. Ia menghasilkan fail dengan sambungan `.xz`, yang biasanya lebih kecil berbanding dengan fail asal.

## Usage
Berikut adalah sintaks asas untuk perintah `xz`:

```csh
xz [options] [arguments]
```

## Common Options
- `-d`, `--decompress`: Mendekompres fail.
- `-k`, `--keep`: Menyimpan fail asal selepas pemampatan.
- `-v`, `--verbose`: Menunjukkan maklumat lanjut semasa pemampatan.
- `-f`, `--force`: Memaksa pemampatan walaupun fail dengan nama yang sama sudah wujud.

## Common Examples
Berikut adalah beberapa contoh praktikal menggunakan perintah `xz`:

1. **Mengompres fail**
   ```csh
   xz fail.txt
   ```
   Ini akan menghasilkan fail `fail.txt.xz`.

2. **Mendekompres fail**
   ```csh
   xz -d fail.txt.xz
   ```
   Ini akan mengembalikan fail kepada `fail.txt`.

3. **Mengompres fail dan menyimpan fail asal**
   ```csh
   xz -k fail.txt
   ```
   Ini akan menghasilkan `fail.txt.xz` dan mengekalkan `fail.txt`.

4. **Menunjukkan maklumat pemampatan**
   ```csh
   xz -v fail.txt
   ```
   Ini akan menunjukkan proses pemampatan dengan maklumat lanjut.

## Tips
- Sentiasa gunakan pilihan `-k` jika anda ingin mengekalkan fail asal semasa pemampatan.
- Untuk pemampatan yang lebih cepat, pertimbangkan untuk menggunakan pilihan `-1` (pemampatan lebih rendah) jika saiz fail tidak terlalu penting.
- Periksa ruang cakera anda sebelum mengompres fail besar untuk mengelakkan masalah ruang.