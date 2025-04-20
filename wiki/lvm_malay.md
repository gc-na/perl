# [Sistem Operasi] C Shell (csh) lvm: Mengurus Logical Volume Management

## Overview
Perintah `lvm` digunakan untuk mengurus Logical Volume Management (LVM) dalam sistem Linux. Ia membolehkan pengguna untuk membuat, mengubah, dan menghapus logical volumes, serta menguruskan ruang penyimpanan secara lebih fleksibel.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `lvm`:

```
lvm [options] [arguments]
```

## Common Options
- `create`: Membuat logical volume baru.
- `remove`: Menghapus logical volume yang sedia ada.
- `extend`: Menambah ruang kepada logical volume.
- `reduce`: Mengurangkan ruang daripada logical volume.
- `list`: Menunjukkan senarai logical volumes yang ada.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `lvm`:

1. **Membuat Logical Volume Baru**
   ```bash
   lvm create -n my_volume -L 10G my_volume_group
   ```

2. **Menghapus Logical Volume**
   ```bash
   lvm remove my_volume
   ```

3. **Menambah Ruang kepada Logical Volume**
   ```bash
   lvm extend -L +5G my_volume
   ```

4. **Mengurangkan Ruang daripada Logical Volume**
   ```bash
   lvm reduce -L -2G my_volume
   ```

5. **Menunjukkan Senarai Logical Volumes**
   ```bash
   lvm list
   ```

## Tips
- Sentiasa buat salinan data penting sebelum melakukan pengubahsuaian pada logical volumes.
- Gunakan perintah `lvm list` untuk memeriksa status dan ruang yang ada sebelum membuat sebarang perubahan.
- Pastikan anda memahami kesan daripada menambah atau mengurangkan ruang pada logical volumes untuk mengelakkan kehilangan data.