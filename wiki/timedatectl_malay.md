# [Sistem Pengendalian] C Shell (csh) timedatectl: Mengurus waktu dan tarikh sistem

## Overview
Perintah `timedatectl` digunakan untuk mengurus dan mengkonfigurasi waktu serta tarikh pada sistem Linux. Ia membolehkan pengguna untuk melihat dan menetapkan waktu sistem, serta menguruskan pengaturan waktu dan zon waktu.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `timedatectl`:

```bash
timedatectl [options] [arguments]
```

## Common Options
- `status`: Menunjukkan status waktu dan tarikh semasa.
- `set-time`: Menetapkan waktu sistem kepada waktu yang ditentukan.
- `set-timezone`: Menetapkan zon waktu sistem.
- `list-timezones`: Menyenaraikan semua zon waktu yang tersedia.
- `set-ntp`: Mengaktifkan atau mematikan penyegerakan waktu melalui NTP (Network Time Protocol).

## Common Examples
Berikut adalah beberapa contoh penggunaan `timedatectl`:

1. **Menunjukkan status waktu dan tarikh semasa:**
   ```bash
   timedatectl status
   ```

2. **Menetapkan waktu sistem kepada 15:30 pada 1 Januari 2023:**
   ```bash
   timedatectl set-time '2023-01-01 15:30:00'
   ```

3. **Menetapkan zon waktu kepada Asia/Kuala_Lumpur:**
   ```bash
   timedatectl set-timezone Asia/Kuala_Lumpur
   ```

4. **Menyenaraikan semua zon waktu yang tersedia:**
   ```bash
   timedatectl list-timezones
   ```

5. **Mengaktifkan penyegerakan waktu melalui NTP:**
   ```bash
   timedatectl set-ntp true
   ```

## Tips
- Sentiasa semak status waktu dan tarikh selepas melakukan perubahan untuk memastikan ia telah diterapkan dengan betul.
- Gunakan `list-timezones` untuk memilih zon waktu yang tepat sebelum menetapkannya.
- Pastikan sistem anda disambungkan ke internet jika anda menggunakan NTP untuk penyegerakan waktu.