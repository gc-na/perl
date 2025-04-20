# [Linux] C Shell (csh) date: Menunjukkan dan mengubah tarikh dan masa

## Overview
Perintah `date` dalam C Shell (csh) digunakan untuk memaparkan dan mengubah tarikh serta masa sistem. Ia membolehkan pengguna untuk melihat tarikh dan masa semasa, serta memformatnya mengikut keperluan.

## Usage
Sintaks asas untuk perintah `date` adalah seperti berikut:

```
date [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk perintah `date`:

- `+FORMAT` : Menentukan format output tarikh dan masa.
- `-u` : Menunjukkan waktu dalam format UTC (Coordinated Universal Time).
- `-d STRING` : Menetapkan tarikh dan masa berdasarkan string yang diberikan.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `date`:

1. **Menunjukkan tarikh dan masa semasa:**
   ```csh
   date
   ```

2. **Menunjukkan tarikh dalam format tertentu:**
   ```csh
   date "+%Y-%m-%d %H:%M:%S"
   ```

3. **Menunjukkan waktu dalam format UTC:**
   ```csh
   date -u
   ```

4. **Menetapkan tarikh dan masa berdasarkan string:**
   ```csh
   date -d "2023-10-01 12:00:00"
   ```

## Tips
- Gunakan pilihan `+FORMAT` untuk menyesuaikan output tarikh dan masa mengikut keperluan laporan atau skrip.
- Sentiasa semak waktu sistem anda jika anda menggunakan `date` untuk menetapkan waktu, terutamanya pada pelayan.
- Anda boleh menyimpan output perintah `date` ke dalam fail dengan menggunakan pengalihan, contohnya:
  ```csh
  date "+%Y-%m-%d %H:%M:%S" > tarikh.txt
  ```