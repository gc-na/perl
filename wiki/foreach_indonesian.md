# [Sistem Operasi] C Shell (csh) foreach: Menjalankan perintah untuk setiap elemen dalam daftar

## Overview
Perintah `foreach` dalam C Shell (csh) digunakan untuk menjalankan serangkaian perintah untuk setiap elemen dalam daftar yang diberikan. Ini sangat berguna ketika Anda ingin melakukan operasi yang sama pada beberapa item tanpa harus menulis ulang perintah untuk setiap item.

## Usage
Berikut adalah sintaks dasar dari perintah `foreach`:

```csh
foreach variable (list)
    command
end
```

## Common Options
Perintah `foreach` tidak memiliki banyak opsi, tetapi berikut adalah beberapa yang umum digunakan:

- `variable`: Nama variabel yang akan menyimpan setiap elemen dari daftar saat iterasi.
- `list`: Daftar elemen yang akan diproses.

## Common Examples

### Contoh 1: Menampilkan nama file
Menampilkan semua file dengan ekstensi `.txt` dalam direktori saat ini.

```csh
foreach file (*.txt)
    echo $file
end
```

### Contoh 2: Menghapus file sementara
Menghapus semua file sementara yang memiliki ekstensi `.tmp`.

```csh
foreach temp_file (*.tmp)
    rm $temp_file
end
```

### Contoh 3: Mengompresi file
Mengompresi semua file gambar dalam direktori.

```csh
foreach img_file (*.jpg)
    gzip $img_file
end
```

## Tips
- Pastikan untuk menggunakan `end` di akhir blok `foreach` untuk menandai akhir dari perintah yang akan dieksekusi.
- Gunakan wildcard (`*`) untuk memudahkan pemilihan file atau direktori yang sesuai dengan pola tertentu.
- Jika Anda ingin melihat hasil dari setiap iterasi, gunakan `echo` untuk mencetak nilai variabel sebelum menjalankan perintah.