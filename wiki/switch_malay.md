# [Sistem Operasi] C Shell (csh) switch: Mengubah antara pilihan

## Overview
Perintah `switch` dalam C Shell (csh) digunakan untuk membuat keputusan berdasarkan nilai yang diberikan. Ia membolehkan pengguna untuk memilih antara pelbagai pilihan yang ditetapkan, menjadikannya berguna untuk pengendalian aliran program.

## Usage
Berikut adalah sintaks asas untuk perintah `switch`:

```csh
switch (ekspresi)
    case pilihan1:
        perintah1
        breaksw
    case pilihan2:
        perintah2
        breaksw
    default:
        perintah_default
end
```

## Common Options
Perintah `switch` tidak mempunyai banyak pilihan, tetapi berikut adalah beberapa elemen penting:

- `case`: Menentukan pilihan yang akan dibandingkan dengan ekspresi.
- `breaksw`: Menghentikan pemprosesan lebih lanjut dalam blok `switch`.
- `default`: Menentukan perintah yang akan dijalankan jika tiada pilihan yang sepadan.

## Common Examples

### Contoh 1: Menggunakan switch untuk memilih hari
```csh
set hari = "Isnin"
switch ($hari)
    case "Isnin":
        echo "Hari ini adalah Isnin."
        breaksw
    case "Selasa":
        echo "Hari ini adalah Selasa."
        breaksw
    default:
        echo "Hari tidak dikenali."
end
```

### Contoh 2: Menentukan jenis fail
```csh
set fail = "dokumen"
switch ($fail)
    case "gambar":
        echo "Ini adalah fail gambar."
        breaksw
    case "dokumen":
        echo "Ini adalah fail dokumen."
        breaksw
    case "audio":
        echo "Ini adalah fail audio."
        breaksw
    default:
        echo "Jenis fail tidak dikenali."
end
```

### Contoh 3: Memilih tindakan berdasarkan pilihan pengguna
```csh
set pilihan = "keluar"
switch ($pilihan)
    case "masuk":
        echo "Anda telah memilih untuk masuk."
        breaksw
    case "keluar":
        echo "Anda telah memilih untuk keluar."
        breaksw
    default:
        echo "Pilihan tidak sah."
end
```

## Tips
- Sentiasa gunakan `breaksw` selepas setiap `case` untuk mengelakkan pemprosesan berterusan ke dalam kes yang lain.
- Gunakan `default` untuk menangani situasi di mana tiada pilihan yang sepadan dijumpai.
- Pastikan ekspresi yang digunakan dalam `switch` adalah dalam tanda kurung untuk mengelakkan ralat sintaks.