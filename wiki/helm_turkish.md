# [Linux] C Shell (csh) helm kullanımı: Helm ile uygulama yönetimi

## Genel Bakış
Helm, Kubernetes üzerinde uygulama yönetimini kolaylaştıran bir paket yöneticisidir. Helm, uygulamaları ve bunların bağımlılıklarını tanımlamak, kurmak ve güncellemek için kullanılır. Helm, Kubernetes üzerinde uygulama dağıtımını basit ve tekrarlanabilir hale getirir.

## Kullanım
Helm komutunun temel sözdizimi aşağıdaki gibidir:

```bash
helm [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `install`: Yeni bir uygulama kurar.
- `upgrade`: Mevcut bir uygulamayı günceller.
- `uninstall`: Kurulu bir uygulamayı kaldırır.
- `list`: Kurulu uygulamaların listesini gösterir.
- `repo`: Helm depolarını yönetmek için kullanılır.

## Yaygın Örnekler
Aşağıda helm komutunun bazı pratik örnekleri verilmiştir:

1. Yeni bir uygulama kurmak için:
   ```bash
   helm install my-app my-repo/my-chart
   ```

2. Mevcut bir uygulamayı güncellemek için:
   ```bash
   helm upgrade my-app my-repo/my-chart
   ```

3. Kurulu uygulamaların listesini görüntülemek için:
   ```bash
   helm list
   ```

4. Bir uygulamayı kaldırmak için:
   ```bash
   helm uninstall my-app
   ```

5. Helm deposunu eklemek için:
   ```bash
   helm repo add my-repo https://my-repo-url
   ```

## İpuçları
- Helm chart'larınızı versiyon kontrol sisteminde saklayarak değişikliklerinizi takip edin.
- Uygulama güncellemeleri sırasında rollback (geri alma) işlemini kullanarak önceki sürümlere dönebilirsiniz.
- Helm komutlarını çalıştırmadan önce `helm repo update` komutunu kullanarak depolarınızı güncel tutun.