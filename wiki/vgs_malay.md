# [Sistem Pengendalian] C Shell (csh) vgs: [menunjukkan maklumat kumpulan volum]

## Overview
Perintah `vgs` digunakan dalam sistem pengurusan storan untuk menunjukkan maklumat mengenai kumpulan volum (volume groups) dalam sistem Linux. Ia memberikan pandangan ringkas tentang status dan atribut kumpulan volum yang ada.

## Usage
Berikut adalah sintaks asas bagi perintah `vgs`:

```
vgs [options] [arguments]
```

## Common Options
- `-o`: Menentukan lajur yang ingin dipaparkan.
- `-n`: Menunjukkan nama kumpulan volum sahaja.
- `-P`: Memaparkan output dalam format yang lebih padat.
- `--units`: Menetapkan unit untuk ukuran yang dipaparkan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `vgs`:

1. **Menunjukkan maklumat semua kumpulan volum:**
   ```bash
   vgs
   ```

2. **Menunjukkan maklumat dengan lajur tertentu:**
   ```bash
   vgs -o vg_name,vg_size,vg_free
   ```

3. **Menunjukkan nama kumpulan volum sahaja:**
   ```bash
   vgs -n
   ```

4. **Memaparkan output dalam format padat:**
   ```bash
   vgs -P
   ```

5. **Menetapkan unit untuk ukuran yang dipaparkan:**
   ```bash
   vgs --units g
   ```

## Tips
- Sentiasa gunakan pilihan `-o` untuk menyesuaikan output kepada maklumat yang anda perlukan.
- Gunakan pilihan `-P` jika anda ingin mendapatkan output yang lebih ringkas dan mudah dibaca.
- Pastikan anda mempunyai keizinan yang sesuai untuk menjalankan perintah ini, kerana ia memerlukan akses kepada maklumat sistem.