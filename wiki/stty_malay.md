# [Sistem Operasi] C Shell (csh) stty: Mengubah tetapan terminal

## Overview
Perintah `stty` digunakan untuk mengubah dan memaparkan tetapan terminal dalam C Shell. Ia membolehkan pengguna untuk mengkonfigurasi cara terminal berfungsi, termasuk pengendalian input dan output.

## Usage
Berikut adalah sintaks asas untuk perintah `stty`:

```csh
stty [options] [arguments]
```

## Common Options
- `-a` : Memaparkan semua tetapan terminal semasa.
- `-g` : Mengeluarkan tetapan terminal dalam format yang boleh digunakan semula.
- `-F` : Menentukan fail peranti terminal yang ingin digunakan.
- `intr` : Menetapkan kunci untuk interupsi (biasanya Ctrl+C).
- `erase` : Menetapkan kunci untuk menghapuskan karakter (biasanya Ctrl+H).

## Common Examples
1. **Memaparkan tetapan terminal semasa:**
   ```csh
   stty -a
   ```

2. **Menetapkan kunci interupsi kepada Ctrl+C:**
   ```csh
   stty intr ^C
   ```

3. **Menetapkan kunci hapus kepada Ctrl+H:**
   ```csh
   stty erase ^H
   ```

4. **Mengeluarkan tetapan dalam format boleh digunakan semula:**
   ```csh
   stty -g
   ```

5. **Menetapkan tetapan untuk terminal tertentu:**
   ```csh
   stty -F /dev/ttyS0 9600
   ```

## Tips
- Sentiasa semak tetapan terminal semasa dengan `stty -a` sebelum membuat perubahan.
- Gunakan `stty -g` untuk menyimpan tetapan semasa jika anda ingin mengembalikannya kemudian.
- Berhati-hati ketika mengubah tetapan yang berkaitan dengan kunci, kerana ia boleh mempengaruhi cara anda berinteraksi dengan terminal.