# [SUSE] C Shell (csh) zypper: Pengurus pakej untuk sistem SUSE

## Overview
Zypper adalah alat pengurus pakej untuk sistem operasi SUSE yang membolehkan pengguna untuk memasang, mengemas kini, dan menghapus pakej perisian dengan mudah. Ia juga membolehkan pengguna mengurus repositori dan mengendalikan ketergantungan pakej.

## Usage
Berikut adalah sintaks asas untuk menggunakan zypper:

```
zypper [options] [arguments]
```

## Common Options
- `install`: Memasang pakej baru.
- `remove`: Menghapus pakeg yang sedia ada.
- `update`: Mengemas kini pakej yang telah dipasang.
- `search`: Mencari pakej dalam repositori.
- `refresh`: Menyegarkan senarai repositori untuk mendapatkan maklumat terkini.

## Common Examples
1. **Memasang pakej**:
   ```bash
   zypper install nama-pakej
   ```

2. **Menghapus pakeg**:
   ```bash
   zypper remove nama-pakej
   ```

3. **Mengemas kini semua pakej**:
   ```bash
   zypper update
   ```

4. **Mencari pakej**:
   ```bash
   zypper search nama-pakej
   ```

5. **Menyegarkan repositori**:
   ```bash
   zypper refresh
   ```

## Tips
- Sentiasa gunakan `zypper refresh` sebelum mengemas kini atau memasang pakej untuk memastikan anda mempunyai maklumat terkini.
- Gunakan `zypper search` untuk mencari pakej yang mungkin anda perlukan sebelum memasangnya.
- Untuk mengelakkan konflik, pastikan semua pakej yang berkaitan dikemas kini secara berkala.