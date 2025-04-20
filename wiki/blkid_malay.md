# [Linux] C Shell (csh) blkid Penggunaan: Menyenaraikan UUID dan jenis sistem fail

## Overview
Perintah `blkid` digunakan untuk mencari dan mencetak UUID (Universally Unique Identifier) serta jenis sistem fail untuk peranti penyimpanan yang tersedia. Ini berguna untuk mengenal pasti dan mengkonfigurasi peranti penyimpanan dalam sistem Linux.

## Usage
Berikut adalah sintaks asas untuk perintah `blkid`:

```bash
blkid [options] [arguments]
```

## Common Options
- `-o`: Menentukan format output, seperti `value`, `full`, atau `udev`.
- `-s`: Memilih atribut tertentu untuk ditunjukkan, seperti `UUID` atau `TYPE`.
- `-p`: Mengabaikan peranti yang tidak dapat diakses.
- `-c`: Menggunakan cache untuk mempercepat pencarian.

## Common Examples
Berikut adalah beberapa contoh penggunaan `blkid`:

1. **Mendapatkan maklumat semua peranti penyimpanan**:
   ```bash
   blkid
   ```

2. **Mendapatkan UUID untuk peranti tertentu**:
   ```bash
   blkid /dev/sda1
   ```

3. **Menampilkan hanya UUID dalam format nilai**:
   ```bash
   blkid -o value -s UUID /dev/sda1
   ```

4. **Menggunakan cache untuk mempercepat pencarian**:
   ```bash
   blkid -c /dev/null
   ```

## Tips
- Sentiasa gunakan `blkid` dengan hak akses yang sesuai untuk mendapatkan maklumat yang tepat tentang peranti penyimpanan.
- Gunakan pilihan `-o` untuk menyesuaikan output mengikut keperluan anda.
- Jika anda bekerja dengan banyak peranti, pertimbangkan untuk menggunakan cache untuk meningkatkan prestasi.