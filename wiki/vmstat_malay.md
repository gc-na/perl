# [Sistem Operasi] C Shell (csh) vmstat Penggunaan: Memantau statistik sistem

## Overview
Perintah `vmstat` digunakan untuk memantau statistik sistem dalam sistem operasi Unix dan Linux. Ia memberikan maklumat mengenai penggunaan memori, proses, dan aktiviti I/O, yang membantu pengguna memahami prestasi sistem mereka.

## Usage
Sintaks asas untuk menggunakan perintah `vmstat` adalah seperti berikut:

```csh
vmstat [options] [arguments]
```

## Common Options
- `-a`: Menunjukkan statistik memori yang lebih terperinci.
- `-n`: Mengelakkan pengulangan output.
- `-s`: Menunjukkan statistik sistem secara ringkas.
- `-m`: Menunjukkan statistik memori berasaskan objek.

## Common Examples
Berikut adalah beberapa contoh penggunaan `vmstat`:

1. Menunjukkan statistik sistem secara asas:
   ```csh
   vmstat
   ```

2. Menunjukkan statistik setiap 5 saat:
   ```csh
   vmstat 5
   ```

3. Menunjukkan statistik memori yang lebih terperinci:
   ```csh
   vmstat -a
   ```

4. Menunjukkan statistik sistem secara ringkas:
   ```csh
   vmstat -s
   ```

## Tips
- Gunakan `vmstat` bersama dengan perintah lain seperti `top` untuk mendapatkan gambaran yang lebih lengkap mengenai prestasi sistem.
- Perhatikan nilai `si` dan `so` dalam output untuk memahami pertukaran memori (swap) yang berlaku.
- Jalankan `vmstat` secara berkala untuk memantau perubahan dalam prestasi sistem semasa waktu puncak.