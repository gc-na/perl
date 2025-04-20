# [Sistem Operasi] C Shell (csh) shutdown: Mematikan sistem

## Overview
Perintah `shutdown` dalam C Shell (csh) digunakan untuk mematikan sistem secara aman. Ia memberi amaran kepada pengguna dan menutup semua proses sebelum mematikan komputer, memastikan bahawa tiada data yang hilang.

## Usage
Berikut adalah sintaks asas untuk perintah `shutdown`:

```
shutdown [options] [arguments]
```

## Common Options
- `-h`: Mematikan sistem.
- `-r`: Menghidupkan semula sistem selepas mematikan.
- `-k`: Menghantar amaran kepada pengguna tanpa mematikan sistem.
- `+m`: Menjadualkan pematian dalam m minit.
- `hh:mm`: Menjadualkan pematian pada waktu tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `shutdown`:

1. Mematikan sistem segera:
   ```csh
   shutdown -h now
   ```

2. Menjadualkan pematian dalam 10 minit:
   ```csh
   shutdown +10
   ```

3. Menghidupkan semula sistem selepas mematikan:
   ```csh
   shutdown -r now
   ```

4. Menghantar amaran kepada pengguna tanpa mematikan:
   ```csh
   shutdown -k now
   ```

5. Menjadualkan pematian pada waktu tertentu (contoh: 22:00):
   ```csh
   shutdown 22:00
   ```

## Tips
- Pastikan untuk memberitahu pengguna lain sebelum mematikan sistem untuk mengelakkan kehilangan data.
- Gunakan pilihan `-k` untuk menghantar amaran sebelum melakukan pematian sebenar.
- Sentiasa simpan kerja anda sebelum menjalankan perintah `shutdown`.