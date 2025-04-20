# [Sistem Operasi] C Shell (csh) dnf Penggunaan: Mengurus pakej perisian

## Overview
Perintah `dnf` adalah pengurus pakej yang digunakan dalam sistem pengendalian Linux untuk memasang, mengemas kini, dan menghapus perisian. Ia menggantikan `yum` dan menawarkan prestasi yang lebih baik serta pengurusan ketergantungan yang lebih efisien.

## Usage
Sintaks asas untuk menggunakan `dnf` adalah seperti berikut:

```bash
dnf [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `dnf`:

- `install`: Memasang pakej baru.
- `remove`: Menghapus pakej yang telah dipasang.
- `update`: Mengemas kini pakej yang telah dipasang ke versi terbaru.
- `search`: Mencari pakej dalam repositori.
- `info`: Menunjukkan maklumat tentang pakej tertentu.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `dnf`:

1. **Memasang pakej baru**:
   ```bash
   dnf install nama-pakej
   ```

2. **Menghapus pakej**:
   ```bash
   dnf remove nama-pakej
   ```

3. **Mengemas kini semua pakej**:
   ```bash
   dnf update
   ```

4. **Mencari pakej**:
   ```bash
   dnf search nama-pakej
   ```

5. **Menunjukkan maklumat tentang pakej**:
   ```bash
   dnf info nama-pakej
   ```

## Tips
- Sentiasa jalankan `dnf update` secara berkala untuk memastikan sistem anda sentiasa terkini.
- Gunakan `dnf search` untuk mencari pakej jika anda tidak pasti tentang nama tepatnya.
- Anda boleh menggunakan `dnf history` untuk melihat sejarah tindakan yang telah dilakukan oleh `dnf`, termasuk pemasangan dan penghapusan pakej.