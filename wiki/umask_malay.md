# [Linux] C Shell (csh) umask: Mengawal kebenaran fail

## Overview
Perintah `umask` dalam C Shell (csh) digunakan untuk menetapkan nilai umask yang menentukan kebenaran lalai untuk fail dan direktori baru yang dicipta. Ia mengawal kebenaran akses yang akan ditetapkan secara automatik apabila fail atau direktori baru dibuat.

## Usage
Sintaks asas untuk perintah `umask` adalah seperti berikut:

```
umask [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan umum untuk `umask`:

- `-S` : Menunjukkan nilai umask dalam format simbolik.
- `-p` : Menunjukkan nilai umask semasa dalam format simbolik.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `umask`:

1. **Menetapkan nilai umask kepada 022**:
   ```csh
   umask 022
   ```

2. **Memeriksa nilai umask semasa**:
   ```csh
   umask
   ```

3. **Menunjukkan nilai umask dalam format simbolik**:
   ```csh
   umask -S
   ```

4. **Menetapkan nilai umask kepada 007**:
   ```csh
   umask 007
   ```

## Tips
- Sentiasa semak nilai umask semasa sebelum mencipta fail atau direktori untuk memastikan kebenaran yang diingini.
- Gunakan nilai umask yang lebih ketat untuk meningkatkan keselamatan fail, terutamanya pada sistem pelayan.
- Pertimbangkan untuk menetapkan umask dalam fail konfigurasi shell anda untuk memastikan nilai tersebut digunakan secara konsisten setiap kali anda log masuk.