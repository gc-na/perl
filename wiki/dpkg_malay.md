# [Linux] C Shell (csh) dpkg Penggunaan: Mengurus pakej dalam sistem Debian

## Overview
Perintah `dpkg` adalah alat pengurusan pakej untuk sistem berasaskan Debian. Ia digunakan untuk memasang, mengeluarkan, dan mengurus pakej perisian dalam format `.deb`.

## Usage
Sintaks asas untuk menggunakan `dpkg` adalah seperti berikut:

```
dpkg [options] [arguments]
```

## Common Options
- `-i` : Memasang pakej dari fail `.deb`.
- `-r` : Mengeluarkan pakej yang telah dipasang.
- `-l` : Menyenaraikan semua pakej yang telah dipasang.
- `-s` : Menunjukkan status pakej tertentu.
- `-c` : Menunjukkan kandungan pakej `.deb`.

## Common Examples
Berikut adalah beberapa contoh penggunaan `dpkg`:

1. **Memasang pakej dari fail `.deb`:**
   ```bash
   dpkg -i nama-pakej.deb
   ```

2. **Mengeluarkan pakej yang telah dipasang:**
   ```bash
   dpkg -r nama-pakej
   ```

3. **Menyenaraikan semua pakej yang telah dipasang:**
   ```bash
   dpkg -l
   ```

4. **Menunjukkan status pakej tertentu:**
   ```bash
   dpkg -s nama-pakej
   ```

5. **Menunjukkan kandungan pakej `.deb`:**
   ```bash
   dpkg -c nama-pakej.deb
   ```

## Tips
- Sentiasa gunakan `dpkg` dengan hak akses `sudo` jika anda perlu memasang atau mengeluarkan pakej.
- Untuk mengelakkan masalah ketergantungan, gunakan `apt-get` atau `apt` selepas `dpkg` untuk menyelesaikan sebarang isu yang mungkin timbul.
- Simpan salinan fail `.deb` yang telah dimuat turun untuk rujukan masa depan atau pemasangan semula.