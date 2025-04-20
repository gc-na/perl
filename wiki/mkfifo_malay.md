# [Linux] C Shell (csh) mkfifo: Membuat fail FIFO

## Overview
Perintah `mkfifo` dalam C Shell (csh) digunakan untuk membuat fail FIFO (First In, First Out). Fail FIFO adalah jenis fail khas yang membolehkan komunikasi antara proses dengan cara yang teratur, di mana data yang ditulis ke dalam fail FIFO akan dibaca dalam urutan yang sama.

## Usage
Sintaks asas untuk menggunakan perintah `mkfifo` adalah seperti berikut:

```
mkfifo [options] [arguments]
```

## Common Options
- `-m` : Menetapkan izin untuk fail FIFO yang baru dibuat.
- `-Z` : Menetapkan konteks SELinux untuk fail FIFO.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `mkfifo`:

1. **Membuat fail FIFO dengan nama `myfifo`:**
   ```csh
   mkfifo myfifo
   ```

2. **Membuat fail FIFO dengan izin tertentu:**
   ```csh
   mkfifo -m 644 myfifo
   ```

3. **Membuat beberapa fail FIFO sekaligus:**
   ```csh
   mkfifo fifo1 fifo2 fifo3
   ```

4. **Membuat fail FIFO dengan konteks SELinux:**
   ```csh
   mkfifo -Z myfifo
   ```

## Tips
- Pastikan untuk menghapus fail FIFO setelah selesai menggunakannya untuk mengelakkan kekeliruan.
- Gunakan perintah `ls -l` untuk memeriksa izin fail FIFO yang telah dibuat.
- Ingat bahawa fail FIFO hanya berfungsi jika ada proses yang membaca dan menulis ke dalamnya secara serentak.