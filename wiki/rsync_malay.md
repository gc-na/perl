# [Sistem Operasi] C Shell (csh) rsync Penggunaan: Menyalin dan menyegerakkan fail

## Overview
Perintah `rsync` digunakan untuk menyalin dan menyegerakkan fail dan direktori antara lokasi yang berbeza. Ia sangat efisien kerana hanya memindahkan perubahan yang dibuat pada fail, menjadikannya pilihan yang baik untuk sandaran dan pemindahan data.

## Usage
Sintaks asas untuk perintah `rsync` adalah seperti berikut:

```bash
rsync [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan umum yang boleh digunakan dengan `rsync`:

- `-a`: Menyalin fail secara rekursif dan mengekalkan atribut fail.
- `-v`: Menunjukkan maklumat terperinci semasa pemindahan.
- `-z`: Mengompres data semasa pemindahan untuk menjimatkan lebar jalur.
- `--delete`: Menghapus fail di lokasi destinasi yang tidak ada di lokasi sumber.
- `-e`: Menentukan protokol pengangkutan, seperti SSH.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `rsync`:

1. Menyalin direktori secara rekursif dengan mengekalkan atribut:

   ```bash
   rsync -av /path/sumber/ /path/destinasi/
   ```

2. Menyalin fail dan mengompres data semasa pemindahan:

   ```bash
   rsync -az /path/sumber/file.txt /path/destinasi/
   ```

3. Menyalin fail dari pelayan jauh menggunakan SSH:

   ```bash
   rsync -avz -e ssh user@remote:/path/sumber/ /path/destinasi/
   ```

4. Menyegerakkan dua direktori dan menghapus fail yang tidak ada di sumber:

   ```bash
   rsync -av --delete /path/sumber/ /path/destinasi/
   ```

## Tips
- Sentiasa gunakan pilihan `-n` (dry run) untuk melihat apa yang akan dilakukan tanpa membuat sebarang perubahan.
- Pastikan anda mempunyai salinan sandaran sebelum menggunakan pilihan `--delete` untuk mengelakkan kehilangan data.
- Gunakan `-v` untuk mendapatkan maklumat terperinci semasa pemindahan, ini boleh membantu dalam menyelesaikan masalah.