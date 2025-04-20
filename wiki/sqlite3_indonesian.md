# [Sistem Operasi] C Shell (csh) sqlite3 Penggunaan: Mengelola database SQLite

## Overview
Perintah `sqlite3` digunakan untuk mengelola database SQLite. Dengan perintah ini, pengguna dapat membuat, mengedit, dan menjalankan kueri pada database SQLite melalui antarmuka baris perintah.

## Usage
Berikut adalah sintaks dasar untuk menggunakan perintah `sqlite3`:

```csh
sqlite3 [options] [arguments]
```

## Common Options
Beberapa opsi umum yang dapat digunakan dengan `sqlite3` antara lain:

- `-help`: Menampilkan bantuan dan informasi tentang penggunaan perintah.
- `-version`: Menampilkan versi dari SQLite yang sedang digunakan.
- `-init <file>`: Menjalankan skrip SQL dari file yang ditentukan saat memulai.
- `-batch`: Menjalankan dalam mode batch, yang tidak menampilkan prompt interaktif.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan perintah `sqlite3`:

### Membuat Database Baru
Untuk membuat database baru, Anda bisa menggunakan perintah berikut:

```csh
sqlite3 mydatabase.db
```

### Menjalankan Skrip SQL dari File
Jika Anda memiliki skrip SQL yang ingin dijalankan, gunakan opsi `-init`:

```csh
sqlite3 mydatabase.db -init script.sql
```

### Mengambil Data dari Tabel
Untuk mengambil data dari tabel, Anda bisa menggunakan kueri SQL:

```csh
sqlite3 mydatabase.db "SELECT * FROM mytable;"
```

### Menambahkan Data ke Tabel
Menambahkan data ke tabel dapat dilakukan dengan perintah berikut:

```csh
sqlite3 mydatabase.db "INSERT INTO mytable (column1, column2) VALUES ('value1', 'value2');"
```

## Tips
- Selalu buat cadangan database Anda sebelum melakukan perubahan besar.
- Gunakan opsi `-batch` saat menjalankan skrip untuk menghindari prompt interaktif yang tidak perlu.
- Pelajari sintaks SQL dasar untuk memaksimalkan penggunaan `sqlite3`.