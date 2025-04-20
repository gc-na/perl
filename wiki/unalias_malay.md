# [Sistem Operasi] C Shell (csh) unalias: Menghapus alias yang ditetapkan

## Overview
Perintah `unalias` dalam C Shell (csh) digunakan untuk menghapus alias yang telah ditetapkan sebelumnya. Alias adalah nama pendek yang digunakan untuk menggantikan perintah yang lebih panjang atau kompleks, dan `unalias` membolehkan pengguna untuk membatalkan alias tersebut.

## Usage
Berikut adalah sintaks asas untuk perintah `unalias`:

```
unalias [options] [arguments]
```

## Common Options
- `-a` : Menghapus semua alias yang ditetapkan.
- `-m` : Menghapus alias yang mengandungi nama tertentu yang ditetapkan.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `unalias`:

1. **Menghapus alias tertentu:**
   ```csh
   unalias ll
   ```
   Perintah ini akan menghapus alias `ll` jika ia telah ditetapkan.

2. **Menghapus semua alias:**
   ```csh
   unalias -a
   ```
   Perintah ini akan menghapus semua alias yang telah ditetapkan dalam sesi semasa.

3. **Menghapus alias berdasarkan pola:**
   ```csh
   unalias -m 'l*'
   ```
   Perintah ini akan menghapus semua alias yang namanya bermula dengan huruf `l`.

## Tips
- Sentiasa semak alias yang telah ditetapkan sebelum menggunakan `unalias` dengan perintah `alias` untuk mengelakkan penghapusan yang tidak disengajakan.
- Gunakan `unalias -a` dengan hati-hati, kerana ini akan menghapus semua alias tanpa amaran.
- Jika anda sering menggunakan alias, pertimbangkan untuk menyimpannya dalam fail konfigurasi seperti `.cshrc` untuk kemudahan akses di masa hadapan.