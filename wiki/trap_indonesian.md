# [Sistem Operasi] C Shell (csh) trap: Menangani sinyal dan kejadian

## Overview
Perintah `trap` dalam C Shell (csh) digunakan untuk menangani sinyal dan kejadian tertentu yang terjadi saat eksekusi skrip. Dengan menggunakan `trap`, Anda dapat menentukan tindakan yang harus diambil ketika sinyal tertentu diterima, seperti menghentikan skrip atau menjalankan perintah pembersihan.

## Usage
Berikut adalah sintaks dasar dari perintah `trap`:

```csh
trap [options] [arguments]
```

## Common Options
- `signal`: Menentukan sinyal yang ingin ditangani, seperti `INT` untuk interupsi.
- `command`: Perintah yang akan dijalankan ketika sinyal diterima.

## Common Examples
Berikut adalah beberapa contoh penggunaan `trap`:

### Contoh 1: Menangani Interupsi
Menangani sinyal interupsi (Ctrl+C) untuk mencetak pesan sebelum keluar.

```csh
trap 'echo "Skrip dihentikan"; exit' INT
```

### Contoh 2: Membersihkan File Sementara
Menghapus file sementara saat skrip dihentikan.

```csh
trap 'rm -f /tmp/tempfile; exit' HUP
```

### Contoh 3: Menangani Sinyal Keluar
Menangani sinyal keluar untuk mencetak pesan.

```csh
trap 'echo "Skrip selesai"; exit' EXIT
```

## Tips
- Selalu gunakan `trap` untuk membersihkan sumber daya yang digunakan oleh skrip Anda.
- Uji skrip Anda dengan berbagai sinyal untuk memastikan bahwa `trap` berfungsi seperti yang diharapkan.
- Gunakan `trap` di bagian awal skrip untuk memastikan bahwa semua sinyal ditangani dengan benar.