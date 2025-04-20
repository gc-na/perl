# [Linux] C Shell (csh) ssh Penggunaan: Menghubungkan ke pelayan secara selamat

## Overview
Perintah `ssh` (Secure Shell) digunakan untuk menghubungkan ke pelayan lain secara selamat melalui rangkaian. Ia membolehkan pengguna untuk mengakses dan mengawal sistem jauh dengan cara yang selamat.

## Usage
Berikut adalah sintaks asas untuk perintah `ssh`:

```
ssh [options] [user@]hostname
```

## Common Options
- `-p [port]`: Menentukan nombor port yang digunakan untuk sambungan.
- `-i [file]`: Menentukan fail kunci peribadi untuk pengesahan.
- `-v`: Mengaktifkan mod verbose untuk mendapatkan maklumat lebih lanjut tentang sambungan.
- `-X`: Mengaktifkan pengalihan X11 untuk aplikasi grafik.

## Common Examples
Berikut adalah beberapa contoh penggunaan `ssh`:

1. **Sambungan ke pelayan dengan nama pengguna:**
   ```bash
   ssh user@hostname
   ```

2. **Sambungan ke pelayan pada port tertentu:**
   ```bash
   ssh -p 2222 user@hostname
   ```

3. **Menggunakan kunci peribadi untuk pengesahan:**
   ```bash
   ssh -i ~/.ssh/id_rsa user@hostname
   ```

4. **Mengaktifkan pengalihan X11:**
   ```bash
   ssh -X user@hostname
   ```

## Tips
- Sentiasa gunakan kunci peribadi untuk pengesahan yang lebih selamat berbanding kata laluan.
- Gunakan mod verbose (`-v`) untuk menyelesaikan masalah sambungan jika perlu.
- Simpan alamat pelayan dan pilihan sambungan dalam fail `~/.ssh/config` untuk kemudahan akses.