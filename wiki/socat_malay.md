# [Linux] C Shell (csh) socat: [menghubungkan aliran data]

## Overview
Perintah `socat` adalah alat yang kuat untuk menghubungkan dua aliran data, seperti soket, fail, atau peranti. Ia membolehkan pengguna untuk membuat sambungan antara pelbagai sumber dan destinasi, menjadikannya berguna dalam pelbagai situasi rangkaian dan pemprosesan data.

## Usage
Berikut adalah sintaks asas untuk menggunakan `socat`:

```csh
socat [options] [arguments]
```

## Common Options
- `-d` : Mengaktifkan mod debug untuk mendapatkan maklumat tambahan tentang sambungan.
- `-v` : Mengaktifkan mod verbose untuk menunjukkan lebih banyak maklumat semasa operasi.
- `tcp:` : Menunjukkan bahawa sambungan yang akan dibuat adalah melalui protokol TCP.
- `udp:` : Menunjukkan bahawa sambungan yang akan dibuat adalah melalui protokol UDP.
- `file:` : Menggunakan fail sebagai sumber atau destinasi untuk aliran data.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `socat`:

1. **Menghubungkan dua port TCP**:
   ```csh
   socat TCP-LISTEN:1234,fork TCP:localhost:5678
   ```

2. **Menghantar data dari fail ke soket TCP**:
   ```csh
   socat TCP:localhost:1234 file:/path/to/file.txt
   ```

3. **Membaca dari stdin dan menghantar ke soket UDP**:
   ```csh
   socat -u -v FILE:- UDP:localhost:1234
   ```

4. **Membuat sambungan antara dua fail**:
   ```csh
   socat file:/path/to/input.txt file:/path/to/output.txt
   ```

## Tips
- Sentiasa gunakan pilihan `-d` dan `-v` semasa pengujian untuk mendapatkan maklumat tambahan yang berguna.
- Pastikan port yang anda gunakan tidak sedang digunakan oleh aplikasi lain untuk mengelakkan konflik.
- Gunakan `socat` dalam skrip untuk automasi tugas yang melibatkan pemindahan data antara sumber yang berbeza.