# [Linux] C Shell (csh) pacman Penggunaan: Mengurus pakej perisian

## Overview
Perintah `pacman` adalah pengurus pakej yang digunakan dalam sistem operasi Arch Linux dan derivatifnya. Ia membolehkan pengguna untuk memasang, mengemas kini, dan menghapuskan perisian dengan mudah.

## Usage
Sintaks asas untuk menggunakan `pacman` adalah seperti berikut:

```bash
pacman [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa yang boleh digunakan dengan `pacman`:

- `-S`: Memasang pakej.
- `-R`: Menghapuskan pakej.
- `-U`: Mengemas kini pakej dari fail.
- `-Sy`: Mengemas kini senarai pakej tanpa mengemas kini sistem.
- `-Ss`: Mencari pakej dalam repositori.

## Common Examples
Berikut adalah beberapa contoh penggunaan `pacman`:

1. **Memasang pakej**:
   ```bash
   pacman -S nama_pakej
   ```

2. **Menghapuskan pakej**:
   ```bash
   pacman -R nama_pakej
   ```

3. **Mengemas kini semua pakej**:
   ```bash
   pacman -Syu
   ```

4. **Mencari pakej dalam repositori**:
   ```bash
   pacman -Ss nama_pakej
   ```

5. **Mengemas kini pakej dari fail**:
   ```bash
   pacman -U /path/to/package.pkg.tar.zst
   ```

## Tips
- Sentiasa pastikan sistem anda dikemas kini dengan menggunakan `pacman -Syu` secara berkala.
- Gunakan `pacman -Qdt` untuk mencari pakej yang tidak lagi diperlukan oleh sistem.
- Simpan salinan fail pakej yang telah dimuat turun untuk memudahkan pemasangan semula di masa hadapan.