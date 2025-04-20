# [Linux] C Shell (csh) du Penggunaan: Mengira saiz direktori dan fail

## Overview
Perintah `du` (disk usage) digunakan untuk mengira dan memaparkan saiz penggunaan ruang disk oleh fail dan direktori. Ia membantu pengguna untuk memahami berapa banyak ruang yang digunakan oleh fail-fail tertentu dalam sistem.

## Usage
Sintaks asas untuk perintah `du` adalah seperti berikut:

```csh
du [options] [arguments]
```

## Common Options
- `-h`: Memaparkan saiz dalam format yang mudah dibaca (contohnya, KB, MB).
- `-s`: Menunjukkan jumlah saiz untuk setiap argumen yang diberikan, bukan untuk setiap fail atau subdirektori.
- `-a`: Menunjukkan saiz untuk semua fail, bukan hanya direktori.
- `-c`: Mengira jumlah keseluruhan untuk semua argumen yang diberikan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `du`:

1. **Mengira saiz direktori semasa**:
   ```csh
   du
   ```

2. **Mengira saiz direktori dengan format yang mudah dibaca**:
   ```csh
   du -h
   ```

3. **Mengira saiz untuk direktori tertentu**:
   ```csh
   du /path/to/directory
   ```

4. **Menunjukkan saiz semua fail dan direktori**:
   ```csh
   du -a
   ```

5. **Menunjukkan jumlah keseluruhan untuk direktori tertentu**:
   ```csh
   du -sh /path/to/directory
   ```

## Tips
- Gunakan pilihan `-h` untuk memudahkan pemahaman saiz fail, terutamanya jika anda bekerja dengan fail yang besar.
- Untuk mendapatkan ringkasan cepat tentang penggunaan ruang disk, pilihan `-s` sangat berguna.
- Jika anda ingin melihat penggunaan ruang disk untuk semua fail dalam direktori, gunakan pilihan `-a` untuk mendapatkan maklumat yang lebih terperinci.