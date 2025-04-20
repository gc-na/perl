# [Linux] C Shell (csh) lvextend Penggunaan: Memperbesar ukuran logical volume

## Overview
Perintah `lvextend` digunakan untuk memperbesar ukuran logical volume dalam sistem manajemen volume logis (LVM). Dengan menggunakan perintah ini, pengguna dapat menambah ruang penyimpanan pada volume yang sudah ada tanpa kehilangan data.

## Usage
Berikut adalah sintaks dasar dari perintah `lvextend`:

```bash
lvextend [options] [arguments]
```

## Common Options
- `-L +size`: Menambah ukuran volume dengan ukuran yang ditentukan.
- `-l +number_of_extents`: Menambah ukuran volume dengan jumlah extent yang ditentukan.
- `-r`: Secara otomatis memperluas filesystem setelah memperbesar logical volume.
- `-n new_name`: Mengubah nama logical volume.

## Common Examples
Berikut adalah beberapa contoh penggunaan `lvextend`:

1. **Menambah ukuran logical volume sebesar 10GB:**
   ```bash
   lvextend -L +10G /dev/vg01/lv01
   ```

2. **Menambah ukuran logical volume dengan jumlah extent:**
   ```bash
   lvextend -l +100 /dev/vg01/lv01
   ```

3. **Memperbesar logical volume dan secara otomatis memperluas filesystem:**
   ```bash
   lvextend -r -L +5G /dev/vg01/lv01
   ```

4. **Mengubah nama logical volume:**
   ```bash
   lvextend -n lv_new /dev/vg01/lv01
   ```

## Tips
- Selalu pastikan untuk memeriksa ruang yang tersedia sebelum memperbesar logical volume.
- Gunakan opsi `-r` untuk memperluas filesystem secara otomatis, sehingga Anda tidak perlu melakukannya secara manual.
- Lakukan backup data penting sebelum melakukan perubahan pada logical volume untuk menghindari kehilangan data.