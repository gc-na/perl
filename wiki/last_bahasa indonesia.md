# [Sistem Operasi] C Shell (csh) last: Menampilkan riwayat login pengguna

## Overview
Perintah `last` digunakan untuk menampilkan daftar login pengguna yang terakhir pada sistem. Ini memberikan informasi tentang pengguna yang telah masuk dan keluar, serta waktu dan durasi sesi mereka.

## Usage
Berikut adalah sintaks dasar dari perintah `last`:

```csh
last [options] [arguments]
```

## Common Options
- `-n <number>`: Menentukan jumlah entri terakhir yang ingin ditampilkan.
- `-R`: Menghilangkan nama host dari output.
- `-f <file>`: Menggunakan file tertentu untuk membaca data login, bukan file default.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `last`:

1. Menampilkan semua login terakhir:
   ```csh
   last
   ```

2. Menampilkan 5 login terakhir:
   ```csh
   last -n 5
   ```

3. Menampilkan login terakhir tanpa nama host:
   ```csh
   last -R
   ```

4. Menggunakan file log tertentu:
   ```csh
   last -f /var/log/wtmp
   ```

## Tips
- Gunakan opsi `-n` untuk membatasi jumlah entri yang ditampilkan, sehingga output lebih mudah dibaca.
- Periksa file log yang berbeda jika Anda ingin melihat riwayat login dari sumber yang berbeda.
- Jika Anda hanya tertarik pada sesi tertentu, Anda dapat menambahkan nama pengguna sebagai argumen untuk memfilter hasil.