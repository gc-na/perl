# [Sistem Operasi] C Shell (csh) if: Memeriksa kondisi

## Overview
Perintah `if` dalam C Shell (csh) digunakan untuk mengevaluasi kondisi dan menjalankan perintah tertentu berdasarkan hasil evaluasi tersebut. Ini sangat berguna dalam skrip untuk mengontrol alur eksekusi berdasarkan kondisi yang diberikan.

## Usage
Berikut adalah sintaks dasar dari perintah `if`:

```
if (kondisi) then
    perintah
endif
```

## Common Options
- `-eq`: Memeriksa apakah dua angka sama.
- `-ne`: Memeriksa apakah dua angka tidak sama.
- `-lt`: Memeriksa apakah angka pertama lebih kecil dari angka kedua.
- `-gt`: Memeriksa apakah angka pertama lebih besar dari angka kedua.
- `-f`: Memeriksa apakah file yang diberikan ada dan merupakan file biasa.

## Common Examples

### Contoh 1: Memeriksa apakah sebuah file ada
```csh
if (-f "file.txt") then
    echo "File ada."
endif
```

### Contoh 2: Memeriksa dua angka
```csh
set a = 5
set b = 10
if ($a -lt $b) then
    echo "$a lebih kecil dari $b."
endif
```

### Contoh 3: Menggunakan pernyataan else
```csh
if (-f "file.txt") then
    echo "File ada."
else
    echo "File tidak ada."
endif
```

### Contoh 4: Memeriksa lebih dari satu kondisi
```csh
set a = 5
if ($a -gt 0 && $a -lt 10) then
    echo "$a berada dalam rentang 1 hingga 9."
endif
```

## Tips
- Selalu gunakan spasi yang tepat di sekitar operator untuk menghindari kesalahan sintaks.
- Gunakan tanda kurung untuk mengelompokkan kondisi yang kompleks agar lebih mudah dibaca.
- Pastikan untuk menutup blok `if` dengan `endif` untuk menghindari kebingungan dalam skrip.