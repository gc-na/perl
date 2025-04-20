# [Linux] C Shell (csh) update-rc.d: [mengurus skrip permulaan]

## Overview
Perintah `update-rc.d` digunakan dalam sistem operasi Linux untuk mengurus skrip permulaan (init scripts) yang mengawal perkhidmatan semasa boot. Ia membolehkan pengguna untuk menambah, menghapus, atau mengubah suai skrip permulaan untuk pelbagai perkhidmatan.

## Usage
Berikut adalah sintaks asas untuk menggunakan perintah `update-rc.d`:

```
update-rc.d [options] [arguments]
```

## Common Options
- `defaults`: Menambah skrip permulaan dengan tetapan lalai.
- `remove`: Menghapus skrip permulaan dari sistem.
- `enable`: Mengaktifkan skrip permulaan.
- `disable`: Menonaktifkan skrip permulaan.
- `start <runlevel>`: Menentukan tahap permulaan untuk menjalankan skrip.
- `stop <runlevel>`: Menentukan tahap permulaan untuk menghentikan skrip.

## Common Examples
Berikut adalah beberapa contoh praktikal menggunakan `update-rc.d`:

1. **Menambah skrip permulaan dengan tetapan lalai:**
   ```bash
   sudo update-rc.d myservice defaults
   ```

2. **Menghapus skrip permulaan:**
   ```bash
   sudo update-rc.d myservice remove
   ```

3. **Mengaktifkan skrip permulaan:**
   ```bash
   sudo update-rc.d myservice enable
   ```

4. **Menonaktifkan skrip permulaan:**
   ```bash
   sudo update-rc.d myservice disable
   ```

5. **Menentukan tahap permulaan untuk menjalankan skrip:**
   ```bash
   sudo update-rc.d myservice start 20 2 3 4 5 .
   ```

## Tips
- Sentiasa buat salinan skrip permulaan sebelum melakukan sebarang perubahan.
- Gunakan `update-rc.d` dengan hak akses superuser (sudo) untuk memastikan anda mempunyai kebenaran yang diperlukan.
- Semak dokumentasi perkhidmatan yang anda uruskan untuk memastikan anda menggunakan pilihan yang betul.