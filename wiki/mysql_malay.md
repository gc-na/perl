# [Sistem Operasi] C Shell (csh) mysql Penggunaan: Mengurus pangkalan data MySQL

## Overview
Perintah `mysql` digunakan untuk berinteraksi dengan pangkalan data MySQL. Ia membolehkan pengguna untuk menjalankan arahan SQL, menguruskan pangkalan data, dan melaksanakan pelbagai tugas berkaitan pengurusan data.

## Usage
Sintaks asas bagi perintah `mysql` adalah seperti berikut:

```
mysql [options] [arguments]
```

## Common Options
- `-u [username]`: Menetapkan nama pengguna untuk log masuk ke MySQL.
- `-p`: Meminta kata laluan untuk pengguna yang ditetapkan.
- `-h [hostname]`: Menetapkan nama hos pangkalan data yang ingin disambungkan.
- `-D [database]`: Menetapkan pangkalan data yang ingin digunakan.
- `--execute`: Menjalankan arahan SQL yang diberikan secara langsung.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `mysql`:

1. **Sambung ke MySQL tanpa pangkalan data tertentu:**
   ```bash
   mysql -u root -p
   ```

2. **Sambung ke pangkalan data tertentu:**
   ```bash
   mysql -u user -p -D mydatabase
   ```

3. **Jalankan arahan SQL secara langsung:**
   ```bash
   mysql -u user -p --execute "SHOW TABLES;" -D mydatabase
   ```

4. **Muat naik fail SQL ke dalam pangkalan data:**
   ```bash
   mysql -u user -p mydatabase < backup.sql
   ```

## Tips
- Sentiasa gunakan pilihan `-p` untuk memastikan kata laluan tidak ditulis dalam arahan secara langsung.
- Gunakan pilihan `--execute` untuk menjalankan arahan SQL tanpa memasuki sesi interaktif.
- Pastikan anda mempunyai hak akses yang sesuai untuk pangkalan data yang ingin diuruskan.