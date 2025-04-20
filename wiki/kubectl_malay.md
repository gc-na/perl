# [Sistem Operasi] C Shell (csh) kubectl Penggunaan: Mengurus kluster Kubernetes

## Overview
Perintah `kubectl` adalah alat baris perintah yang digunakan untuk berinteraksi dengan kluster Kubernetes. Ia membolehkan pengguna untuk mengurus sumber daya dalam kluster, seperti pod, servis, dan pengaturan lain yang berkaitan dengan aplikasi yang berjalan di Kubernetes.

## Usage
Sintaks asas untuk menggunakan `kubectl` adalah seperti berikut:

```
kubectl [options] [arguments]
```

## Common Options
- `get`: Mengambil maklumat tentang sumber daya tertentu.
- `create`: Membuat sumber daya baru dalam kluster.
- `delete`: Menghapus sumber daya yang ada.
- `apply`: Mengaplikasikan perubahan pada sumber daya berdasarkan fail konfigurasi.
- `describe`: Memberikan maklumat terperinci tentang sumber daya tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan `kubectl`:

1. **Mengambil senarai pod dalam kluster:**
   ```bash
   kubectl get pods
   ```

2. **Membuat pod baru dari fail YAML:**
   ```bash
   kubectl create -f pod.yaml
   ```

3. **Menghapus pod tertentu:**
   ```bash
   kubectl delete pod nama-pod
   ```

4. **Mengaplikasikan perubahan dari fail konfigurasi:**
   ```bash
   kubectl apply -f deployment.yaml
   ```

5. **Mendapatkan maklumat terperinci tentang servis:**
   ```bash
   kubectl describe service nama-servis
   ```

## Tips
- Sentiasa gunakan `kubectl get` untuk memeriksa status sumber daya selepas melakukan perubahan.
- Gunakan fail YAML untuk mengurus konfigurasi sumber daya dengan lebih mudah dan teratur.
- Manfaatkan `kubectl --help` untuk mendapatkan maklumat lanjut tentang pilihan dan argumen yang tersedia.