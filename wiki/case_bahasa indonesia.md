# [Sistem Operasi] C Shell (csh) case: Menangani pola string

## Overview
Perintah `case` dalam C Shell (csh) digunakan untuk membandingkan sebuah variabel dengan beberapa pola. Ini memungkinkan pengguna untuk mengeksekusi blok perintah yang berbeda berdasarkan nilai variabel tersebut. Dengan menggunakan `case`, Anda dapat membuat skrip yang lebih dinamis dan responsif terhadap input yang berbeda.

## Usage
Berikut adalah sintaks dasar dari perintah `case`:

```csh
case [variabel] in
    [pola1]) 
        [perintah1]
        ;;
    [pola2]) 
        [perintah2]
        ;;
    ...
    *) 
        [perintah_default]
        ;;
esac
```

## Common Options
Perintah `case` tidak memiliki opsi khusus, tetapi Anda dapat menggunakan pola wildcard seperti `*` dan `?` untuk mencocokkan string.

## Common Examples

### Contoh 1: Menentukan jenis file
```csh
set file_type = "document.txt"
case $file_type in
    *.txt) 
        echo "Ini adalah file teks."
        ;;
    *.jpg) 
        echo "Ini adalah file gambar."
        ;;
    *) 
        echo "Jenis file tidak dikenali."
        ;;
esac
```

### Contoh 2: Menangani input pengguna
```csh
set user_input = "y"
case $user_input in
    y|Y) 
        echo "Anda memilih Ya."
        ;;
    n|N) 
        echo "Anda memilih Tidak."
        ;;
    *) 
        echo "Pilihan tidak valid."
        ;;
esac
```

### Contoh 3: Menggunakan wildcard
```csh
set command = "ls"
case $command in
    ls) 
        echo "Menampilkan daftar file."
        ;;
    cp) 
        echo "Menyalin file."
        ;;
    *) 
        echo "Perintah tidak dikenali."
        ;;
esac
```

## Tips
- Gunakan pola wildcard untuk menangani variasi dalam input, seperti `*` untuk mencocokkan nol atau lebih karakter.
- Pastikan untuk menutup setiap blok perintah dengan `;;` untuk menghindari kesalahan sintaks.
- Gunakan `*)` sebagai default case untuk menangani semua input yang tidak cocok dengan pola yang telah ditentukan.