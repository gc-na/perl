# [Linux] C Shell (csh) groups: Menunjukkan keahlian pengguna dalam kumpulan

## Overview
Perintah `groups` dalam C Shell (csh) digunakan untuk menunjukkan kumpulan (group) yang dimiliki oleh pengguna semasa. Ia memberikan maklumat tentang keahlian kumpulan yang berkaitan dengan pengguna yang sedang aktif.

## Usage
Berikut adalah sintaks asas untuk perintah `groups`:

```
groups [options] [arguments]
```

## Common Options
- `-a`: Menunjukkan semua kumpulan yang ada, termasuk yang tidak aktif.
- `username`: Menunjukkan kumpulan untuk pengguna tertentu jika nama pengguna diberikan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `groups`:

1. **Menunjukkan kumpulan untuk pengguna semasa:**
   ```csh
   groups
   ```

2. **Menunjukkan kumpulan untuk pengguna tertentu:**
   ```csh
   groups john
   ```

3. **Menunjukkan semua kumpulan termasuk yang tidak aktif:**
   ```csh
   groups -a
   ```

## Tips
- Gunakan perintah `groups` tanpa sebarang argumen untuk cepat melihat keahlian kumpulan anda.
- Untuk melihat keahlian kumpulan pengguna lain, pastikan anda mempunyai hak akses yang sesuai.
- Perintah ini berguna untuk pengurusan pengguna dan pengesahan akses dalam sistem.