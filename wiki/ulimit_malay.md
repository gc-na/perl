# [Linux] C Shell (csh) ulimit: Mengawal had sumber sistem

## Overview
Perintah `ulimit` dalam C Shell (csh) digunakan untuk mengawal had sumber yang boleh digunakan oleh proses yang dijalankan dalam shell. Ia membolehkan pengguna menetapkan batasan pada penggunaan memori, jumlah fail terbuka, dan sumber lain untuk mengelakkan penggunaan berlebihan yang boleh menjejaskan prestasi sistem.

## Usage
Sintaks asas bagi perintah `ulimit` adalah seperti berikut:

```csh
ulimit [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `ulimit` beserta penjelasan ringkas:

- `-a`: Menunjukkan semua had sumber semasa.
- `-c [size]`: Menetapkan had saiz fail core.
- `-d [size]`: Menetapkan had saiz segmen data.
- `-f [size]`: Menetapkan had saiz fail maksimum.
- `-l [size]`: Menetapkan had saiz memori terkunci.
- `-n [number]`: Menetapkan had bilangan fail terbuka.
- `-s [size]`: Menetapkan had saiz stack.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `ulimit`:

1. **Menunjukkan semua had sumber semasa:**
   ```csh
   ulimit -a
   ```

2. **Menetapkan had saiz fail maksimum kepada 1024 blok:**
   ```csh
   ulimit -f 1024
   ```

3. **Menetapkan had bilangan fail terbuka kepada 256:**
   ```csh
   ulimit -n 256
   ```

4. **Menetapkan had saiz segmen data kepada 2048 kilobyte:**
   ```csh
   ulimit -d 2048
   ```

5. **Menetapkan had saiz stack kepada 8192 kilobyte:**
   ```csh
   ulimit -s 8192
   ```

## Tips
- Sentiasa semak had sumber semasa dengan `ulimit -a` sebelum menjalankan aplikasi yang memerlukan banyak sumber.
- Gunakan `ulimit` dalam skrip shell untuk memastikan had yang sesuai ditetapkan sebelum menjalankan proses penting.
- Hati-hati apabila menetapkan had yang terlalu rendah, kerana ia boleh menyebabkan aplikasi gagal berfungsi dengan baik.