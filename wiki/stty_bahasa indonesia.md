# [Sistem Operasi] C Shell (csh) stty: Mengatur terminal

## Overview
Perintah `stty` digunakan untuk mengubah dan mengatur pengaturan terminal dalam lingkungan shell. Dengan `stty`, pengguna dapat mengonfigurasi berbagai opsi terminal seperti pengaturan input, output, dan kontrol aliran.

## Usage
Berikut adalah sintaks dasar dari perintah `stty`:

```
stty [options] [arguments]
```

## Common Options
- `-a` : Menampilkan semua pengaturan terminal saat ini.
- `-g` : Menghasilkan pengaturan terminal dalam format yang dapat digunakan kembali.
- `erase` : Mengatur karakter penghapus.
- `kill` : Mengatur karakter untuk menghapus seluruh baris.
- `intr` : Mengatur karakter untuk interupsi (biasanya Ctrl+C).

## Common Examples
Berikut adalah beberapa contoh penggunaan `stty`:

1. Menampilkan semua pengaturan terminal saat ini:
   ```bash
   stty -a
   ```

2. Mengatur karakter penghapus menjadi `^H` (Backspace):
   ```bash
   stty erase ^H
   ```

3. Mengatur karakter interupsi menjadi `^C`:
   ```bash
   stty intr ^C
   ```

4. Menghasilkan pengaturan terminal dalam format yang dapat digunakan kembali:
   ```bash
   stty -g
   ```

5. Mengatur karakter untuk menghapus seluruh baris menjadi `^U`:
   ```bash
   stty kill ^U
   ```

## Tips
- Selalu periksa pengaturan terminal saat ini dengan `stty -a` sebelum melakukan perubahan.
- Simpan pengaturan terminal yang dihasilkan dengan `stty -g` jika Anda ingin mengembalikannya di lain waktu.
- Hati-hati saat mengubah karakter kontrol, karena dapat memengaruhi cara Anda berinteraksi dengan terminal.