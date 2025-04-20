# [Linux] C Shell (csh) getopts: [mengendalikan pilihan dalam skrip]

## Overview
Perintah `getopts` dalam C Shell digunakan untuk mengendalikan pilihan (options) dalam skrip. Ia membolehkan pengguna untuk memproses argumen yang diberikan kepada skrip dan mengurus pilihan yang diterima dengan cara yang teratur.

## Usage
Berikut adalah sintaks asas untuk menggunakan `getopts`:

```csh
getopts [options] [arguments]
```

## Common Options
- `-a`: Menggunakan pilihan yang ditetapkan.
- `-b`: Mengabaikan pilihan yang tidak dikenali.
- `-c`: Menunjukkan pilihan yang telah diproses.

## Common Examples

### Contoh 1: Menggunakan getopts untuk pilihan tunggal
```csh
#!/bin/csh
set opt = ""
while getopts "a:" opt
    switch ($opt)
        case "a":
            echo "Pilihan a dengan argumen: $OPTARG"
        default:
            echo "Pilihan tidak dikenali"
    endsw
end
```

### Contoh 2: Menggunakan getopts untuk pilihan berganda
```csh
#!/bin/csh
set opt = ""
while getopts "abc:" opt
    switch ($opt)
        case "a":
            echo "Pilihan a dipilih"
        case "b":
            echo "Pilihan b dipilih"
        case "c":
            echo "Pilihan c dengan argumen: $OPTARG"
        default:
            echo "Pilihan tidak dikenali"
    endsw
end
```

### Contoh 3: Menggunakan getopts dengan pilihan tidak dikenali
```csh
#!/bin/csh
set opt = ""
while getopts "x:y:" opt
    switch ($opt)
        case "x":
            echo "Pilihan x dengan argumen: $OPTARG"
        case "y":
            echo "Pilihan y dengan argumen: $OPTARG"
        default:
            echo "Pilihan tidak dikenali: $opt"
    endsw
end
```

## Tips
- Sentiasa gunakan `switch` untuk mengendalikan pilihan yang berbeza dengan lebih teratur.
- Pastikan untuk menguji skrip dengan pilihan yang berbeza untuk memastikan semua pilihan berfungsi seperti yang diharapkan.
- Gunakan `OPTARG` untuk mendapatkan argumen yang berkaitan dengan pilihan yang telah dipilih.