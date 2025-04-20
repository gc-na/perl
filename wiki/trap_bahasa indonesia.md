# [Sistem Operasi] C Shell (csh) trap Penggunaan: Mengelola sinyal dalam skrip

## Overview
Perintah `trap` dalam C Shell (csh) digunakan untuk menangani sinyal tertentu yang diterima oleh skrip. Dengan menggunakan `trap`, Anda dapat menentukan tindakan yang harus diambil ketika sinyal tertentu diterima, seperti menghentikan skrip atau membersihkan sumber daya sebelum keluar.

## Usage
Berikut adalah sintaks dasar dari perintah `trap`:

```csh
trap [options] [arguments]
```

## Common Options
- `SIGINT`: Menangani sinyal interupsi (Ctrl+C).
- `SIGTERM`: Menangani sinyal terminasi.
- `EXIT`: Menentukan perintah yang dijalankan saat skrip keluar.

## Common Examples

### Contoh 1: Menangani Sinyal Interupsi
Menggunakan `trap` untuk menangani sinyal interupsi dan mencetak pesan sebelum keluar.

```csh
trap 'echo "Skrip dihentikan oleh pengguna"; exit' SIGINT
```

### Contoh 2: Membersihkan Sumber Daya
Menangani sinyal terminasi untuk membersihkan file sementara sebelum keluar.

```csh
trap 'rm -f /tmp/tempfile; exit' SIGTERM
```

### Contoh 3: Menjalankan Perintah Saat Keluar
Menjalankan perintah tertentu saat skrip selesai dieksekusi.

```csh
trap 'echo "Skrip selesai"; exit' EXIT
```

## Tips
- Selalu gunakan `trap` untuk menangani sinyal yang mungkin mengganggu eksekusi skrip Anda.
- Pastikan untuk menguji skrip Anda dengan berbagai sinyal untuk memastikan bahwa `trap` berfungsi seperti yang diharapkan.
- Gunakan `trap` dengan hati-hati, terutama saat menentukan tindakan untuk sinyal yang dapat menghentikan skrip, agar tidak kehilangan data penting.