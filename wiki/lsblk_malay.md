# [Linux] C Shell (csh) lsblk Penggunaan: Menyenaraikan peranti blok

## Overview
Perintah `lsblk` digunakan untuk menyenaraikan semua peranti blok yang tersedia dalam sistem. Ini termasuk cakera keras, pemacu USB, dan partisi yang ada, memberikan pandangan yang jelas tentang struktur penyimpanan.

## Usage
Sintaks asas untuk perintah `lsblk` adalah seperti berikut:

```csh
lsblk [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `lsblk` beserta penjelasan ringkas:

- `-a` : Menunjukkan semua peranti, termasuk yang tidak terpasang.
- `-f` : Menunjukkan sistem fail pada setiap peranti.
- `-o` : Menentukan lajur yang ingin ditunjukkan dalam output.
- `-p` : Menunjukkan nama peranti penuh.
- `-n` : Menghilangkan tajuk dalam output.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `lsblk`:

1. **Menyenaraikan semua peranti blok:**
   ```csh
   lsblk
   ```

2. **Menyenaraikan peranti dengan sistem fail:**
   ```csh
   lsblk -f
   ```

3. **Menyenaraikan peranti dengan lajur khusus:**
   ```csh
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
   ```

4. **Menunjukkan semua peranti termasuk yang tidak terpasang:**
   ```csh
   lsblk -a
   ```

5. **Menunjukkan nama peranti penuh:**
   ```csh
   lsblk -p
   ```

## Tips
- Gunakan pilihan `-f` untuk mendapatkan maklumat tambahan tentang sistem fail, yang berguna untuk pengurusan penyimpanan.
- Pertimbangkan untuk menggunakan pilihan `-o` untuk menyesuaikan output agar lebih mudah dibaca dan difahami.
- Sentiasa periksa peranti sebelum melakukan operasi yang berisiko, seperti pemformatan atau penghapusan data.