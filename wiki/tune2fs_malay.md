# [Linux] C Shell (csh) tune2fs Penggunaan: Mengubah parameter sistem fail ext2/ext3/ext4

## Overview
Perintah `tune2fs` digunakan untuk mengubah parameter sistem fail pada sistem fail ext2, ext3, dan ext4. Ia membolehkan pengguna untuk mengubah pelbagai tetapan yang berkaitan dengan sistem fail tanpa perlu memformat semula sistem fail tersebut.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `tune2fs`:

```csh
tune2fs [options] [arguments]
```

## Common Options
- `-c <count>`: Menetapkan bilangan maksimum pengesanan sistem fail sebelum pemeriksaan automatik dilakukan.
- `-i <interval>`: Menetapkan selang masa antara pemeriksaan sistem fail.
- `-m <reserved-blocks>`: Menetapkan peratusan blok yang disimpan untuk pengguna root.
- `-O <feature>`: Menambah ciri baru pada sistem fail.
- `-L <label>`: Menetapkan label untuk sistem fail.

## Common Examples
Berikut adalah beberapa contoh penggunaan `tune2fs`:

1. **Menetapkan bilangan maksimum pengesanan:**
   ```csh
   tune2fs -c 30 /dev/sda1
   ```

2. **Menetapkan selang masa pemeriksaan kepada 6 bulan:**
   ```csh
   tune2fs -i 6m /dev/sda1
   ```

3. **Menetapkan peratusan blok yang disimpan untuk root kepada 5%:**
   ```csh
   tune2fs -m 5 /dev/sda1
   ```

4. **Menambah ciri 'dir_index' pada sistem fail:**
   ```csh
   tune2fs -O dir_index /dev/sda1
   ```

5. **Menetapkan label sistem fail kepada "Data":**
   ```csh
   tune2fs -L Data /dev/sda1
   ```

## Tips
- Pastikan untuk membuat salinan sandaran data penting sebelum mengubah parameter sistem fail.
- Gunakan perintah `tune2fs -l /dev/sda1` untuk menyemak tetapan semasa sistem fail sebelum membuat perubahan.
- Hanya gunakan `tune2fs` pada sistem fail yang tidak sedang digunakan untuk mengelakkan kerosakan data.