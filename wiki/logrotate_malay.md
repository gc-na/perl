# [Linux] C Shell (csh) logrotate Penggunaan: Mengurus fail log

## Overview
Perintah `logrotate` digunakan untuk mengurus dan memutar fail log dalam sistem operasi. Ia membolehkan pengguna untuk mengatur saiz fail log dan mengelakkan fail log daripada menjadi terlalu besar dengan memindahkan atau menghapus fail log lama secara automatik.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `logrotate`:

```bash
logrotate [options] [arguments]
```

## Common Options
- `-f`: Memaksa logrotate untuk memproses fail log walaupun tidak ada keperluan untuk melakukannya.
- `-s`: Menentukan fail status yang digunakan oleh logrotate untuk menyimpan maklumat tentang pemputaran log.
- `-v`: Mengaktifkan mod verbose, yang menunjukkan maklumat tambahan semasa proses pemputaran.

## Common Examples
Berikut adalah beberapa contoh penggunaan `logrotate`:

1. **Menggunakan fail konfigurasi lalai**:
   ```bash
   logrotate /etc/logrotate.conf
   ```

2. **Memaksa pemputaran log**:
   ```bash
   logrotate -f /etc/logrotate.conf
   ```

3. **Menjalankan logrotate dengan mod verbose**:
   ```bash
   logrotate -v /etc/logrotate.conf
   ```

4. **Menggunakan fail status tertentu**:
   ```bash
   logrotate -s /var/lib/logrotate/status /etc/logrotate.conf
   ```

## Tips
- Pastikan untuk mengkonfigurasi fail logrotate dengan betul untuk mengelakkan kehilangan data log penting.
- Sentiasa semak fail status untuk memastikan logrotate berfungsi dengan baik.
- Gunakan mod verbose semasa pengujian untuk mendapatkan maklumat lebih lanjut tentang proses pemputaran.