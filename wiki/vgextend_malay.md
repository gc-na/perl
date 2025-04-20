# [Linux] C Shell (csh) vgextend Penggunaan: Menambah ruang ke dalam kumpulan volum

## Overview
Perintah `vgextend` digunakan dalam pengurusan sistem fail untuk menambah ruang ke dalam kumpulan volum (volume group) di Linux. Ini membolehkan pengguna untuk mengembangkan kapasiti penyimpanan tanpa kehilangan data yang ada.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `vgextend`:

```
vgextend [options] [arguments]
```

## Common Options
- `-l, --extents`: Menentukan jumlah extents yang ingin ditambah.
- `-n, --no-activation`: Menambah ruang tanpa mengaktifkan kumpulan volum.
- `-f, --force`: Memaksa penambahan walaupun terdapat amaran.

## Common Examples
Berikut adalah beberapa contoh penggunaan `vgextend`:

1. Menambah satu atau lebih peranti ke dalam kumpulan volum:
   ```csh
   vgextend my_volume_group /dev/sdb1
   ```

2. Menambah beberapa peranti sekaligus:
   ```csh
   vgextend my_volume_group /dev/sdb1 /dev/sdc1
   ```

3. Menambah ruang dengan menggunakan pilihan `--extents`:
   ```csh
   vgextend -l +100 my_volume_group /dev/sdb1
   ```

4. Memaksa penambahan walaupun terdapat amaran:
   ```csh
   vgextend -f my_volume_group /dev/sdb1
   ```

## Tips
- Pastikan anda mempunyai sandaran data sebelum melakukan perubahan pada kumpulan volum.
- Periksa status kumpulan volum selepas penambahan untuk memastikan semuanya berjalan lancar.
- Gunakan pilihan `--no-activation` jika anda tidak ingin mengaktifkan kumpulan volum selepas penambahan.