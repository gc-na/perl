# [Sistem Operasi] C Shell (csh) sftp Penggunaan: Memindahkan fail dengan selamat

## Overview
Perintah `sftp` (Secure File Transfer Protocol) digunakan untuk memindahkan fail dengan selamat antara komputer melalui rangkaian. Ia menyediakan cara yang selamat untuk menghantar dan menerima fail menggunakan protokol SSH.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `sftp`:

```csh
sftp [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan umum untuk `sftp`:

- `-b batchfile` : Menggunakan fail batch untuk menjalankan perintah secara automatik.
- `-o option` : Menetapkan pilihan tertentu untuk sambungan.
- `-P port` : Menentukan nombor port yang digunakan untuk sambungan.
- `-v` : Mengaktifkan mod verbose untuk mendapatkan maklumat lebih lanjut tentang sambungan.

## Common Examples
Berikut adalah beberapa contoh praktikal menggunakan `sftp`:

1. **Menyambung ke pelayan SFTP:**
   ```csh
   sftp user@hostname
   ```

2. **Menghantar fail ke pelayan:**
   ```csh
   sftp user@hostname
   put localfile.txt
   ```

3. **Mendapatkan fail dari pelayan:**
   ```csh
   sftp user@hostname
   get remotefile.txt
   ```

4. **Menggunakan fail batch:**
   ```csh
   sftp -b batchfile.txt user@hostname
   ```

## Tips
- Sentiasa gunakan sambungan yang selamat dengan `sftp` untuk melindungi data anda.
- Gunakan pilihan `-v` untuk menyelesaikan masalah jika sambungan tidak berjaya.
- Simpan maklumat sambungan dalam fail konfigurasi untuk kemudahan akses di masa hadapan.