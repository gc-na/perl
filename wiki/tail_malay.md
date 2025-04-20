# [Sistem Operasi] C Shell (csh) tail Penggunaan: Menunjukkan akhir fail

## Overview
Perintah `tail` digunakan untuk memaparkan beberapa baris terakhir dari satu atau lebih fail. Ini berguna untuk memantau log atau fail teks yang sedang berkembang, membolehkan pengguna melihat kemas kini terkini tanpa perlu membuka keseluruhan fail.

## Usage
Berikut adalah sintaks asas untuk perintah `tail`:

```csh
tail [options] [arguments]
```

## Common Options
- `-n [number]`: Menunjukkan bilangan baris terakhir yang ditetapkan dari fail. Contohnya, `-n 10` akan menunjukkan 10 baris terakhir.
- `-f`: Mengikuti fail secara langsung, memaparkan baris baru yang ditambahkan secara masa nyata.
- `-c [number]`: Menunjukkan bilangan bait terakhir dari fail.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `tail`:

1. Menunjukkan 10 baris terakhir dari fail `log.txt`:
   ```csh
   tail -n 10 log.txt
   ```

2. Mengikuti fail `log.txt` secara langsung untuk melihat kemas kini baru:
   ```csh
   tail -f log.txt
   ```

3. Menunjukkan 50 bait terakhir dari fail `data.txt`:
   ```csh
   tail -c 50 data.txt
   ```

4. Menunjukkan 5 baris terakhir dari beberapa fail:
   ```csh
   tail -n 5 file1.txt file2.txt
   ```

## Tips
- Gunakan pilihan `-f` untuk memantau fail log secara langsung, sangat berguna untuk debugging.
- Anda boleh menggabungkan pilihan, seperti `tail -n 20 -f log.txt`, untuk melihat 20 baris terakhir dan mengikuti kemas kini.
- Jika anda ingin menghentikan pemantauan fail dengan `-f`, tekan `Ctrl + C`.