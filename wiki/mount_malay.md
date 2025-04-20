# [Linux] C Shell (csh) mount penggunaan: [menyambung sistem fail]

## Overview
Perintah `mount` dalam C Shell (csh) digunakan untuk menyambungkan sistem fail ke dalam direktori tertentu dalam sistem pengendalian. Ini membolehkan pengguna mengakses fail dan direktori yang terdapat dalam sistem fail yang disambungkan.

## Usage
Berikut adalah sintaks asas untuk perintah `mount`:

```
mount [options] [arguments]
```

## Common Options
- `-t type` : Menentukan jenis sistem fail yang akan dipasang, seperti `ext4`, `ntfs`, dll.
- `-o options` : Menyediakan pilihan tambahan untuk pemasangan, seperti `ro` (read-only) atau `rw` (read-write).
- `-a` : Memasang semua sistem fail yang dinyatakan dalam fail `/etc/fstab`.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `mount`:

1. **Menyambung sistem fail dengan jenis tertentu**:
   ```csh
   mount -t ext4 /dev/sda1 /mnt/mydisk
   ```

2. **Menyambung sistem fail sebagai read-only**:
   ```csh
   mount -o ro /dev/sdb1 /mnt/readonly
   ```

3. **Menyambung semua sistem fail dari fstab**:
   ```csh
   mount -a
   ```

4. **Menyambung USB drive**:
   ```csh
   mount /dev/sdc1 /mnt/usb
   ```

## Tips
- Sentiasa pastikan anda mempunyai hak akses yang diperlukan untuk menyambung sistem fail.
- Gunakan pilihan `-o ro` jika anda ingin mengelakkan sebarang perubahan pada sistem fail yang disambungkan.
- Semak direktori pemasangan selepas menggunakan perintah `mount` untuk memastikan ia disambungkan dengan betul.