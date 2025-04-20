# [Sistem Operasi] C Shell (csh) rsync Penggunaan: Menyalin dan menyinkronkan file

## Overview
Perintah `rsync` digunakan untuk menyalin dan menyinkronkan file atau direktori antara dua lokasi, baik di dalam mesin yang sama maupun antara mesin yang berbeda melalui jaringan. `rsync` sangat efisien karena hanya mentransfer perubahan yang terjadi pada file, bukan seluruh file.

## Usage
Berikut adalah sintaks dasar dari perintah `rsync`:

```csh
rsync [options] [source] [destination]
```

## Common Options
Berikut adalah beberapa opsi umum yang sering digunakan dengan `rsync`:

- `-a`: Archive mode; menyalin file dan direktori secara rekursif dan mempertahankan atribut file.
- `-v`: Verbose; menampilkan informasi lebih detail selama proses transfer.
- `-z`: Mengompres data selama transfer untuk menghemat bandwidth.
- `-r`: Menyalin direktori secara rekursif.
- `--delete`: Menghapus file di tujuan yang tidak ada di sumber.

## Common Examples
Berikut adalah beberapa contoh penggunaan `rsync`:

1. Menyalin file dari direktori lokal ke direktori tujuan:
   ```csh
   rsync -av /path/to/source/file.txt /path/to/destination/
   ```

2. Menyalin seluruh direktori ke lokasi lain:
   ```csh
   rsync -av /path/to/source/directory/ /path/to/destination/directory/
   ```

3. Menyalin file ke server jarak jauh menggunakan SSH:
   ```csh
   rsync -avz /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
   ```

4. Menyinkronkan direktori dan menghapus file yang tidak ada di sumber:
   ```csh
   rsync -av --delete /path/to/source/directory/ /path/to/destination/directory/
   ```

## Tips
- Selalu gunakan opsi `-n` (dry run) sebelum melakukan transfer untuk melihat apa yang akan dilakukan tanpa benar-benar menyalin file.
- Gunakan `-z` saat mentransfer file besar melalui jaringan untuk menghemat bandwidth.
- Pastikan untuk menambahkan trailing slash (`/`) pada direktori sumber jika ingin menyalin isi direktori, bukan direktori itu sendiri.