# [Sistem Operasi] C Shell (csh) who: Menunjukkan pengguna yang sedang log masuk

## Overview
Perintah `who` dalam C Shell (csh) digunakan untuk menampilkan senarai pengguna yang sedang log masuk ke sistem. Ia memberikan maklumat tentang pengguna, termasuk nama pengguna, terminal yang mereka gunakan, dan waktu mereka log masuk.

## Usage
Berikut adalah sintaks asas untuk perintah `who`:

```
who [options] [arguments]
```

## Common Options
- `-a`: Menunjukkan semua maklumat termasuk pengguna yang tidak aktif.
- `-b`: Menunjukkan waktu terakhir sistem dimulakan.
- `-q`: Menunjukkan senarai pengguna yang log masuk dan jumlah mereka.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `who`:

1. **Menampilkan semua pengguna yang sedang log masuk:**
   ```csh
   who
   ```

2. **Menampilkan waktu terakhir sistem dimulakan:**
   ```csh
   who -b
   ```

3. **Menampilkan senarai pengguna dan jumlah mereka:**
   ```csh
   who -q
   ```

4. **Menampilkan semua maklumat pengguna termasuk yang tidak aktif:**
   ```csh
   who -a
   ```

## Tips
- Gunakan `who` secara berkala untuk memantau aktiviti pengguna di sistem.
- Kombinasikan `who` dengan perintah lain seperti `grep` untuk mencari pengguna tertentu.
- Perhatikan output `who` untuk mengesan sesi yang tidak aktif atau pengguna yang tidak dikenali.