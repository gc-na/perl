# [Linux] C Shell (csh) jobs: Menguruskan proses latar belakang

## Overview
Perintah `jobs` dalam C Shell (csh) digunakan untuk menyenaraikan proses yang sedang berjalan di latar belakang dalam sesi terminal semasa. Ini membolehkan pengguna melihat status proses yang telah dijalankan, sama ada ia sedang berjalan, dihentikan, atau telah selesai.

## Usage
Sintaks asas untuk menggunakan perintah `jobs` adalah seperti berikut:

```
jobs [options] [arguments]
```

## Common Options
Berikut adalah beberapa pilihan biasa untuk perintah `jobs`:

- `-l`: Menunjukkan ID proses (PID) untuk setiap proses yang disenaraikan.
- `-n`: Menunjukkan hanya proses yang baru sahaja berubah status.
- `-p`: Menunjukkan hanya ID proses (PID) tanpa maklumat lain.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `jobs`:

1. **Menyenaraikan semua proses latar belakang:**
   ```csh
   jobs
   ```

2. **Menyenaraikan proses dengan ID proses:**
   ```csh
   jobs -l
   ```

3. **Menyenaraikan hanya proses yang baru berubah status:**
   ```csh
   jobs -n
   ```

4. **Mendapatkan ID proses untuk proses tertentu:**
   ```csh
   jobs -p
   ```

## Tips
- Sentiasa semak status proses latar belakang sebelum menutup terminal untuk memastikan tiada proses penting yang terhenti.
- Gunakan perintah `fg` untuk membawa proses latar belakang ke hadapan jika anda perlu berinteraksi dengannya.
- Jika anda ingin menghentikan proses latar belakang, gunakan perintah `kill` bersama dengan ID proses yang diperoleh dari `jobs -l`.