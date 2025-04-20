# [Sistem Operasi] C Shell (csh) pengguna: [senarai pengguna]

## Overview
Perintah `users` dalam C Shell (csh) digunakan untuk memaparkan senarai nama pengguna yang sedang log masuk ke sistem. Ia memberikan gambaran ringkas tentang siapa yang sedang aktif pada masa tertentu.

## Usage
Berikut adalah sintaks asas untuk perintah `users`:

```
users [options] [arguments]
```

## Common Options
- `-n`: Menunjukkan bilangan pengguna yang sedang log masuk.
- `-r`: Menunjukkan hanya pengguna yang sedang aktif.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `users`:

1. **Menunjukkan senarai semua pengguna yang sedang log masuk:**
   ```csh
   users
   ```

2. **Menunjukkan bilangan pengguna yang sedang log masuk:**
   ```csh
   users -n
   ```

3. **Menunjukkan hanya pengguna yang aktif:**
   ```csh
   users -r
   ```

## Tips
- Gunakan perintah `who` jika anda memerlukan maklumat tambahan mengenai pengguna, seperti waktu log masuk dan terminal yang digunakan.
- Perintah `users` sangat berguna untuk pentadbir sistem yang ingin memantau aktiviti pengguna secara cepat.