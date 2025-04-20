# [Sistem Operasi] C Shell (csh) helm penggunaan: Mengurus aplikasi dalam Kubernetes

## Overview
Perintah `helm` digunakan untuk mengurus aplikasi dalam persekitaran Kubernetes. Ia berfungsi sebagai pengurus pakej untuk Kubernetes, membolehkan pengguna untuk memasang, mengemas kini, dan menghapus aplikasi dengan mudah.

## Usage
Sintaks asas untuk perintah helm adalah seperti berikut:

```bash
helm [options] [arguments]
```

## Common Options
- `install`: Memasang chart baru.
- `upgrade`: Mengemas kini chart yang sedia ada.
- `uninstall`: Menghapus chart yang telah dipasang.
- `list`: Menyenaraikan semua release yang telah dipasang.
- `repo`: Mengurus repositori chart.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah helm:

1. **Memasang chart baru**:
   ```bash
   helm install nama-release nama-chart
   ```

2. **Mengemas kini chart yang sedia ada**:
   ```bash
   helm upgrade nama-release nama-chart
   ```

3. **Menghapus chart**:
   ```bash
   helm uninstall nama-release
   ```

4. **Menyenaraikan semua release**:
   ```bash
   helm list
   ```

5. **Menambah repositori chart**:
   ```bash
   helm repo add nama-repo url-repo
   ```

## Tips
- Sentiasa semak versi chart sebelum memasang untuk memastikan keserasian.
- Gunakan `helm search` untuk mencari chart yang sesuai dalam repositori.
- Simpan konfigurasi helm dalam sistem kawalan versi untuk pengurusan yang lebih baik.