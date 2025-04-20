# [Linux] C Shell (csh) mkswap: Membuat ruang tukar

## Overview
Perintah `mkswap` digunakan untuk menyiapkan ruang tukar (swap space) pada sistem Linux. Ruang tukar ini berfungsi sebagai memori tambahan yang digunakan ketika RAM penuh, membantu meningkatkan prestasi sistem.

## Usage
Berikut adalah sintaks asas untuk perintah `mkswap`:

```csh
mkswap [options] [arguments]
```

## Common Options
- `-f`: Memaksa pembuatan ruang tukar walaupun terdapat kesalahan.
- `-L label`: Memberi label kepada ruang tukar yang dibuat.
- `-p priority`: Menetapkan keutamaan untuk ruang tukar yang baru.

## Common Examples
Berikut adalah beberapa contoh penggunaan `mkswap`:

1. **Membuat ruang tukar dari fail**:
   ```csh
   dd if=/dev/zero of=/swapfile bs=1M count=1024
   mkswap /swapfile
   ```

2. **Membuat ruang tukar dari partisi**:
   ```csh
   mkswap /dev/sdX1
   ```

3. **Menetapkan label pada ruang tukar**:
   ```csh
   mkswap -L my_swap /dev/sdX1
   ```

4. **Menetapkan keutamaan untuk ruang tukar**:
   ```csh
   mkswap -p 10 /dev/sdX1
   ```

## Tips
- Pastikan untuk mengaktifkan ruang tukar selepas membuatnya dengan menggunakan perintah `swapon`.
- Sentiasa semak ruang tukar yang ada dengan perintah `swapon -s` untuk memastikan ia berfungsi dengan baik.
- Gunakan fail swap di lokasi yang mempunyai ruang yang cukup untuk mengelakkan masalah prestasi.