# [Sistem Operasi] C Shell (csh) iconv Penggunaan: Menukar kod pemfailan

## Overview
Perintah `iconv` digunakan untuk menukar kod pemfailan dari satu set karakter ke set karakter yang lain. Ini berguna apabila anda perlu membaca atau memproses fail yang menggunakan pelbagai kod karakter.

## Usage
Sintaks asas bagi perintah `iconv` adalah seperti berikut:

```
iconv [options] [arguments]
```

## Common Options
- `-f` : Menentukan set karakter asal.
- `-t` : Menentukan set karakter sasaran.
- `-o` : Menentukan nama fail output.
- `-c` : Mengabaikan karakter yang tidak dapat ditukar.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `iconv`:

1. Menukar fail dari UTF-8 ke ISO-8859-1:
   ```csh
   iconv -f UTF-8 -t ISO-8859-1 input.txt -o output.txt
   ```

2. Mengabaikan karakter yang tidak dapat ditukar:
   ```csh
   iconv -f UTF-8 -t ASCII//TRANSLIT -c input.txt -o output.txt
   ```

3. Menukar fail dan menulis output ke terminal:
   ```csh
   iconv -f UTF-8 -t UTF-16 input.txt
   ```

4. Menukar fail dan menyimpan hasil dalam fail baru:
   ```csh
   iconv -f WINDOWS-1252 -t UTF-8 input.txt -o output.txt
   ```

## Tips
- Pastikan anda mengetahui set karakter asal dan sasaran sebelum menggunakan `iconv` untuk mengelakkan kesilapan.
- Gunakan pilihan `-c` jika anda ingin mengabaikan karakter yang tidak dikenali semasa penukaran.
- Sentiasa buat salinan fail asal sebelum melakukan penukaran, terutamanya jika anda menulis ke fail yang sama.