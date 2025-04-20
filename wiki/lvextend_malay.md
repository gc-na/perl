# [Linux] C Shell (csh) lvextend: Memperluas saiz logical volume

## Overview
Perintah `lvextend` digunakan untuk memperluas saiz logical volume dalam sistem pengurusan storan LVM (Logical Volume Manager). Dengan menggunakan perintah ini, pengguna dapat menambah ruang pada logical volume yang sedia ada tanpa perlu memformat atau menghapus data yang ada.

## Usage
Berikut adalah sintaks asas untuk perintah `lvextend`:

```csh
lvextend [options] [arguments]
```

## Common Options
- `-L +size`: Menambah saiz tertentu pada logical volume.
- `-l +number`: Menambah bilangan logical extents pada logical volume.
- `-r`: Secara automatik mengembangkan sistem fail yang berkaitan dengan logical volume selepas ia diperluas.
- `-n`: Menentukan nama baru untuk logical volume.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `lvextend`:

1. Menambah 10GB pada logical volume bernama `my_volume`:
   ```csh
   lvextend -L +10G /dev/vg_name/my_volume
   ```

2. Menambah 5 logical extents pada logical volume:
   ```csh
   lvextend -l +5 /dev/vg_name/my_volume
   ```

3. Memperluas logical volume dan secara automatik mengembangkan sistem fail:
   ```csh
   lvextend -r -L +20G /dev/vg_name/my_volume
   ```

4. Mengubah nama logical volume:
   ```csh
   lvextend -n new_volume_name /dev/vg_name/my_volume
   ```

## Tips
- Sentiasa pastikan bahawa anda mempunyai sandaran data sebelum melakukan pengubahsuaian pada logical volume.
- Gunakan pilihan `-r` untuk mengelakkan langkah tambahan dalam mengembangkan sistem fail selepas memperluas logical volume.
- Periksa ruang yang tersedia dalam volume group sebelum menambah saiz logical volume untuk mengelakkan kesilapan.