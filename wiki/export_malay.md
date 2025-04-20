# [Linux] C Shell (csh) export: Menguruskan Pembolehubah Persekitaran

## Overview
Perintah `export` dalam C Shell (csh) digunakan untuk menetapkan dan menguruskan pembolehubah persekitaran. Pembolehubah ini membolehkan pengguna untuk menyimpan maklumat yang boleh diakses oleh proses dan skrip lain dalam sesi terminal.

## Usage
Sintaks asas bagi perintah `export` adalah seperti berikut:

```
export [options] [arguments]
```

## Common Options
- `-n` : Menghapuskan pembolehubah daripada senarai pembolehubah persekitaran.
- `-p` : Memaparkan semua pembolehubah persekitaran yang telah ditetapkan.

## Common Examples

### Menetapkan Pembolehubah Persekitaran
Untuk menetapkan pembolehubah persekitaran baru, gunakan perintah berikut:

```csh
setenv MY_VAR "Hello, World!"
```

### Mengakses Pembolehubah Persekitaran
Anda boleh mengakses pembolehubah yang telah ditetapkan dengan menggunakan perintah `echo`:

```csh
echo $MY_VAR
```

### Memaparkan Semua Pembolehubah Persekitaran
Untuk melihat semua pembolehubah persekitaran yang telah ditetapkan, gunakan:

```csh
export -p
```

### Menghapuskan Pembolehubah Persekitaran
Jika anda ingin menghapuskan pembolehubah persekitaran, gunakan:

```csh
unsetenv MY_VAR
```

## Tips
- Sentiasa gunakan `setenv` untuk menetapkan pembolehubah persekitaran dalam C Shell.
- Pastikan nama pembolehubah persekitaran adalah jelas dan deskriptif untuk memudahkan pengurusan.
- Gunakan `export -p` untuk menyemak pembolehubah yang telah ditetapkan sebelum membuat perubahan.