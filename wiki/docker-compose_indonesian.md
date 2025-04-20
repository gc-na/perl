# [Sistem Operasi] C Shell (csh) docker-compose Penggunaan: Mengelola aplikasi Docker

## Overview
Perintah `docker-compose` digunakan untuk mendefinisikan dan menjalankan aplikasi multi-kontainer Docker. Dengan menggunakan file konfigurasi YAML, pengguna dapat mengatur layanan, jaringan, dan volume yang diperlukan untuk aplikasi mereka dengan mudah.

## Usage
Berikut adalah sintaks dasar dari perintah `docker-compose`:

```bash
docker-compose [options] [arguments]
```

## Common Options
- `up`: Membangun, (re)start, dan menjalankan kontainer.
- `down`: Menghentikan dan menghapus kontainer, jaringan, dan volume yang dibuat oleh `up`.
- `build`: Membangun atau membangun ulang layanan.
- `logs`: Menampilkan log dari kontainer yang sedang berjalan.
- `ps`: Menampilkan status dari kontainer yang dikelola oleh docker-compose.

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

4. **Membangun ulang layanan**:
   ```bash
   docker-compose build
   ```

5. **Melihat log dari kontainer**:
   ```bash
   docker-compose logs
   ```

## Tips
- Selalu gunakan file `docker-compose.yml` untuk mendefinisikan konfigurasi aplikasi Anda agar lebih terstruktur.
- Gunakan opsi `-d` untuk menjalankan kontainer di latar belakang, sehingga terminal Anda tetap tersedia untuk perintah lain.
- Periksa status kontainer dengan `docker-compose ps` untuk memastikan semuanya berjalan dengan baik.