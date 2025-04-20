# [Sistem Operasi] C Shell (csh) docker penggunaan: Mengurus kontena aplikasi

## Overview
Perintah `docker` digunakan untuk mengurus dan mengendalikan kontena aplikasi. Ia membolehkan pengguna untuk membina, menjalankan, dan mengurus aplikasi dalam persekitaran yang terasing, menjadikannya lebih mudah untuk mengurus kebergantungan dan persekitaran aplikasi.

## Usage
Sintaks asas untuk perintah `docker` adalah seperti berikut:

```
docker [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa yang digunakan dengan perintah `docker`:

- `run`: Menjalankan kontena baru.
- `ps`: Menunjukkan senarai kontena yang sedang berjalan.
- `stop`: Menghentikan kontena yang sedang berjalan.
- `rm`: Menghapus kontena.
- `images`: Menunjukkan senarai imej yang tersedia.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `docker`:

1. **Menjalankan kontena baru:**
   ```bash
   docker run hello-world
   ```

2. **Menunjukkan senarai kontena yang sedang berjalan:**
   ```bash
   docker ps
   ```

3. **Menghentikan kontena tertentu:**
   ```bash
   docker stop <container_id>
   ```

4. **Menghapus kontena:**
   ```bash
   docker rm <container_id>
   ```

5. **Menunjukkan senarai imej yang tersedia:**
   ```bash
   docker images
   ```

## Tips
- Sentiasa gunakan `docker ps -a` untuk melihat semua kontena, termasuk yang telah dihentikan.
- Gunakan tag pada imej anda untuk memudahkan pengurusan versi.
- Pastikan untuk membersihkan kontena dan imej yang tidak digunakan dengan `docker system prune` untuk menjimatkan ruang.