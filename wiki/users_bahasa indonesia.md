# [Sistem Operasi] Pengguna C Shell (csh): Mengelola pengguna sistem

## Overview
Perintah `users` dalam C Shell (csh) digunakan untuk menampilkan daftar nama pengguna yang sedang aktif di sistem. Ini berguna untuk mengetahui siapa saja yang sedang login dan aktif pada saat tertentu.

## Usage
Berikut adalah sintaks dasar dari perintah `users`:

```csh
users [options] [arguments]
```

## Common Options
- `-n`: Menampilkan nama pengguna tanpa duplikasi.
- `-r`: Menampilkan hanya pengguna yang sedang aktif.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `users`:

1. Menampilkan semua pengguna yang sedang login:
   ```csh
   users
   ```

2. Menampilkan pengguna yang sedang login tanpa duplikasi:
   ```csh
   users -n
   ```

3. Menampilkan hanya pengguna yang aktif:
   ```csh
   users -r
   ```

## Tips
- Gunakan opsi `-n` jika Anda ingin menghindari tampilan nama pengguna yang sama lebih dari sekali.
- Perintah ini sangat berguna dalam skrip untuk memantau aktivitas pengguna di sistem.
- Kombinasikan dengan perintah lain seperti `who` untuk mendapatkan informasi lebih lengkap tentang sesi pengguna.