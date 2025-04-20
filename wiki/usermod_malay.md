# [Linux] C Shell (csh) usermod Penggunaan: Mengubah maklumat pengguna

## Overview
Perintah `usermod` dalam C Shell (csh) digunakan untuk mengubah maklumat pengguna dalam sistem. Ia membolehkan pentadbir sistem untuk mengubah pelbagai atribut pengguna seperti nama, kumpulan, dan direktori rumah.

## Usage
Berikut adalah sintaks asas untuk perintah `usermod`:

```csh
usermod [options] [arguments]
```

## Common Options
- `-l`: Mengubah nama log masuk pengguna.
- `-d`: Mengubah direktori rumah pengguna.
- `-g`: Mengubah kumpulan utama pengguna.
- `-aG`: Menambah pengguna ke dalam kumpulan tambahan tanpa mengeluarkannya dari kumpulan lain.

## Common Examples
Berikut adalah beberapa contoh penggunaan `usermod`:

1. **Mengubah nama log masuk pengguna:**
   ```csh
   usermod -l nama_baru nama_lama
   ```

2. **Mengubah direktori rumah pengguna:**
   ```csh
   usermod -d /path/ke/direktori_baru nama_pengguna
   ```

3. **Mengubah kumpulan utama pengguna:**
   ```csh
   usermod -g kumpulan_baru nama_pengguna
   ```

4. **Menambah pengguna ke dalam kumpulan tambahan:**
   ```csh
   usermod -aG kumpulan_tambahan nama_pengguna
   ```

## Tips
- Sentiasa buat salinan sandaran maklumat pengguna sebelum melakukan perubahan.
- Pastikan anda mempunyai hak akses pentadbir untuk menggunakan perintah `usermod`.
- Periksa perubahan dengan menggunakan perintah `id nama_pengguna` selepas mengubah maklumat pengguna.