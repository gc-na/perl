# [Sistem Operasi] C Shell (csh) uniq Penggunaan: Menghapus baris duplikat

## Overview
Perintah `uniq` digunakan untuk menghapus baris yang berulang dalam sebuah fail teks. Ia hanya berfungsi pada baris yang bersebelahan, jadi biasanya ia digunakan bersama perintah lain seperti `sort` untuk memastikan baris yang sama berada bersebelahan.

## Usage
Berikut adalah sintaks asas untuk perintah `uniq`:

```
uniq [options] [arguments]
```

## Common Options
- `-c`: Menghitung dan menampilkan jumlah kemunculan setiap baris.
- `-d`: Menampilkan hanya baris yang muncul lebih dari sekali.
- `-u`: Menampilkan hanya baris yang unik, iaitu baris yang muncul sekali sahaja.
- `-i`: Mengabaikan kes (case insensitive) ketika membandingkan baris.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `uniq`:

1. Menghapus baris duplikat dari fail:
   ```csh
   sort fail.txt | uniq > fail_unik.txt
   ```

2. Menghitung kemunculan setiap baris:
   ```csh
   sort fail.txt | uniq -c
   ```

3. Menampilkan hanya baris yang muncul lebih dari sekali:
   ```csh
   sort fail.txt | uniq -d
   ```

4. Menampilkan hanya baris yang unik:
   ```csh
   sort fail.txt | uniq -u
   ```

5. Mengabaikan kes ketika membandingkan baris:
   ```csh
   sort fail.txt | uniq -i
   ```

## Tips
- Pastikan untuk menggunakan `sort` sebelum `uniq` untuk mendapatkan hasil yang tepat, kerana `uniq` hanya menghapus duplikasi yang bersebelahan.
- Gunakan pilihan `-c` untuk mendapatkan gambaran jelas tentang berapa kali setiap baris muncul dalam fail.
- Jika anda bekerja dengan fail yang besar, pertimbangkan untuk menggunakan `uniq` dalam kombinasi dengan `head` atau `tail` untuk memeriksa hasil secara lebih mudah.