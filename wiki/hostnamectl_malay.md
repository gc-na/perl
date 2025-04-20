# [Linux] C Shell (csh) hostnamectl Penggunaan: Mengurus nama hos dan maklumat sistem

## Overview
Perintah `hostnamectl` digunakan untuk mengurus nama hos dan maklumat sistem dalam sistem operasi Linux. Ia membolehkan pengguna untuk melihat dan mengubah nama hos serta mendapatkan maklumat berkaitan sistem dengan mudah.

## Usage
Sintaks asas untuk perintah `hostnamectl` adalah seperti berikut:

```csh
hostnamectl [options] [arguments]
```

## Common Options
- `set-hostname`: Mengubah nama hos sistem.
- `status`: Menunjukkan maklumat tentang nama hos dan status sistem.
- `set-icon-name`: Mengubah nama ikon untuk sistem.
- `set-chassis`: Menetapkan jenis chasis sistem (contohnya, desktop, laptop, server).

## Common Examples
1. **Menunjukkan maklumat nama hos dan sistem:**
   ```csh
   hostnamectl status
   ```

2. **Mengubah nama hos sistem:**
   ```csh
   hostnamectl set-hostname nama-baru
   ```

3. **Menetapkan jenis chasis sistem:**
   ```csh
   hostnamectl set-chassis laptop
   ```

4. **Mengubah nama ikon sistem:**
   ```csh
   hostnamectl set-icon-name ikon-baru
   ```

## Tips
- Pastikan anda mempunyai hak akses yang diperlukan untuk mengubah nama hos.
- Selepas mengubah nama hos, mungkin perlu untuk memulakan semula sistem agar perubahan berkuat kuasa sepenuhnya.
- Gunakan `hostnamectl status` selepas membuat perubahan untuk memastikan semuanya telah dikemas kini dengan betul.