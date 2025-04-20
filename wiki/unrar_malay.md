# [Sistem Operasi] C Shell (csh) unrar: Mengeluarkan fail dari arkib RAR

## Overview
Perintah `unrar` digunakan untuk mengekstrak fail dari arkib RAR. Ia membolehkan pengguna untuk mengakses dan mendapatkan semula fail yang telah dimampatkan dalam format RAR.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `unrar`:

```
unrar [options] [arguments]
```

## Common Options
- `e`: Mengekstrak semua fail ke dalam direktori semasa.
- `x`: Mengekstrak fail dan mengekalkan struktur direktori asal.
- `l`: Menyenaraikan kandungan arkib tanpa mengekstrak.
- `v`: Menunjukkan maklumat terperinci tentang arkib.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `unrar`:

1. Mengekstrak semua fail ke dalam direktori semasa:
   ```bash
   unrar e fail. rar
   ```

2. Mengekstrak fail dan mengekalkan struktur direktori:
   ```bash
   unrar x fail. rar
   ```

3. Menyenaraikan kandungan arkib:
   ```bash
   unrar l fail. rar
   ```

4. Menunjukkan maklumat terperinci tentang arkib:
   ```bash
   unrar v fail. rar
   ```

## Tips
- Pastikan anda berada dalam direktori yang betul sebelum mengekstrak fail untuk mengelakkan kekeliruan.
- Gunakan pilihan `l` untuk melihat kandungan arkib sebelum mengekstrak, ini membantu anda mengetahui fail yang ada.
- Sentiasa periksa ruang simpanan yang mencukupi sebelum mengekstrak arkib besar.