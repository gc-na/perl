# [Linux] C Shell (csh) kubectl Kullanımı: Kubernetes ile etkileşim kurma

## Genel Bakış
`kubectl`, Kubernetes ile etkileşim kurmak için kullanılan bir komut satırı aracıdır. Kubernetes, konteynerleştirilmiş uygulamaların otomatik dağıtımını, ölçeklenmesini ve yönetimini sağlayan bir platformdur. `kubectl`, kullanıcıların Kubernetes kümesine komutlar göndermesine ve kaynakları yönetmesine olanak tanır.

## Kullanım
`kubectl` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
kubectl [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `get`: Belirtilen kaynak türlerini listelemek için kullanılır.
- `describe`: Belirtilen bir kaynağın ayrıntılı bilgilerini gösterir.
- `apply`: Bir kaynak tanımını uygulamak veya güncellemek için kullanılır.
- `delete`: Belirtilen bir kaynağı silmek için kullanılır.

## Yaygın Örnekler
Aşağıda `kubectl` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### Tüm Pod'ları Listeleme
```bash
kubectl get pods
```

### Belirli Bir Pod Hakkında Bilgi Alma
```bash
kubectl describe pod <pod-adı>
```

### Bir Kaynağı Uygulama
```bash
kubectl apply -f <dosya.yaml>
```

### Bir Kaynağı Silme
```bash
kubectl delete pod <pod-adı>
```

## İpuçları
- `kubectl` komutunu kullanmadan önce, Kubernetes kümesine erişiminizin olduğundan emin olun.
- Komutları daha hızlı yazmak için `kubectl` için alias tanımlayabilirsiniz.
- `--help` seçeneğini kullanarak belirli bir komut hakkında daha fazla bilgi alabilirsiniz. Örneğin: `kubectl get --help`.