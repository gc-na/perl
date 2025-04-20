# [Sistem Operasi] C Shell (csh) while: Mengulangi Perintah

## Overview
Perintah `while` dalam C Shell (csh) digunakan untuk menjalankan serangkaian perintah berulang kali selama suatu kondisi tertentu terpenuhi. Ini sangat berguna untuk menjalankan loop yang terus berlanjut sampai kondisi yang ditentukan menjadi salah.

## Usage
Berikut adalah sintaks dasar dari perintah `while`:

```csh
while (kondisi)
    perintah
end
```

## Common Options
Perintah `while` tidak memiliki banyak opsi, tetapi berikut adalah beberapa hal yang perlu diperhatikan:
- `kondisi`: Ekspresi yang dievaluasi sebelum setiap iterasi. Jika ekspresi ini bernilai benar, perintah di dalam loop akan dijalankan.

## Common Examples

### Contoh 1: Menghitung dari 1 hingga 5
```csh
set i = 1
while ($i <= 5)
    echo $i
    @ i++
end
```
Contoh ini akan mencetak angka dari 1 hingga 5.

### Contoh 2: Mengulangi hingga kondisi terpenuhi
```csh
set count = 0
while ($count < 3)
    echo "Ini pengulangan nomor $count"
    @ count++
end
```
Loop ini akan mencetak pesan sebanyak tiga kali.

### Contoh 3: Menggunakan input pengguna
```csh
set input = ""
while ("$input" != "exit")
    echo "Masukkan perintah (ketik 'exit' untuk keluar):"
    set input = $<
end
```
Contoh ini akan terus meminta input dari pengguna sampai pengguna mengetik "exit".

## Tips
- Pastikan untuk memperbarui kondisi di dalam loop agar tidak terjadi loop tak berujung.
- Gunakan perintah `break` di dalam loop jika Anda ingin keluar dari loop lebih awal berdasarkan kondisi tertentu.
- Selalu periksa sintaks Anda untuk memastikan bahwa semua tanda kurung dan kata kunci ditutup dengan benar.