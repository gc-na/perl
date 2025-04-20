# [Linux] C Shell (csh) nl: Menambah nombor baris pada fail teks

## Overview
Perintah `nl` dalam C Shell digunakan untuk menambah nombor baris pada fail teks. Ia membantu dalam memudahkan pembacaan dan rujukan pada teks yang panjang dengan memberikan nombor pada setiap baris.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `nl`:

```csh
nl [options] [arguments]
```

## Common Options
- `-b` : Menentukan cara nombor baris ditambah. Contohnya, `-b a` untuk menambah nombor pada setiap baris.
- `-f` : Menentukan baris yang tidak perlu dinomborkan.
- `-n` : Menentukan format nombor baris. Contohnya, `-n ln` untuk nombor baris dalam format kiri.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `nl`:

1. Menambah nombor baris pada fail teks:
   ```csh
   nl myfile.txt
   ```

2. Menambah nombor baris pada setiap baris tanpa mengabaikan baris kosong:
   ```csh
   nl -b a myfile.txt
   ```

3. Menyimpan output ke dalam fail baru:
   ```csh
   nl myfile.txt > myfile_numbered.txt
   ```

4. Menggunakan format nombor baris kanan:
   ```csh
   nl -n rn myfile.txt
   ```

## Tips
- Gunakan pilihan `-b` untuk mengawal baris mana yang dinomborkan, terutama jika anda mempunyai baris kosong yang ingin diabaikan.
- Simpan output ke dalam fail baru jika anda ingin mengekalkan fail asal tanpa perubahan.
- Eksperimen dengan pilihan `-n` untuk mendapatkan format nombor yang sesuai dengan keperluan anda.