# [Sistem Operasi] C Shell (csh) parted: Mengurus partisi cakera

## Overview
Perintah `parted` digunakan untuk mengurus partisi cakera. Ia membolehkan pengguna untuk mencipta, memadam, dan mengubah saiz partisi pada cakera keras dengan cara yang mudah dan berkesan.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `parted`:

```csh
parted [options] [arguments]
```

## Common Options
- `-l` : Menunjukkan senarai semua cakera dan partisi yang ada.
- `mkpart` : Mencipta partisi baru.
- `rm` : Memadam partisi yang sedia ada.
- `resizepart` : Mengubah saiz partisi yang sedia ada.
- `print` : Menunjukkan maklumat tentang partisi yang ada.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `parted`:

1. **Menunjukkan senarai cakera dan partisi:**
   ```csh
   parted -l
   ```

2. **Mencipta partisi baru:**
   ```csh
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

3. **Memadam partisi:**
   ```csh
   parted /dev/sda rm 1
   ```

4. **Mengubah saiz partisi:**
   ```csh
   parted /dev/sda resizepart 1 200MiB
   ```

5. **Menunjukkan maklumat tentang partisi:**
   ```csh
   parted /dev/sda print
   ```

## Tips
- Sentiasa buat salinan sandaran data penting sebelum mengubah partisi untuk mengelakkan kehilangan data.
- Gunakan `print` untuk memeriksa keadaan partisi sebelum dan selepas melakukan sebarang perubahan.
- Pastikan anda mempunyai hak akses yang mencukupi (seperti root) untuk menjalankan perintah `parted`.