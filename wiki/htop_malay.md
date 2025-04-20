# [Sistem Operasi] C Shell (csh) htop: Memantau penggunaan sumber

## Overview
Perintah `htop` adalah alat pemantauan sistem interaktif yang membolehkan pengguna melihat proses yang sedang berjalan dalam sistem operasi. Ia memberikan pandangan yang lebih baik dan lebih mudah dibaca berbanding dengan perintah `top`, dengan sokongan untuk navigasi menggunakan kunci anak panah dan pilihan untuk menamatkan proses dengan mudah.

## Usage
Sintaks asas untuk menggunakan `htop` adalah seperti berikut:

```csh
htop [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa yang boleh digunakan dengan `htop`:

- `-d <delay>`: Menetapkan selang masa antara kemas kini (dalam saat).
- `-p <pid>`: Menunjukkan hanya proses dengan ID proses tertentu.
- `-s <sort_column>`: Menyusun proses berdasarkan lajur tertentu (contohnya, `PID`, `MEM`, `CPU`).
- `--help`: Menunjukkan maklumat bantuan mengenai penggunaan `htop`.

## Common Examples
Berikut adalah beberapa contoh penggunaan `htop`:

1. **Menjalankan htop secara asas:**
   ```csh
   htop
   ```

2. **Menetapkan selang kemas kini kepada 2 saat:**
   ```csh
   htop -d 2
   ```

3. **Menunjukkan proses tertentu dengan ID proses 1234:**
   ```csh
   htop -p 1234
   ```

4. **Menyusun proses berdasarkan penggunaan CPU:**
   ```csh
   htop -s CPU
   ```

## Tips
- Gunakan kunci anak panah untuk menavigasi senarai proses dan tekan `F9` untuk menamatkan proses yang dipilih.
- Anda boleh menapis proses dengan menekan `F3` dan memasukkan nama proses yang ingin dicari.
- Untuk mengubah cara proses disusun, tekan `F6` dan pilih lajur yang diingini.

Dengan menggunakan `htop`, anda dapat memantau dan mengurus proses dalam sistem anda dengan lebih berkesan.