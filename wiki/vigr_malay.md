# [Linux] C Shell (csh) vigr Penggunaan: Mengedit fail konfigurasi

## Overview
Perintah `vigr` digunakan untuk mengedit fail konfigurasi sistem yang terletak di `/etc`, seperti fail `passwd` dan `group`. Ia membuka fail tersebut dalam editor teks yang ditetapkan, memastikan bahawa fail tersebut tidak diubah semasa proses pengeditan.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `vigr`:

```csh
vigr [options] [arguments]
```

## Common Options
- `-s`: Menjalankan `vigr` dalam mod selamat, yang akan memeriksa kesilapan dalam fail sebelum menyimpannya.
- `-f <file>`: Menentukan fail yang ingin diedit, jika tidak, `vigr` akan membuka fail lalai.

## Common Examples
Berikut adalah beberapa contoh penggunaan `vigr`:

1. **Mengedit fail passwd**:
    ```csh
    vigr /etc/passwd
    ```

2. **Mengedit fail group**:
    ```csh
    vigr /etc/group
    ```

3. **Menggunakan mod selamat**:
    ```csh
    vigr -s /etc/passwd
    ```

4. **Menentukan fail lain untuk diedit**:
    ```csh
    vigr -f /etc/someconfig.conf
    ```

## Tips
- Sentiasa gunakan `vigr` untuk mengedit fail sistem penting untuk mengelakkan kerosakan pada fail tersebut.
- Pastikan anda mempunyai hak akses yang sesuai sebelum mengedit fail sistem.
- Gunakan pilihan `-s` untuk memastikan fail tidak mempunyai kesilapan sebelum disimpan.