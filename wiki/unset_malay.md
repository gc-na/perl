# [Sistem Operasi] C Shell (csh) unset: Menghapus pembolehubah

## Overview
Perintah `unset` dalam C Shell (csh) digunakan untuk menghapus pembolehubah daripada persekitaran semasa. Ini bermakna pembolehubah yang dihapuskan tidak lagi tersedia untuk digunakan dalam sesi shell yang sama.

## Usage
Sintaks asas untuk perintah `unset` adalah seperti berikut:

```csh
unset [options] [arguments]
```

## Common Options
- `-f`: Menghapus fungsi yang ditakrifkan.
- `-v`: Menghapus pembolehubah biasa.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `unset`:

1. **Menghapus pembolehubah biasa:**
   ```csh
   set var="Hello, World!"
   unset var
   ```

2. **Menghapus fungsi:**
   ```csh
   function myFunc {
       echo "This is my function"
   }
   unset -f myFunc
   ```

3. **Menghapus lebih daripada satu pembolehubah:**
   ```csh
   set var1="Value1"
   set var2="Value2"
   unset var1 var2
   ```

## Tips
- Pastikan anda tidak menghapus pembolehubah yang diperlukan untuk operasi lain dalam skrip anda.
- Gunakan `echo $var` sebelum dan selepas menggunakan `unset` untuk memeriksa sama ada pembolehubah telah dihapuskan dengan betul.
- Untuk mengelakkan kesilapan, pertimbangkan untuk menyemak senarai pembolehubah semasa dengan menggunakan perintah `set` sebelum menghapusnya.