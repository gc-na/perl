# [Sistem Operasi] C Shell (csh) grep Penggunaan: Mencari pola dalam teks

## Overview
Perintah `grep` digunakan untuk mencari pola dalam teks. Ini sangat berguna untuk menemukan baris yang mengandung string tertentu dalam file atau output dari perintah lain.

## Usage
Berikut adalah sintaks dasar dari perintah `grep`:

```csh
grep [options] [arguments]
```

## Common Options
- `-i`: Mengabaikan perbedaan antara huruf besar dan kecil saat mencari.
- `-v`: Menampilkan baris yang tidak cocok dengan pola yang diberikan.
- `-r`: Mencari secara rekursif dalam direktori.
- `-n`: Menampilkan nomor baris dari hasil pencarian.
- `-l`: Menampilkan nama file yang mengandung pola yang dicari.

## Common Examples
Berikut adalah beberapa contoh penggunaan `grep`:

1. Mencari kata "error" dalam file `log.txt`:
   ```csh
   grep "error" log.txt
   ```

2. Mencari kata "warning" tanpa memperhatikan huruf besar/kecil:
   ```csh
   grep -i "warning" log.txt
   ```

3. Menampilkan nomor baris saat mencari kata "success":
   ```csh
   grep -n "success" log.txt
   ```

4. Mencari pola dalam semua file dengan ekstensi `.txt` di direktori saat ini:
   ```csh
   grep "pattern" *.txt
   ```

5. Mencari secara rekursif untuk kata "TODO" dalam direktori proyek:
   ```csh
   grep -r "TODO" /path/to/project
   ```

## Tips
- Gunakan opsi `-v` untuk menyaring hasil dan hanya menampilkan baris yang tidak sesuai dengan pola.
- Kombinasikan `grep` dengan perintah lain menggunakan pipe (`|`) untuk mencari dalam output perintah tersebut.
- Simpan hasil pencarian ke dalam file dengan menggunakan redirection (`>`):
  ```csh
  grep "error" log.txt > hasil_pencarian.txt
  ```