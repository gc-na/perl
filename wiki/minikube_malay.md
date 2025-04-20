# [Sistem Operasi] C Shell (csh) minikube: Mengurus kluster Kubernetes tempatan

## Overview
Minikube adalah alat yang membolehkan pengguna menjalankan kluster Kubernetes tempatan di komputer mereka. Ia sangat berguna untuk pembangunan dan pengujian aplikasi dalam persekitaran Kubernetes tanpa memerlukan infrastruktur yang kompleks.

## Usage
Berikut adalah sintaks asas untuk menggunakan minikube:

```
minikube [options] [arguments]
```

## Common Options
- `start`: Memulakan kluster minikube.
- `stop`: Menghentikan kluster minikube yang sedang berjalan.
- `status`: Menunjukkan status kluster minikube.
- `delete`: Memadam kluster minikube yang telah dibuat.
- `dashboard`: Membuka antaramuka pengguna web untuk mengurus kluster.

## Common Examples
Berikut adalah beberapa contoh penggunaan minikube:

1. **Memulakan kluster minikube:**
   ```csh
   minikube start
   ```

2. **Menghentikan kluster minikube:**
   ```csh
   minikube stop
   ```

3. **Memeriksa status kluster:**
   ```csh
   minikube status
   ```

4. **Memadam kluster minikube:**
   ```csh
   minikube delete
   ```

5. **Membuka dashboard Kubernetes:**
   ```csh
   minikube dashboard
   ```

## Tips
- Sentiasa pastikan bahawa minikube anda dikemas kini untuk mendapatkan ciri-ciri terbaru dan pembetulan pepijat.
- Gunakan `minikube addons` untuk mengaktifkan pelbagai tambahan yang boleh membantu dalam pembangunan aplikasi.
- Simpan konfigurasi minikube anda untuk memudahkan pengurusan kluster di masa hadapan.