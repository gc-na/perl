# [Sistem Operasi] C Shell (csh) strace Penggunaan: Melacak panggilan sistem

## Overview
Perintah `strace` digunakan untuk melacak panggilan sistem dan sinyal yang diterima oleh proses. Ini sangat berguna untuk debugging dan menganalisis bagaimana program berinteraksi dengan kernel dan sumber daya sistem.

## Usage
Berikut adalah sintaks dasar dari perintah `strace`:

```csh
strace [options] [arguments]
```

## Common Options
- `-c`: Menghitung statistik panggilan sistem dan menampilkan ringkasan.
- `-e trace=<event>`: Melacak hanya jenis panggilan sistem tertentu, seperti `open`, `read`, atau `write`.
- `-p <pid>`: Melacak proses yang sudah berjalan berdasarkan ID proses (PID) yang diberikan.
- `-o <file>`: Mengalihkan output ke file yang ditentukan.

## Common Examples
Berikut adalah beberapa contoh penggunaan `strace`:

1. Melacak semua panggilan sistem dari program `ls`:
   ```csh
   strace ls
   ```

2. Menghitung statistik panggilan sistem dari program `cat`:
   ```csh
   strace -c cat file.txt
   ```

3. Melacak hanya panggilan sistem `open` dari program `grep`:
   ```csh
   strace -e trace=open grep "text" file.txt
   ```

4. Melacak proses yang sudah berjalan dengan PID 1234:
   ```csh
   strace -p 1234
   ```

5. Mengalihkan output `strace` ke file `output.txt`:
   ```csh
   strace -o output.txt ls
   ```

## Tips
- Gunakan opsi `-c` untuk mendapatkan ringkasan yang lebih mudah dibaca dari panggilan sistem yang dilakukan oleh program.
- Jika Anda hanya tertarik pada panggilan sistem tertentu, gunakan opsi `-e trace=<event>` untuk mempersempit output.
- Saat melacak proses yang sudah berjalan, pastikan Anda memiliki izin yang sesuai untuk mengakses proses tersebut.