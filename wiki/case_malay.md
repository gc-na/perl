# [Sistem Operasi] C Shell (csh) case: mengendalikan pilihan

## Overview
Perintah `case` dalam C Shell (csh) digunakan untuk mengendalikan aliran program berdasarkan nilai yang diberikan. Ia membolehkan pengguna untuk membuat keputusan berdasarkan pelbagai pilihan yang mungkin, menjadikannya berguna dalam skrip yang memerlukan pengendalian pelbagai keadaan.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `case`:

```
case [nilai] in
    [pola1])
        [perintah1]
        ;;
    [pola2])
        [perintah2]
        ;;
    *)
        [perintah_default]
        ;;
esac
```

## Common Options
- `*` : Menunjukkan pilihan lalai jika tiada pola yang sepadan.
- `;;` : Menandakan akhir bagi setiap blok perintah dalam kes tertentu.
- `esac` : Menandakan akhir bagi struktur `case`.

## Common Examples
Berikut adalah beberapa contoh praktikal menggunakan perintah `case`:

### Contoh 1: Memilih hari dalam seminggu
```csh
set hari = "Isnin"
case $hari in
    "Isnin")
        echo "Hari ini adalah Isnin."
        ;;
    "Selasa")
        echo "Hari ini adalah Selasa."
        ;;
    *)
        echo "Hari tidak dikenali."
        ;;
esac
```

### Contoh 2: Memeriksa jenis fail
```csh
set fail = "dokumen.txt"
case $fail in
    *.txt)
        echo "Ini adalah fail teks."
        ;;
    *.jpg)
        echo "Ini adalah fail gambar."
        ;;
    *)
        echo "Jenis fail tidak dikenali."
        ;;
esac
```

### Contoh 3: Menentukan pilihan pengguna
```csh
set pilihan = "2"
case $pilihan in
    "1")
        echo "Anda memilih pilihan 1."
        ;;
    "2")
        echo "Anda memilih pilihan 2."
        ;;
    "3")
        echo "Anda memilih pilihan 3."
        ;;
    *)
        echo "Pilihan tidak sah."
        ;;
esac
```

## Tips
- Sentiasa gunakan `;;` untuk menandakan akhir setiap blok perintah untuk mengelakkan kesilapan.
- Gunakan pola wildcard seperti `*` untuk menangkap pelbagai pilihan dengan lebih mudah.
- Pastikan untuk menguji setiap kes untuk memastikan semua kemungkinan telah ditangani.