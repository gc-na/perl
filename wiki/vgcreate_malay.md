# [Linux] C Shell (csh) vgcreate Penggunaan: Membuat kumpulan volum baru

## Overview
Perintah `vgcreate` digunakan untuk membuat kumpulan volum (volume group) baru dalam sistem pengurusan penyimpanan LVM (Logical Volume Manager). Kumpulan volum ini membolehkan pengguna menguruskan ruang penyimpanan secara lebih fleksibel dan efisien.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `vgcreate`:

```csh
vgcreate [options] [nama_kumpulan_volum] [peranti]
```

## Common Options
- `-s, --stripes <n>`: Menentukan bilangan jalur (stripes) untuk kumpulan volum.
- `-p, --pe-size <size>`: Menentukan saiz unit pengagihan (physical extent) untuk kumpulan volum.
- `-n, --noudevsync`: Mengabaikan pengesanan peranti semasa mencipta kumpulan volum.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `vgcreate`:

1. **Membuat kumpulan volum baru dengan satu peranti:**
   ```csh
   vgcreate my_volume_group /dev/sdb1
   ```

2. **Membuat kumpulan volum baru dengan saiz unit pengagihan tertentu:**
   ```csh
   vgcreate -p 16m my_volume_group /dev/sdb1
   ```

3. **Membuat kumpulan volum dengan beberapa peranti:**
   ```csh
   vgcreate my_volume_group /dev/sdb1 /dev/sdc1
   ```

## Tips
- Pastikan peranti yang ingin digunakan telah diformat dan tidak sedang digunakan oleh sistem lain.
- Sentiasa semak status kumpulan volum selepas mencipta dengan menggunakan perintah `vgs` untuk memastikan ia telah dicipta dengan betul.
- Gunakan pilihan `-s` untuk meningkatkan prestasi jika anda menggunakan peranti yang menyokong jalur (striping).