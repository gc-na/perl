# [Linux] C Shell (csh) wc Penggunaan: Mengira bilangan baris, kata, dan aksara

## Overview
Perintah `wc` (word count) digunakan untuk mengira bilangan baris, kata, dan aksara dalam satu atau lebih fail. Ia adalah alat yang berguna untuk mendapatkan statistik ringkas tentang kandungan teks.

## Usage
Sintaks asas untuk perintah `wc` adalah seperti berikut:

```
wc [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk perintah `wc`:

- `-l`: Mengira bilangan baris.
- `-w`: Mengira bilangan kata.
- `-c`: Mengira bilangan aksara.
- `-m`: Mengira bilangan aksara (termasuk aksara Unicode).
- `-L`: Menunjukkan panjang baris terpanjang.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `wc`:

1. Mengira bilangan baris dalam fail:
   ```csh
   wc -l fail.txt
   ```

2. Mengira bilangan kata dalam fail:
   ```csh
   wc -w fail.txt
   ```

3. Mengira bilangan aksara dalam fail:
   ```csh
   wc -c fail.txt
   ```

4. Mengira bilangan baris, kata, dan aksara secara serentak:
   ```csh
   wc fail.txt
   ```

5. Mengira panjang baris terpanjang dalam fail:
   ```csh
   wc -L fail.txt
   ```

## Tips
- Gunakan pilihan `-l`, `-w`, dan `-c` bersama-sama untuk mendapatkan semua statistik dalam satu perintah.
- Jika anda ingin mengira kandungan dari beberapa fail, anda boleh menyenaraikan semua fail dalam satu perintah.
- Perintah `wc` boleh digunakan dalam kombinasi dengan perintah lain menggunakan pipe (`|`) untuk mengira hasil output dari perintah sebelumnya. Contohnya:
  ```csh
  cat fail.txt | wc -l
  ```