# [Sistem Operasi] C Shell (csh) bzip2 Penggunaan: Memampatkan dan menyahmampatkan fail

## Overview
Perintah `bzip2` digunakan untuk memampatkan dan menyahmampatkan fail menggunakan algoritma pemampatan yang berkesan. Ia menghasilkan fail dengan sambungan `.bz2`, yang lebih kecil saiznya berbanding dengan fail asal.

## Usage
Sintaks asas untuk menggunakan `bzip2` adalah seperti berikut:

```
bzip2 [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `bzip2` beserta penjelasan ringkas:

- `-d` : Menyahmampatkan fail.
- `-k` : Menyimpan fail asal selepas pemampatan.
- `-f` : Memaksa pemampatan walaupun fail dengan nama yang sama sudah wujud.
- `-v` : Mengaktifkan mod verbose, menunjukkan maklumat lanjut semasa pemprosesan.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `bzip2`:

1. **Memampatkan fail:**
   ```bash
   bzip2 fail.txt
   ```

2. **Menyahmampatkan fail:**
   ```bash
   bzip2 -d fail.txt.bz2
   ```

3. **Memampatkan fail dan menyimpan fail asal:**
   ```bash
   bzip2 -k fail.txt
   ```

4. **Memaksa pemampatan walaupun fail dengan nama yang sama ada:**
   ```bash
   bzip2 -f fail.txt
   ```

5. **Menggunakan mod verbose semasa pemampatan:**
   ```bash
   bzip2 -v fail.txt
   ```

## Tips
- Sentiasa semak saiz fail selepas pemampatan untuk memastikan ia berkurang dengan ketara.
- Gunakan pilihan `-k` jika anda ingin mengekalkan fail asal semasa memampatkan.
- Untuk pemampatan yang lebih baik, pertimbangkan untuk menggunakan `bzip2` pada fail yang lebih besar atau fail teks.