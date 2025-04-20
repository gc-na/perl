# [Sistem Pengendalian] C Shell (csh) docker-compose penggunaan: Mengurus aplikasi berbilang kontena

## Overview
Perintah `docker-compose` digunakan untuk mengurus aplikasi yang terdiri daripada beberapa kontena Docker. Dengan `docker-compose`, anda boleh mendefinisikan dan menjalankan aplikasi yang terdiri daripada pelbagai perkhidmatan dengan mudah menggunakan satu fail konfigurasi.

## Usage
Berikut adalah sintaks asas untuk menggunakan `docker-compose`:

```bash
docker-compose [options] [arguments]
```

## Common Options
- `up`: Mula dan jalankan semua perkhidmatan yang ditakrifkan dalam fail `docker-compose.yml`.
- `down`: Hentikan dan padamkan semua perkhidmatan yang sedang berjalan.
- `build`: Bangunkan imej untuk perkhidmatan yang ditakrifkan.
- `logs`: Paparkan log untuk semua perkhidmatan.
- `exec`: Jalankan perintah dalam kontena yang sedang berjalan.

## Common Examples
Berikut adalah beberapa contoh penggunaan `docker-compose`:

1. **Mula semua perkhidmatan**:
   ```bash
   docker-compose up
   ```

2. **Hentikan semua perkhidmatan**:
   ```bash
   docker-compose down
   ```

3. **Bangunkan imej perkhidmatan**:
   ```bash
   docker-compose build
   ```

4. **Paparkan log perkhidmatan**:
   ```bash
   docker-compose logs
   ```

5. **Jalankan perintah dalam kontena**:
   ```bash
   docker-compose exec <service_name> <command>
   ```

## Tips
- Sentiasa pastikan anda berada dalam direktori yang mengandungi fail `docker-compose.yml` sebelum menjalankan perintah.
- Gunakan `-d` bersama `up` untuk menjalankan perkhidmatan dalam latar belakang.
- Periksa dokumen rasmi untuk pilihan dan parameter tambahan yang mungkin berguna untuk keperluan khusus anda.