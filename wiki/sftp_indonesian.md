# [Sistem Operasi] C Shell (csh) sftp Penggunaan: Transfer file secara aman

## Overview
Perintah `sftp` (SSH File Transfer Protocol) digunakan untuk mentransfer file secara aman antara komputer lokal dan remote. Dengan menggunakan protokol SSH, `sftp` menyediakan cara yang aman untuk meng-upload dan meng-download file.

## Usage
Berikut adalah sintaks dasar dari perintah `sftp`:

```csh
sftp [options] [user@]host
```

## Common Options
- `-P port`: Menentukan port yang digunakan untuk koneksi.
- `-b batchfile`: Menggunakan file batch untuk menjalankan perintah secara otomatis.
- `-o option`: Mengatur opsi tambahan untuk koneksi SSH.

## Common Examples
Berikut adalah beberapa contoh penggunaan `sftp`:

1. **Koneksi ke server SFTP:**
   ```csh
   sftp user@hostname
   ```

2. **Meng-upload file ke server:**
   ```csh
   put localfile.txt
   ```

3. **Meng-download file dari server:**
   ```csh
   get remotefile.txt
   ```

4. **Meng-upload direktori secara rekursif:**
   ```csh
   put -r localdir
   ```

5. **Menggunakan port yang berbeda:**
   ```csh
   sftp -P 2222 user@hostname
   ```

## Tips
- Selalu gunakan `sftp` daripada `ftp` untuk menjaga keamanan data Anda.
- Gunakan opsi `-b` untuk menjalankan perintah secara otomatis jika Anda perlu melakukan banyak transfer.
- Periksa izin file dan direktori di server remote untuk memastikan Anda memiliki akses yang tepat.