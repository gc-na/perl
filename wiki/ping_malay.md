# [Sistem Operasi] C Shell (csh) ping Penggunaan: Menguji sambungan rangkaian

## Overview
Perintah `ping` digunakan untuk menguji sambungan rangkaian antara komputer anda dan host lain. Ia menghantar paket data ke alamat IP atau nama domain yang ditentukan dan menunggu balasan, membolehkan anda mengetahui sama ada host tersebut boleh dihubungi dan seberapa cepat sambungan tersebut.

## Usage
Sintaks asas bagi perintah `ping` adalah seperti berikut:

```
ping [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan umum yang boleh digunakan dengan perintah `ping`:

- `-c [count]`: Menentukan jumlah paket yang akan dihantar.
- `-i [interval]`: Menetapkan selang masa antara setiap paket yang dihantar.
- `-s [size]`: Menentukan saiz paket yang akan dihantar.
- `-t [ttl]`: Menetapkan nilai Time To Live untuk paket.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `ping`:

1. Menghantar ping ke alamat IP tertentu:
   ```csh
   ping 192.168.1.1
   ```

2. Menghantar 5 paket ping:
   ```csh
   ping -c 5 google.com
   ```

3. Menghantar ping dengan saiz paket tertentu:
   ```csh
   ping -s 100 google.com
   ```

4. Menghantar ping dengan selang 2 saat antara setiap paket:
   ```csh
   ping -i 2 google.com
   ```

## Tips
- Gunakan pilihan `-c` untuk menghentikan ping secara automatik setelah menghantar jumlah paket yang ditentukan.
- Jika anda ingin memantau sambungan secara berterusan, jalankan `ping` tanpa pilihan `-c`.
- Perhatikan masa respons yang ditunjukkan dalam hasil ping untuk menilai kualiti sambungan rangkaian.