# [Sistem Operasi] C Shell (csh) 7z Penggunaan: Mengurus fail arkib

## Overview
Perintah `7z` adalah alat yang digunakan untuk mengurus fail arkib, termasuk membuat, mengekstrak, dan mengurus pelbagai format arkib seperti ZIP, RAR, dan 7z. Ia terkenal dengan kecekapan dan kadar pemampatan yang tinggi.

## Usage
Sintaks asas untuk perintah `7z` adalah seperti berikut:

```
7z [options] [arguments]
```

## Common Options
- `a` : Menambah fail ke dalam arkib.
- `x` : Mengekstrak fail dari arkib.
- `l` : Menyenaraikan kandungan arkib.
- `d` : Memadam fail dari arkib.
- `t` : Menguji arkib untuk memastikan ia tidak rosak.

## Common Examples
Berikut adalah beberapa contoh praktikal penggunaan `7z`:

1. **Membuat arkib baru:**
   ```bash
   7z a fail_arkib.7z fail1.txt fail2.txt
   ```

2. **Mengekstrak kandungan arkib:**
   ```bash
   7z x fail_arkib.7z
   ```

3. **Menyenaraikan kandungan arkib:**
   ```bash
   7z l fail_arkib.7z
   ```

4. **Memadam fail dari arkib:**
   ```bash
   7z d fail_arkib.7z fail1.txt
   ```

5. **Mengujinya untuk kerosakan:**
   ```bash
   7z t fail_arkib.7z
   ```

## Tips
- Sentiasa gunakan pilihan `l` untuk menyemak kandungan arkib sebelum mengekstrak, bagi memastikan anda tahu apa yang akan diekstrak.
- Gunakan pilihan `-p` untuk menetapkan kata laluan bagi arkib yang sensitif.
- Untuk pemampatan yang lebih baik, pertimbangkan untuk menggunakan format `7z` berbanding format lain seperti ZIP.