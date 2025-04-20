# [Sistem Operasi] C Shell (csh) rmdir: Menghapus direktori kosong

## Overview
Perintah `rmdir` digunakan dalam C Shell untuk menghapus direktori yang kosong. Jika direktori yang ingin dihapus mengandung fail atau subdirektori, perintah ini tidak akan berjaya.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `rmdir`:

```
rmdir [options] [arguments]
```

## Common Options
- `-p`: Menghapus direktori dan semua direktori induknya jika mereka juga kosong.
- `--help`: Menampilkan maklumat bantuan tentang penggunaan perintah.
- `--version`: Menampilkan versi perintah `rmdir`.

## Common Examples
Berikut adalah beberapa contoh penggunaan `rmdir`:

1. Menghapus direktori kosong:
   ```csh
   rmdir direktori_kosong
   ```

2. Menghapus beberapa direktori kosong sekaligus:
   ```csh
   rmdir direktori1 direktori2 direktori3
   ```

3. Menghapus direktori dan semua direktori induknya jika kosong:
   ```csh
   rmdir -p direktori/induk/direktori_kosong
   ```

## Tips
- Pastikan direktori yang ingin dihapus benar-benar kosong, jika tidak, perintah `rmdir` akan gagal.
- Gunakan opsi `-p` dengan hati-hati, kerana ia akan menghapus semua direktori induk yang kosong.
- Selalu periksa isi direktori sebelum menghapus untuk menghindari kehilangan data yang tidak diingini.