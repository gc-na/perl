# [Linux] C Shell (csh) lsblk Penggunaan: Menampilkan informasi blok perangkat

## Overview
Perintah `lsblk` digunakan untuk menampilkan informasi tentang perangkat blok yang terpasang di sistem. Ini termasuk disk, partisi, dan perangkat penyimpanan lainnya. Dengan `lsblk`, pengguna dapat dengan mudah melihat struktur perangkat penyimpanan yang ada.

## Usage
Sintaks dasar dari perintah `lsblk` adalah sebagai berikut:

```csh
lsblk [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `lsblk`:

- `-a`, `--all`: Menampilkan semua perangkat, termasuk yang tidak terpasang.
- `-f`, `--fs`: Menampilkan informasi sistem file pada perangkat.
- `-l`, `--list`: Menampilkan output dalam format daftar.
- `-o`, `--output`: Menentukan kolom output yang ingin ditampilkan.
- `-p`, `--paths`: Menampilkan jalur perangkat lengkap.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan `lsblk`:

1. Menampilkan semua perangkat blok:
   ```csh
   lsblk
   ```

2. Menampilkan semua perangkat termasuk yang tidak terpasang:
   ```csh
   lsblk -a
   ```

3. Menampilkan informasi sistem file pada perangkat:
   ```csh
   lsblk -f
   ```

4. Menampilkan output dalam format daftar:
   ```csh
   lsblk -l
   ```

5. Menentukan kolom output yang ingin ditampilkan:
   ```csh
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
   ```

## Tips
- Gunakan opsi `-f` untuk mendapatkan informasi sistem file yang lebih lengkap, terutama saat Anda perlu mengetahui jenis sistem file dari perangkat.
- Kombinasikan opsi untuk mendapatkan output yang lebih spesifik sesuai kebutuhan Anda.
- Perhatikan bahwa output `lsblk` dapat membantu dalam pemecahan masalah terkait penyimpanan dan partisi.