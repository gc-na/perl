# [Sistem Operasi] C Shell (csh) psql Penggunaan: Mengakses dan mengurus pangkalan data PostgreSQL

## Overview
Perintah `psql` adalah alat baris perintah untuk berinteraksi dengan pangkalan data PostgreSQL. Ia membolehkan pengguna untuk menjalankan arahan SQL, mengurus pangkalan data, dan melakukan pelbagai operasi lain berkaitan dengan pengurusan data.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `psql`:

```
psql [options] [arguments]
```

## Common Options
- `-h` : Menentukan hos pangkalan data.
- `-U` : Menentukan nama pengguna untuk sambungan.
- `-d` : Menentukan nama pangkalan data yang ingin disambungkan.
- `-p` : Menentukan port untuk sambungan.
- `-f` : Menjalankan arahan dari fail.

## Common Examples
Berikut adalah beberapa contoh penggunaan `psql`:

1. **Sambungkan ke pangkalan data dengan nama pengguna dan hos tertentu:**
   ```bash
   psql -h localhost -U username -d database_name
   ```

2. **Jalankan arahan SQL dari fail:**
   ```bash
   psql -U username -d database_name -f script.sql
   ```

3. **Tunjukkan senarai semua pangkalan data:**
   ```bash
   psql -U username -c "\l"
   ```

4. **Jalankan arahan SQL secara langsung:**
   ```bash
   psql -U username -d database_name -c "SELECT * FROM table_name;"
   ```

## Tips
- Sentiasa gunakan nama pengguna dan kata laluan yang kuat untuk keselamatan.
- Gunakan pilihan `-f` untuk menjalankan skrip SQL yang panjang untuk mengelakkan kesilapan pengetikan.
- Manfaatkan arahan `\?` dalam psql untuk mendapatkan senarai arahan dan pilihan yang tersedia.