# [Sistem Operasi] C Shell (csh) sqlite3 Penggunaan: Mengelola basis data SQLite

## Overview
Perintah `sqlite3` digunakan untuk mengelola dan berinteraksi dengan basis data SQLite. Dengan perintah ini, pengguna dapat menjalankan kueri SQL, mengelola tabel, dan melakukan berbagai operasi lain pada basis data.

## Usage
Berikut adalah sintaks dasar dari perintah `sqlite3`:

```bash
sqlite3 [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `sqlite3`:

- `-help`: Menampilkan bantuan dan informasi tentang penggunaan perintah.
- `-version`: Menampilkan versi SQLite yang sedang digunakan.
- `-init <file>`: Menjalankan skrip SQL dari file yang ditentukan saat memulai.
- `-batch`: Menjalankan dalam mode batch, cocok untuk skrip tanpa interaksi pengguna.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan `sqlite3`:

1. **Membuat basis data baru:**
   ```bash
   sqlite3 mydatabase.db
   ```

2. **Menjalankan kueri SQL untuk membuat tabel:**
   ```bash
   sqlite3 mydatabase.db "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);"
   ```

3. **Menambahkan data ke tabel:**
   ```bash
   sqlite3 mydatabase.db "INSERT INTO users (name) VALUES ('Alice');"
   ```

4. **Mengambil data dari tabel:**
   ```bash
   sqlite3 mydatabase.db "SELECT * FROM users;"
   ```

5. **Menghapus tabel:**
   ```bash
   sqlite3 mydatabase.db "DROP TABLE users;"
   ```

## Tips
- Selalu buat cadangan basis data sebelum melakukan perubahan besar.
- Gunakan opsi `-init` untuk menjalankan skrip SQL yang kompleks secara otomatis.
- Manfaatkan mode batch untuk menjalankan serangkaian perintah tanpa interaksi manual, terutama saat mengelola basis data besar.