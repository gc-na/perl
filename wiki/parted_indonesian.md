# [Sistem Operasi] C Shell (csh) parted: Mengelola partisi disk

## Overview
Perintah `parted` digunakan untuk mengelola partisi disk pada sistem operasi berbasis Unix. Dengan `parted`, pengguna dapat membuat, menghapus, dan mengubah ukuran partisi dengan mudah.

## Usage
Berikut adalah sintaks dasar dari perintah `parted`:

```bash
parted [options] [arguments]
```

## Common Options
- `-s`: Menjalankan `parted` dalam mode skrip, tanpa interaksi pengguna.
- `-l`: Menampilkan daftar semua disk dan partisi yang ada.
- `mkpart`: Membuat partisi baru.
- `rm`: Menghapus partisi yang ada.
- `resizepart`: Mengubah ukuran partisi yang sudah ada.

## Common Examples
Berikut adalah beberapa contoh penggunaan `parted`:

### Menampilkan daftar partisi
```bash
parted -l
```

### Membuat partisi baru
```bash
parted /dev/sda mkpart primary ext4 1GB 5GB
```

### Menghapus partisi
```bash
parted /dev/sda rm 1
```

### Mengubah ukuran partisi
```bash
parted /dev/sda resizepart 1 10GB
```

## Tips
- Selalu pastikan untuk mencadangkan data penting sebelum melakukan perubahan pada partisi.
- Gunakan opsi `-s` jika Anda ingin menjalankan perintah dalam skrip tanpa interaksi.
- Periksa kembali ukuran dan jenis partisi sebelum membuat atau mengubahnya untuk menghindari kehilangan data.