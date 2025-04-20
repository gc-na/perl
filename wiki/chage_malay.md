# [Sistem Operasi] C Shell (csh) chage: Mengurus tarikh luput kata laluan pengguna

## Overview
Perintah `chage` digunakan untuk mengurus dan mengubah tetapan tarikh luput kata laluan bagi pengguna dalam sistem Linux. Ia membolehkan pentadbir sistem untuk menetapkan bila kata laluan perlu ditukar dan memberikan maklumat tentang status kata laluan pengguna.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `chage`:

```csh
chage [options] [arguments]
```

## Common Options
- `-l, --list`: Menunjukkan maklumat tentang tarikh luput kata laluan pengguna.
- `-m, --mindays`: Menetapkan bilangan hari minimum antara perubahan kata laluan.
- `-M, --maxdays`: Menetapkan bilangan hari maksimum sebelum kata laluan perlu ditukar.
- `-I, --inactive`: Menetapkan bilangan hari selepas kata laluan tamat tempoh sebelum akaun menjadi tidak aktif.
- `-E, --expire`: Menetapkan tarikh tamat untuk akaun pengguna.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `chage`:

1. **Menunjukkan maklumat tarikh luput kata laluan untuk pengguna tertentu:**

   ```csh
   chage -l username
   ```

2. **Menetapkan tarikh luput maksimum kata laluan kepada 90 hari:**

   ```csh
   chage -M 90 username
   ```

3. **Menetapkan bilangan hari minimum antara perubahan kata laluan kepada 7 hari:**

   ```csh
   chage -m 7 username
   ```

4. **Menetapkan tarikh tamat untuk akaun pengguna:**

   ```csh
   chage -E 2024-12-31 username
   ```

## Tips
- Sentiasa semak maklumat kata laluan pengguna selepas membuat perubahan untuk memastikan tetapan adalah seperti yang diingini.
- Gunakan pilihan `-l` secara berkala untuk memantau status kata laluan pengguna.
- Pastikan untuk memberikan notifikasi kepada pengguna tentang perubahan yang akan datang pada kata laluan mereka untuk mengelakkan sebarang gangguan.