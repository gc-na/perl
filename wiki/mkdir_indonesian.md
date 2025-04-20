# [Sistem Operasi] C Shell (csh) mkdir Penggunaan: Membuat direktori baru

## Overview
Perintah `mkdir` digunakan untuk membuat direktori baru di dalam sistem file. Ini adalah cara yang efisien untuk mengorganisir file dan folder dalam struktur yang diinginkan.

## Usage
Berikut adalah sintaks dasar dari perintah `mkdir`:

```
mkdir [options] [arguments]
```

## Common Options
- `-p`: Membuat direktori induk secara otomatis jika belum ada.
- `-m`: Mengatur izin akses untuk direktori yang dibuat.
- `-v`: Menampilkan pesan yang menunjukkan direktori yang telah dibuat.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `mkdir`:

1. Membuat direktori baru bernama `folder_baru`:
   ```csh
   mkdir folder_baru
   ```

2. Membuat beberapa direktori sekaligus:
   ```csh
   mkdir folder1 folder2 folder3
   ```

3. Membuat direktori dengan struktur induk:
   ```csh
   mkdir -p folder_induk/folder_anak
   ```

4. Membuat direktori dengan izin akses tertentu:
   ```csh
   mkdir -m 755 folder_izin
   ```

5. Menampilkan pesan saat direktori dibuat:
   ```csh
   mkdir -v folder_ditampilkan
   ```

## Tips
- Selalu gunakan opsi `-p` jika Anda ingin membuat beberapa tingkat direktori sekaligus untuk menghindari kesalahan.
- Periksa izin akses direktori setelah membuatnya untuk memastikan bahwa Anda memiliki hak yang sesuai.
- Gunakan opsi `-v` saat belajar atau saat scripting untuk mendapatkan umpan balik tentang apa yang terjadi.