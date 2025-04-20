# [Sistem Operasi] C Shell (csh) else: Mengawal aliran pengendalian

## Overview
Perintah `else` dalam C Shell (csh) digunakan dalam struktur kawalan untuk memberikan alternatif kepada blok kod yang akan dijalankan jika syarat tertentu tidak dipenuhi. Ia sering digunakan bersama perintah `if` untuk mengawal aliran program.

## Usage
Sintaks asas untuk perintah `else` adalah seperti berikut:

```
if (condition) then
    # kod jika syarat benar
else
    # kod jika syarat tidak benar
endif
```

## Common Options
Perintah `else` tidak mempunyai pilihan khusus, tetapi ia berfungsi sebagai sebahagian daripada struktur kawalan yang lebih besar. Berikut adalah beberapa elemen yang sering digunakan bersamanya:
- `if`: Menentukan syarat yang perlu dipenuhi.
- `then`: Menandakan permulaan blok kod yang akan dijalankan jika syarat benar.
- `endif`: Menandakan akhir blok kawalan.

## Common Examples

### Contoh 1: Menggunakan `else` dengan `if`
```csh
set var = 10
if ($var < 20) then
    echo "Nilai kurang daripada 20"
else
    echo "Nilai 20 atau lebih"
endif
```

### Contoh 2: Memeriksa fail
```csh
if (-e "fail.txt") then
    echo "Fail wujud"
else
    echo "Fail tidak wujud"
endif
```

### Contoh 3: Menggunakan `else` dalam pengulangan
```csh
set count = 5
if ($count > 0) then
    echo "Pengiraan positif"
else
    echo "Pengiraan tidak positif"
endif
```

## Tips
- Sentiasa pastikan untuk menutup blok `if` dengan `endif` untuk mengelakkan ralat sintaks.
- Gunakan `else` untuk memberikan maklumat tambahan kepada pengguna apabila syarat tidak dipenuhi.
- Struktur kod yang jelas dan teratur memudahkan pemahaman dan penyelenggaraan.