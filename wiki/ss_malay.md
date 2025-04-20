# [Sistem Operasi] C Shell (csh) ss: [perintah untuk melihat soket]

## Overview
Perintah `ss` digunakan untuk memaparkan informasi tentang soket yang sedang aktif di sistem. Ia membolehkan pengguna untuk melihat sambungan rangkaian, termasuk soket TCP dan UDP, serta statusnya.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `ss`:

```csh
ss [options] [arguments]
```

## Common Options
- `-t`: Menunjukkan soket TCP.
- `-u`: Menunjukkan soket UDP.
- `-l`: Menunjukkan soket yang sedang mendengar.
- `-p`: Menunjukkan proses yang menggunakan soket.
- `-n`: Menunjukkan alamat dan nombor port dalam format numerik, bukan nama.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `ss`:

1. **Melihat semua soket TCP:**
   ```csh
   ss -t
   ```

2. **Melihat semua soket UDP:**
   ```csh
   ss -u
   ```

3. **Melihat soket yang sedang mendengar:**
   ```csh
   ss -l
   ```

4. **Melihat soket dengan proses yang berkaitan:**
   ```csh
   ss -p
   ```

5. **Melihat semua soket dengan alamat dan nombor port dalam format numerik:**
   ```csh
   ss -n
   ```

## Tips
- Gunakan kombinasi pilihan untuk mendapatkan maklumat yang lebih spesifik, seperti `ss -t -l` untuk melihat soket TCP yang sedang mendengar.
- Sentiasa gunakan pilihan `-n` untuk mempercepatkan proses, terutamanya jika anda tidak memerlukan nama host.
- Periksa secara berkala soket yang aktif untuk memastikan tiada sambungan yang tidak diingini.