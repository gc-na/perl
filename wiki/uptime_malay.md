# [Linux] C Shell (csh) uptime: Menunjukkan masa aktif sistem

## Overview
Perintah `uptime` digunakan untuk menunjukkan berapa lama sistem telah berjalan sejak terakhir kali dihidupkan. Ia juga memberikan maklumat mengenai jumlah pengguna yang sedang log masuk dan beban sistem dalam jangka masa tertentu.

## Usage
Sintaks asas untuk perintah `uptime` adalah seperti berikut:

```
uptime [options] [arguments]
```

## Common Options
- `-p`: Menunjukkan masa aktif dalam format yang lebih mudah dibaca.
- `-s`: Menunjukkan masa dan tarikh ketika sistem dihidupkan semula.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `uptime`:

1. **Menunjukkan masa aktif sistem**:
   ```csh
   uptime
   ```

2. **Menunjukkan masa aktif dalam format yang lebih mudah dibaca**:
   ```csh
   uptime -p
   ```

3. **Menunjukkan masa dan tarikh sistem dihidupkan semula**:
   ```csh
   uptime -s
   ```

## Tips
- Gunakan `uptime` secara berkala untuk memantau prestasi sistem dan beban kerja.
- Perhatikan nilai beban (load average) yang ditunjukkan untuk menilai kesihatan sistem.
- Kombinasikan `uptime` dengan perintah lain seperti `who` untuk mendapatkan maklumat lebih lanjut tentang pengguna yang sedang aktif.