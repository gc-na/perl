# [Sistem Operasi] C Shell (csh) while: [melaksanakan perulangan]

## Overview
Perintah `while` dalam C Shell (csh) digunakan untuk melaksanakan blok perintah berulang kali selagi syarat tertentu dipenuhi. Ini membolehkan pengguna untuk menjalankan satu set arahan berulang kali tanpa perlu menulis semula kod yang sama.

## Usage
Sintaks asas untuk perintah `while` adalah seperti berikut:

```csh
while (condition)
    # arahan yang ingin dilaksanakan
end
```

## Common Options
Perintah `while` tidak mempunyai banyak pilihan, tetapi berikut adalah beberapa yang sering digunakan:

- `condition`: Syarat yang perlu dipenuhi untuk meneruskan perulangan. Jika syarat ini benar, arahan dalam blok akan dilaksanakan.

## Common Examples

### Contoh 1: Perulangan berdasarkan bilangan
```csh
set i = 1
while ($i <= 5)
    echo "Bilangan: $i"
    @ i++
end
```
*Dalam contoh ini, perintah akan mencetak bilangan dari 1 hingga 5.*

### Contoh 2: Perulangan sehingga syarat dipenuhi
```csh
set input = ""
while ("$input" != "exit")
    echo "Masukkan arahan (atau 'exit' untuk keluar): "
    set input = $<
end
```
*Contoh ini membolehkan pengguna memasukkan arahan sehingga mereka menaip 'exit'.*

### Contoh 3: Menggunakan perulangan untuk membaca fail
```csh
set file = "data.txt"
while (1)
    set line = `head -n 1 $file`
    if ("$line" == "") break
    echo "Baris: $line"
    set file = `tail -n +2 $file`
end
```
*Di sini, perintah akan membaca dan mencetak setiap baris dari fail sehingga fail tersebut habis.*

## Tips
- Pastikan syarat dalam perintah `while` dapat diubah untuk mengelakkan perulangan tanpa henti.
- Gunakan `break` untuk keluar dari perulangan jika perlu.
- Sentiasa periksa nilai variabel yang digunakan dalam syarat untuk memastikan perulangan berfungsi seperti yang diharapkan.