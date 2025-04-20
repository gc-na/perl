# [Linux] C Shell (csh) test penggunaan: Memeriksa ekspresi

## Overview
Perintah `test` dalam C Shell (csh) digunakan untuk mengevaluasi ekspresi dan mengembalikan nilai benar (true) atau salah (false). Ini sering digunakan dalam skrip untuk membuat keputusan berdasarkan syarat tertentu.

## Usage
Sintaks asas untuk perintah `test` adalah seperti berikut:

```csh
test [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk perintah `test`:

- `-e file` : Menguji sama ada fail wujud.
- `-d directory` : Menguji sama ada direktori wujud.
- `-f file` : Menguji sama ada fail adalah fail biasa.
- `-z string` : Menguji sama ada panjang string adalah sifar.
- `string1 = string2` : Menguji sama ada dua string adalah sama.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan perintah `test`:

1. **Menguji kewujudan fail:**
   ```csh
   test -e myfile.txt && echo "Fail wujud"
   ```

2. **Menguji sama ada direktori wujud:**
   ```csh
   test -d /home/user/mydir && echo "Direktori wujud"
   ```

3. **Menguji sama ada fail adalah fail biasa:**
   ```csh
   test -f myscript.sh && echo "Ini adalah fail biasa"
   ```

4. **Menguji sama ada string kosong:**
   ```csh
   mystring=""
   test -z "$mystring" && echo "String adalah kosong"
   ```

5. **Menguji kesamaan dua string:**
   ```csh
   test "hello" = "hello" && echo "String adalah sama"
   ```

## Tips
- Sentiasa gunakan tanda kutip untuk mengelakkan masalah dengan ruang dalam nama fail atau string.
- Gunakan `&&` untuk menggabungkan perintah dan melaksanakan tindakan hanya jika `test` mengembalikan benar.
- Perintah `test` juga boleh ditulis menggunakan tanda kurung persegi `[` dan `]`, contohnya: `[ -e myfile.txt ]`.