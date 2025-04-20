# [Sistem Operasi] C Shell (csh) case <Penggunaan>: Mengelompokkan pola string

## Overview
Perintah `case` dalam C Shell (csh) digunakan untuk mengelompokkan string berdasarkan pola tertentu. Ini memungkinkan pengguna untuk mengeksekusi perintah yang berbeda tergantung pada nilai variabel yang diberikan.

## Usage
Sintaks dasar dari perintah `case` adalah sebagai berikut:

```
case [variabel] in
    [pola1]) perintah1 ;;
    [pola2]) perintah2 ;;
    ...
esac
```

## Common Options
- `in`: Menentukan pola yang akan dicocokkan.
- `;;`: Menandakan akhir dari pernyataan untuk pola tertentu.
- `esac`: Menandakan akhir dari blok `case`.

## Common Examples

### Contoh 1: Menggunakan case untuk menentukan hari
```csh
set hari = "Senin"
case $hari in
    "Senin") echo "Hari pertama dalam seminggu." ;;
    "Selasa") echo "Hari kedua dalam seminggu." ;;
    "Rabu") echo "Hari ketiga dalam seminggu." ;;
    *) echo "Bukan hari kerja." ;;
esac
```

### Contoh 2: Mengelompokkan jenis file
```csh
set file = "dokumen.txt"
case $file in
    *.txt) echo "Ini adalah file teks." ;;
    *.jpg) echo "Ini adalah file gambar." ;;
    *.pdf) echo "Ini adalah file PDF." ;;
    *) echo "Jenis file tidak dikenali." ;;
esac
```

### Contoh 3: Menentukan tindakan berdasarkan input pengguna
```csh
set pilihan = "keluar"
case $pilihan in
    "masuk") echo "Anda memilih untuk masuk." ;;
    "keluar") echo "Anda memilih untuk keluar." ;;
    *) echo "Pilihan tidak valid." ;;
esac
```

## Tips
- Pastikan untuk menggunakan tanda kutip di sekitar pola jika pola tersebut mengandung spasi.
- Gunakan wildcard (`*`) untuk mencocokkan beberapa karakter dalam pola.
- Selalu sertakan pernyataan default (`*`) untuk menangani kasus yang tidak terduga.