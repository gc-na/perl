# [Linux] C Shell (csh) yum: Mengurus pakej perisian

## Overview
Perintah `yum` (Yellowdog Updater, Modified) digunakan dalam sistem pengendalian Linux untuk mengurus pemasangan, kemas kini, dan penghapusan pakej perisian. Ia memudahkan pengguna untuk mengendalikan pakej dengan mengurus kebergantungan secara automatik.

## Usage
Sintaks asas untuk menggunakan `yum` adalah seperti berikut:

```
yum [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa yang boleh digunakan dengan `yum`:

- `install`: Memasang pakej baru.
- `remove`: Menghapuskan pakej yang sedia ada.
- `update`: Mengemas kini pakej yang telah dipasang.
- `search`: Mencari pakej dalam repositori.
- `info`: Menunjukkan maklumat tentang pakej tertentu.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `yum`:

1. **Memasang pakej baru**:
   ```bash
   yum install httpd
   ```

2. **Menghapuskan pakej**:
   ```bash
   yum remove httpd
   ```

3. **Mengemas kini semua pakej**:
   ```bash
   yum update
   ```

4. **Mencari pakej**:
   ```bash
   yum search nginx
   ```

5. **Menunjukkan maklumat tentang pakeg**:
   ```bash
   yum info vim
   ```

## Tips
- Sentiasa jalankan `yum update` secara berkala untuk memastikan sistem anda sentiasa terkini.
- Gunakan `yum clean all` untuk membersihkan cache dan ruang simpanan yang tidak diperlukan.
- Sebelum memasang pakej baru, gunakan `yum info [package]` untuk melihat maklumat dan kebergantungan pakeg tersebut.