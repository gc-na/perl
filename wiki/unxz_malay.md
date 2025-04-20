# [Sistem Operasi] C Shell (csh) unxz: Mengeluarkan fail yang dimampatkan

## Overview
Perintah `unxz` digunakan untuk mengeluarkan fail yang telah dimampatkan menggunakan algoritma XZ. Ia adalah alat yang berguna untuk mengembalikan fail kepada bentuk asalnya selepas proses pemampatan.

## Usage
Sintaks asas bagi perintah `unxz` adalah seperti berikut:

```
unxz [options] [arguments]
```

## Common Options
- `-k`: Menyimpan fail asal yang dimampatkan selepas proses pengeluaran.
- `-f`: Memaksa pengeluaran walaupun fail yang sama sudah ada.
- `-v`: Menunjukkan maklumat terperinci semasa proses pengeluaran.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `unxz`:

1. Mengeluarkan fail yang dimampatkan:
   ```csh
   unxz fail.txt.xz
   ```

2. Mengeluarkan fail dan menyimpan fail asal:
   ```csh
   unxz -k fail.txt.xz
   ```

3. Memaksa pengeluaran walaupun fail yang sama sudah ada:
   ```csh
   unxz -f fail.txt.xz
   ```

4. Menunjukkan maklumat terperinci semasa pengeluaran:
   ```csh
   unxz -v fail.txt.xz
   ```

## Tips
- Pastikan anda mempunyai ruang yang mencukupi di dalam sistem untuk menyimpan fail yang diekstrak.
- Gunakan pilihan `-k` jika anda ingin mengekalkan fail yang dimampatkan untuk rujukan masa depan.
- Sentiasa semak maklumat terperinci dengan pilihan `-v` untuk memastikan proses pengeluaran berjalan lancar.