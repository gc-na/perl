# [Linux] C Shell (csh) strace Penggunaan: Mengesan sistem panggilan

## Overview
Perintah `strace` digunakan untuk mengesan dan mendiagnosis sistem panggilan dan isyarat yang dilakukan oleh proses dalam sistem operasi. Ini berguna untuk memahami bagaimana program berinteraksi dengan sistem dan untuk mengesan masalah yang mungkin berlaku.

## Usage
Sintaks asas untuk menggunakan `strace` adalah seperti berikut:

```csh
strace [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `strace` beserta penjelasan ringkas:

- `-c`: Mengira statistik sistem panggilan.
- `-e trace=SYSCALL`: Mengesan hanya sistem panggilan tertentu.
- `-o filename`: Menyimpan output ke dalam fail yang ditentukan.
- `-p pid`: Mengesan proses yang sedang berjalan dengan ID proses tertentu.
- `-f`: Mengesan proses anak yang dicipta oleh proses yang sedang dipantau.

## Common Examples
Berikut adalah beberapa contoh penggunaan `strace`:

1. Mengesan semua sistem panggilan untuk program `ls`:
   ```csh
   strace ls
   ```

2. Mengira statistik sistem panggilan untuk program `cat`:
   ```csh
   strace -c cat file.txt
   ```

3. Menyimpan output `strace` ke dalam fail:
   ```csh
   strace -o output.txt ls
   ```

4. Mengesan proses yang sedang berjalan dengan ID proses 1234:
   ```csh
   strace -p 1234
   ```

5. Mengesan hanya sistem panggilan `open` dan `close`:
   ```csh
   strace -e trace=open,close ls
   ```

## Tips
- Gunakan pilihan `-c` untuk mendapatkan ringkasan statistik yang berguna tanpa terlalu banyak maklumat.
- Simpan output ke dalam fail untuk analisis lebih lanjut jika outputnya terlalu panjang.
- Sentiasa periksa ID proses dengan `ps` sebelum menggunakan pilihan `-p` untuk memastikan anda mengesan proses yang betul.