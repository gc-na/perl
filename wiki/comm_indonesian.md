# [Sistem Operasi] C Shell (csh) comm: Membandingkan dua file baris

## Overview
Perintah `comm` digunakan untuk membandingkan dua file yang terurut dan menampilkan perbedaan serta kesamaan antara keduanya. Hasilnya dibagi menjadi tiga kolom: baris yang hanya ada di file pertama, baris yang hanya ada di file kedua, dan baris yang ada di kedua file.

## Usage
Berikut adalah sintaks dasar dari perintah `comm`:

```csh
comm [options] [arguments]
```

## Common Options
- `-1`: Mengabaikan kolom pertama (baris yang hanya ada di file pertama).
- `-2`: Mengabaikan kolom kedua (baris yang hanya ada di file kedua).
- `-3`: Mengabaikan kolom ketiga (baris yang ada di kedua file).
- `-i`: Mengabaikan perbedaan huruf besar dan kecil saat membandingkan.
- `-u`: Menampilkan hasil dalam urutan tidak terurut.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `comm`:

1. **Membandingkan dua file dan menampilkan semua kolom**:
    ```csh
    comm file1.txt file2.txt
    ```

2. **Hanya menampilkan baris yang ada di file pertama**:
    ```csh
    comm -13 file1.txt file2.txt
    ```

3. **Hanya menampilkan baris yang ada di file kedua**:
    ```csh
    comm -12 file1.txt file2.txt
    ```

4. **Mengabaikan perbedaan huruf besar dan kecil**:
    ```csh
    comm -i file1.txt file2.txt
    ```

## Tips
- Pastikan kedua file yang akan dibandingkan sudah terurut. Jika tidak, hasilnya mungkin tidak akurat.
- Gunakan opsi `-1`, `-2`, atau `-3` untuk fokus pada bagian tertentu dari hasil perbandingan.
- Untuk analisis yang lebih mendalam, pertimbangkan untuk menggabungkan `comm` dengan perintah lain seperti `sort` untuk memastikan file terurut.