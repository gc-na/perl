# [Sistem Operasi] C Shell (csh) docker-compose Penggunaan: Mengelola aplikasi berbasis Docker

## Overview
Perintah `docker-compose` digunakan untuk mendefinisikan dan menjalankan aplikasi multi-container Docker. Dengan menggunakan file konfigurasi YAML, pengguna dapat dengan mudah mengatur, mengelola, dan menjalankan beberapa kontainer sebagai satu kesatuan.

## Usage
Berikut adalah sintaks dasar untuk menggunakan `docker-compose`:

```bash
docker-compose [options] [arguments]
```

## Common Options
- `up`: Membangun dan menjalankan kontainer sesuai dengan definisi dalam file `docker-compose.yml`.
- `down`: Menghentikan dan menghapus kontainer, jaringan, dan volume yang dibuat oleh `up`.
- `build`: Membangun atau membangun ulang layanan yang ditentukan dalam file `docker-compose.yml`.
- `logs`: Melihat log dari kontainer yang sedang berjalan.
- `ps`: Menampilkan daftar kontainer yang sedang berjalan dan statusnya.

## Common Examples
Berikut adalah beberapa contoh penggunaan `docker-compose`:

1. **Menjalankan aplikasi**:
   ```bash
   docker-compose up
   ```

2. **Menjalankan aplikasi di latar belakang**:
   ```bash
   docker-compose up -d
   ```

3. **Menghentikan dan menghapus kontainer**:
   ```bash
   docker-compose down
   ```

4. **Melihat log dari kontainer**:
   ```bash
   docker-compose logs
   ```

5. **Membangun ulang layanan**:
   ```bash
   docker-compose build
   ```

## Tips
- Selalu pastikan bahwa file `docker-compose.yml` Anda terstruktur dengan benar untuk menghindari kesalahan saat menjalankan perintah.
- Gunakan opsi `-d` untuk menjalankan kontainer di latar belakang, sehingga Anda dapat terus menggunakan terminal untuk perintah lain.
- Manfaatkan perintah `docker-compose logs` untuk memantau aplikasi Anda dan mendeteksi masalah dengan cepat.