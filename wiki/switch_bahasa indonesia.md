# [Sistem Operasi] C Shell (csh) switch: Mengubah nilai variabel

## Overview
Perintah `switch` dalam C Shell (csh) digunakan untuk melakukan pemilihan berdasarkan nilai dari sebuah variabel. Ini memungkinkan pengguna untuk mengeksekusi blok kode yang berbeda tergantung pada nilai yang diberikan.

## Usage
Berikut adalah sintaks dasar dari perintah `switch`:

```
switch (ekspresi)
case nilai1:
    # perintah untuk nilai1
    breaksw
case nilai2:
    # perintah untuk nilai2
    breaksw
default:
    # perintah jika tidak ada nilai yang cocok
endsw
```

## Common Options
- `case`: Menentukan nilai yang akan dibandingkan dengan ekspresi.
- `breaksw`: Menghentikan eksekusi dari blok `switch` saat nilai yang cocok ditemukan.
- `default`: Menyediakan blok kode yang dieksekusi jika tidak ada nilai yang cocok.

## Common Examples

### Contoh 1: Menggunakan switch untuk memilih hari
```csh
set hari = "Senin"
switch ($hari)
case "Senin":
    echo "Hari ini adalah Senin."
    breaksw
case "Selasa":
    echo "Hari ini adalah Selasa."
    breaksw
default:
    echo "Hari tidak dikenali."
endsw
```

### Contoh 2: Menentukan jenis file berdasarkan ekstensi
```csh
set ekstensi = "txt"
switch ($ekstensi)
case "txt":
    echo "Ini adalah file teks."
    breaksw
case "jpg":
    echo "Ini adalah file gambar."
    breaksw
default:
    echo "Ekstensi tidak dikenali."
endsw
```

### Contoh 3: Menentukan status berdasarkan kode
```csh
set kode = 200
switch ($kode)
case 200:
    echo "Permintaan berhasil."
    breaksw
case 404:
    echo "Halaman tidak ditemukan."
    breaksw
default:
    echo "Kode status tidak dikenali."
endsw
```

## Tips
- Pastikan untuk selalu menggunakan `breaksw` setelah setiap `case` untuk mencegah eksekusi berlanjut ke `case` berikutnya.
- Gunakan `default` untuk menangani kasus yang tidak terduga, sehingga program Anda lebih robust.
- Perhatikan penggunaan tanda kurung pada ekspresi, karena ini penting untuk sintaks yang benar.