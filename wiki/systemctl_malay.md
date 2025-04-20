# [Sistem Operasi] C Shell (csh) systemctl: Mengurus perkhidmatan sistem

## Overview
Perintah `systemctl` digunakan dalam sistem pengendalian Linux untuk mengurus dan mengawal perkhidmatan sistem dan unit. Ia membolehkan pengguna untuk memulakan, menghentikan, dan menyemak status perkhidmatan serta menguruskan konfigurasi sistem.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `systemctl`:

```
systemctl [options] [arguments]
```

## Common Options
- `start`: Memulakan perkhidmatan.
- `stop`: Menghentikan perkhidmatan.
- `restart`: Menghidupkan semula perkhidmatan.
- `status`: Menunjukkan status perkhidmatan.
- `enable`: Mengaktifkan perkhidmatan untuk dimulakan secara automatik pada boot.
- `disable`: Menonaktifkan perkhidmatan daripada dimulakan secara automatik pada boot.

## Common Examples
Berikut adalah beberapa contoh penggunaan `systemctl`:

1. **Memulakan perkhidmatan**
   ```bash
   systemctl start nama_perkhidmatan
   ```

2. **Menghentikan perkhidmatan**
   ```bash
   systemctl stop nama_perkhidmatan
   ```

3. **Menghidupkan semula perkhidmatan**
   ```bash
   systemctl restart nama_perkhidmatan
   ```

4. **Semak status perkhidmatan**
   ```bash
   systemctl status nama_perkhidmatan
   ```

5. **Mengaktifkan perkhidmatan pada boot**
   ```bash
   systemctl enable nama_perkhidmatan
   ```

6. **Menonaktifkan perkhidmatan pada boot**
   ```bash
   systemctl disable nama_perkhidmatan
   ```

## Tips
- Sentiasa semak status perkhidmatan selepas menjalankan perintah untuk memastikan ia berfungsi seperti yang diharapkan.
- Gunakan `systemctl list-units` untuk melihat semua unit yang sedang berjalan.
- Untuk mendapatkan maklumat lanjut tentang perkhidmatan tertentu, anda boleh menggunakan `systemctl show nama_perkhidmatan`.