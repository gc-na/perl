# [Linux] C Shell (csh) gzip Penggunaan: Memampatkan fail

## Overview
Perintah `gzip` digunakan untuk memampatkan fail dalam sistem operasi Unix dan Linux. Ia mengurangkan saiz fail dengan menggunakan algoritma pemampatan, menjadikannya lebih mudah untuk disimpan dan dihantar.

## Usage
Sintaks asas untuk menggunakan perintah `gzip` adalah seperti berikut:

```csh
gzip [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan umum untuk perintah `gzip`:

- `-d` : Menguraikan fail yang telah dipampatkan.
- `-k` : Menyimpan fail asal semasa memampatkan.
- `-v` : Menunjukkan maklumat terperinci semasa pemampatan.
- `-r` : Memampatkan fail dalam direktori secara rekursif.

## Common Examples
Berikut adalah beberapa contoh penggunaan `gzip`:

1. Memampatkan fail:
   ```csh
   gzip fail.txt
   ```

2. Menguraikan fail yang telah dipampatkan:
   ```csh
   gzip -d fail.txt.gz
   ```

3. Memampatkan fail tetapi menyimpan fail asal:
   ```csh
   gzip -k fail.txt
   ```

4. Memampatkan semua fail dalam direktori secara rekursif:
   ```csh
   gzip -r direktori/
   ```

5. Menunjukkan maklumat terperinci semasa pemampatan:
   ```csh
   gzip -v fail.txt
   ```

## Tips
- Sentiasa semak saiz fail selepas pemampatan untuk memastikan ia telah dipampatkan dengan berkesan.
- Gunakan pilihan `-k` jika anda ingin mengekalkan fail asal untuk rujukan.
- Untuk fail yang sangat besar, pertimbangkan untuk menggunakan pilihan `-r` untuk memampatkan keseluruhan direktori dengan mudah.