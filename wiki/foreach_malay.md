# [Linux] C Shell (csh) foreach penggunaan: Melaksanakan perulangan pada senarai

## Overview
Perintah `foreach` dalam C Shell (csh) digunakan untuk melaksanakan perulangan ke atas senarai item. Ia membolehkan pengguna untuk menjalankan satu set arahan untuk setiap elemen dalam senarai yang ditentukan.

## Usage
Berikut adalah sintaks asas bagi perintah `foreach`:

```
foreach [options] [arguments]
```

## Common Options
- `-n`: Menjalankan perulangan tanpa mencetak setiap arahan yang dilaksanakan.
- `-e`: Menjalankan arahan yang diberikan sebagai argumen tanpa perlu menulisnya dalam blok.

## Common Examples

### Contoh 1: Mengulangi melalui senarai nombor
```csh
foreach i (1 2 3 4 5)
    echo "Nombor: $i"
end
```
Output:
```
Nombor: 1
Nombor: 2
Nombor: 3
Nombor: 4
Nombor: 5
```

### Contoh 2: Mengulangi melalui senarai fail
```csh
foreach file (*.txt)
    echo "Memproses fail: $file"
end
```
Output:
```
Memproses fail: dokumen1.txt
Memproses fail: dokumen2.txt
...
```

### Contoh 3: Menggunakan pilihan -n
```csh
foreach i (1 2 3)
    echo "Perulangan: $i"
end
```
Dengan pilihan `-n`, arahan tidak akan dicetak tetapi masih akan dilaksanakan.

## Tips
- Pastikan untuk menggunakan `end` untuk menandakan akhir blok perulangan.
- Gunakan `-n` jika anda ingin mengelakkan output arahan yang tidak perlu semasa menjalankan perulangan.
- Anda boleh menggunakan `break` untuk menghentikan perulangan jika perlu.