# [Sistem Operasi] C Shell (csh) last: Menunjukkan log masuk pengguna

## Overview
Perintah `last` dalam C Shell digunakan untuk memaparkan senarai log masuk pengguna yang telah dilakukan pada sistem. Ia menunjukkan maklumat tentang pengguna, termasuk nama pengguna, terminal yang digunakan, dan waktu log masuk serta log keluar.

## Usage
Berikut adalah sintaks asas untuk perintah `last`:

```
last [options] [arguments]
```

## Common Options
- `-n [number]`: Menunjukkan hanya bilangan log masuk terbaru yang ditentukan.
- `-R`: Mengabaikan nama host dan hanya menunjukkan nama pengguna dan waktu log masuk.
- `-f [file]`: Menggunakan fail log yang ditentukan sebagai sumber data.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `last`:

1. **Menunjukkan semua log masuk pengguna:**
   ```csh
   last
   ```

2. **Menunjukkan 5 log masuk terbaru:**
   ```csh
   last -n 5
   ```

3. **Mengabaikan nama host:**
   ```csh
   last -R
   ```

4. **Menggunakan fail log tertentu:**
   ```csh
   last -f /var/log/wtmp
   ```

## Tips
- Gunakan `last` secara berkala untuk memantau aktiviti log masuk pengguna dan memastikan keselamatan sistem.
- Jika anda ingin melihat log keluar pengguna, perhatikan bahawa `last` juga menunjukkan waktu log keluar jika tersedia.
- Anda boleh mengarahkan output ke fail untuk analisis lebih lanjut dengan menggunakan pengalihan, contohnya:
   ```csh
   last > log_masuk.txt
   ```