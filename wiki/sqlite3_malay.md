# [Sistem Pengendalian] C Shell (csh) sqlite3 Penggunaan: Mengurus pangkalan data SQLite

## Overview
Perintah `sqlite3` digunakan untuk berinteraksi dengan pangkalan data SQLite. Ia membolehkan pengguna untuk menjalankan arahan SQL, membuat pangkalan data baru, dan menguruskan data dalam pangkalan data yang sedia ada.

## Usage
Sintaks asas untuk menggunakan perintah `sqlite3` adalah seperti berikut:

```csh
sqlite3 [options] [arguments]
```

## Common Options
- `-init <file>`: Menjalankan arahan dalam fail yang ditentukan selepas pangkalan data dibuka.
- `-header`: Menunjukkan nama lajur dalam output.
- `-csv`: Mengeluarkan hasil dalam format CSV.
- `-batch`: Menjalankan dalam mod batch tanpa interaksi pengguna.
- `-version`: Menunjukkan versi SQLite yang sedang digunakan.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `sqlite3`:

1. **Membuka pangkalan data**:
   ```csh
   sqlite3 mydatabase.db
   ```

2. **Menjalankan arahan SQL untuk mencipta jadual**:
   ```csh
   sqlite3 mydatabase.db "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);"
   ```

3. **Mengambil data dari jadual**:
   ```csh
   sqlite3 mydatabase.db "SELECT * FROM users;"
   ```

4. **Mengeluarkan hasil dalam format CSV**:
   ```csh
   sqlite3 -header -csv mydatabase.db "SELECT * FROM users;" > output.csv
   ```

5. **Menjalankan fail SQL**:
   ```csh
   sqlite3 mydatabase.db < script.sql
   ```

## Tips
- Sentiasa buat salinan sandaran pangkalan data sebelum melakukan perubahan besar.
- Gunakan pilihan `-header` untuk memudahkan pembacaan hasil query.
- Manfaatkan mod `-batch` untuk menjalankan skrip tanpa interaksi jika anda perlu menjalankan banyak arahan sekaligus.