# [Linux] C Shell (csh) comm: Bandingkan dua fail baris

## Overview
Perintah `comm` digunakan untuk membandingkan dua fail teks yang telah disusun dan menghasilkan output yang menunjukkan baris yang terdapat dalam kedua-dua fail, serta baris yang unik kepada setiap fail.

## Usage
Berikut adalah sintaks asas untuk perintah `comm`:

```csh
comm [options] [arguments]
```

## Common Options
- `-1`: Jangan tampilkan baris yang hanya terdapat dalam fail pertama.
- `-2`: Jangan tampilkan baris yang hanya terdapat dalam fail kedua.
- `-3`: Jangan tampilkan baris yang terdapat dalam kedua-dua fail.
- `-i`: Abaikan kes dalam perbandingan.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `comm`:

1. **Membandingkan dua fail**:
   ```csh
   comm file1.txt file2.txt
   ```

2. **Hanya menunjukkan baris yang terdapat dalam fail kedua**:
   ```csh
   comm -13 file1.txt file2.txt
   ```

3. **Mengabaikan kes semasa membandingkan**:
   ```csh
   comm -i file1.txt file2.txt
   ```

4. **Menunjukkan baris yang hanya terdapat dalam fail pertama dan kedua**:
   ```csh
   comm -12 file1.txt file2.txt
   ```

## Tips
- Pastikan kedua-dua fail yang ingin dibandingkan telah disusun untuk mendapatkan hasil yang tepat.
- Gunakan pilihan `-i` jika anda ingin mengabaikan perbezaan kes semasa membandingkan teks.
- Anda boleh mengalihkan output ke fail lain dengan menggunakan `>` untuk menyimpan hasil perbandingan. Contoh:
  ```csh
  comm file1.txt file2.txt > hasil.txt
  ```