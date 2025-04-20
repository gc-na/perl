# [Sistem Operasi] C Shell (csh) netstat: Memaparkan statistik rangkaian

## Overview
Perintah `netstat` digunakan untuk memaparkan statistik rangkaian dan maklumat tentang sambungan rangkaian yang aktif. Ia membantu pengguna untuk memantau dan mendiagnosis masalah rangkaian dengan memberikan maklumat tentang sambungan TCP/IP, protokol, dan statistik lain.

## Usage
Sintaks asas bagi perintah `netstat` adalah seperti berikut:

```
netstat [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk `netstat` beserta penjelasan ringkas:

- `-a`: Memaparkan semua sambungan dan port yang mendengar.
- `-n`: Memaparkan alamat IP dan nombor port dalam format numerik.
- `-r`: Memaparkan jadual penghalaan rangkaian.
- `-s`: Memaparkan statistik untuk setiap protokol.
- `-p`: Menunjukkan proses yang berkaitan dengan sambungan.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `netstat`:

1. **Memaparkan semua sambungan dan port yang mendengar:**
   ```csh
   netstat -a
   ```

2. **Memaparkan sambungan dalam format numerik:**
   ```csh
   netstat -n
   ```

3. **Memaparkan jadual penghalaan rangkaian:**
   ```csh
   netstat -r
   ```

4. **Memaparkan statistik untuk setiap protokol:**
   ```csh
   netstat -s
   ```

5. **Menunjukkan proses yang berkaitan dengan sambungan:**
   ```csh
   netstat -p
   ```

## Tips
- Gunakan pilihan `-n` untuk mempercepatkan output, terutamanya jika anda tidak memerlukan nama host.
- Gabungkan pilihan untuk mendapatkan maklumat yang lebih terperinci, contohnya `netstat -anp`.
- Sentiasa periksa sambungan yang tidak dikenali untuk memastikan keselamatan rangkaian anda.