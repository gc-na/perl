# [Sistem Operasi] C Shell (csh) groupmod Penggunaan: Mengubah kumpulan pengguna

## Overview
Perintah `groupmod` digunakan untuk mengubah atribut kumpulan pengguna dalam sistem. Ini membolehkan pentadbir sistem untuk mengubah nama kumpulan, ID kumpulan, dan atribut lain yang berkaitan dengan kumpulan.

## Usage
Berikut adalah sintaks asas untuk perintah `groupmod`:

```csh
groupmod [options] [arguments]
```

## Common Options
- `-n, --new-name <nama_baru>`: Menetapkan nama baru untuk kumpulan.
- `-g, --gid <gid_baru>`: Menetapkan ID kumpulan baru.
- `-o`: Membenarkan penggunaan ID kumpulan yang tidak standard (ID yang lebih rendah daripada 1000).

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `groupmod`:

1. **Mengubah nama kumpulan**:
   ```csh
   groupmod -n nama_baru nama_lama
   ```

2. **Mengubah ID kumpulan**:
   ```csh
   groupmod -g 2000 nama_kumpulan
   ```

3. **Mengubah nama dan ID kumpulan secara serentak**:
   ```csh
   groupmod -n nama_baru -g 2000 nama_lama
   ```

## Tips
- Pastikan anda mempunyai hak akses yang mencukupi untuk menggunakan `groupmod`, biasanya sebagai pengguna root.
- Selalu buat salinan sandaran fail konfigurasi kumpulan sebelum membuat perubahan.
- Periksa kumpulan yang ada dengan menggunakan perintah `getent group` untuk memastikan perubahan dilakukan dengan betul.