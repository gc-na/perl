# [Sistem Operasi] C Shell (csh) strace Penggunaan: Melacak panggilan sistem

## Overview
Perintah `strace` digunakan untuk melacak panggilan sistem dan sinyal yang diterima oleh suatu proses. Ini sangat berguna untuk debugging dan menganalisis bagaimana program berinteraksi dengan kernel.

## Usage
Berikut adalah sintaks dasar dari perintah `strace`:

```csh
strace [options] [arguments]
```

## Common Options
- `-c`: Menampilkan ringkasan statistik dari panggilan sistem yang dilakukan.
- `-e trace=<event>`: Mengatur jenis panggilan sistem yang ingin dilacak, seperti `file`, `network`, dll.
- `-o <file>`: Menyimpan output ke dalam file yang ditentukan.
- `-p <pid>`: Melacak proses yang sedang berjalan dengan ID proses tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan `strace`:

1. Melacak semua panggilan sistem dari program `ls`:
   ```csh
   strace ls
   ```

2. Menyimpan output `strace` ke dalam file:
   ```csh
   strace -o output.txt ls
   ```

3. Melacak hanya panggilan sistem yang berkaitan dengan file:
   ```csh
   strace -e trace=file ls
   ```

4. Melacak proses yang sudah berjalan dengan ID 1234:
   ```csh
   strace -p 1234
   ```

5. Menampilkan ringkasan statistik dari panggilan sistem:
   ```csh
   strace -c ls
   ```

## Tips
- Gunakan opsi `-o` untuk menyimpan hasil ke dalam file agar lebih mudah dianalisis.
- Kombinasikan opsi `-e` untuk fokus pada jenis panggilan sistem tertentu yang relevan dengan masalah yang Anda hadapi.
- Pastikan Anda memiliki izin yang diperlukan untuk melacak proses, terutama untuk proses yang dijalankan oleh pengguna lain.