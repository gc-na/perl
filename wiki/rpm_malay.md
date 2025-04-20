# [Linux] C Shell (csh) rpm Penggunaan: Mengurus pakej perisian

## Overview
Perintah `rpm` digunakan untuk mengurus pakej perisian dalam sistem pengendalian Linux. Ia membolehkan pengguna untuk memasang, mengeluarkan, dan mengurus pakej yang dibungkus dalam format RPM (Red Hat Package Manager).

## Usage
Sintaks asas untuk perintah `rpm` adalah seperti berikut:

```bash
rpm [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk perintah `rpm`:

- `-i`: Memasang pakej baru.
- `-e`: Mengeluarkan atau menyahpasang pakej.
- `-q`: Menyoal maklumat tentang pakej yang dipasang.
- `-U`: Mengemas kini pakej yang sedia ada.
- `-v`: Menunjukkan maklumat yang lebih terperinci semasa pelaksanaan.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `rpm`:

1. **Memasang pakej baru:**
   ```bash
   rpm -i nama_pakej.rpm
   ```

2. **Mengeluarkan pakej:**
   ```bash
   rpm -e nama_pakej
   ```

3. **Menyoal maklumat tentang pakej yang dipasang:**
   ```bash
   rpm -q nama_pakej
   ```

4. **Mengemas kini pakej:**
   ```bash
   rpm -U nama_pakej_baru.rpm
   ```

5. **Menunjukkan maklumat terperinci tentang pakej:**
   ```bash
   rpm -qi nama_pakej
   ```

## Tips
- Sentiasa semak kebergantungan pakej sebelum memasang atau mengemas kini untuk mengelakkan masalah.
- Gunakan pilihan `-v` untuk mendapatkan maklumat tambahan semasa proses pemasangan atau pengeluaran.
- Simpan salinan pakej RPM yang telah dimuat turun untuk kemudahan pemasangan semula di masa hadapan.