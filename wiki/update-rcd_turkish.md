# [Linux] C Shell (csh) update-rc.d Kullanımı: Servisleri başlatma ve durdurma

## Genel Bakış
`update-rc.d` komutu, Linux sistemlerinde hizmetlerin (servislerin) başlangıçta otomatik olarak başlatılması veya durdurulması için gerekli olan bağlantıları ayarlamak amacıyla kullanılır. Bu komut, özellikle Debian tabanlı dağıtımlarda yaygın olarak kullanılır.

## Kullanım
Temel sözdizimi şu şekildedir:
```csh
update-rc.d [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `defaults`: Varsayılan başlangıç ve durdurma seviyelerini ayarlar.
- `remove`: Belirtilen hizmetin başlangıç bağlantılarını kaldırır.
- `enable`: Hizmeti başlatma seviyelerine ekler.
- `disable`: Hizmeti başlatma seviyelerinden çıkarır.

## Yaygın Örnekler
Aşağıda `update-rc.d` komutunun bazı pratik kullanımları verilmiştir:

### Varsayılan Ayarları Kullanma
Bir hizmeti varsayılan ayarlarla eklemek için:
```csh
update-rc.d myservice defaults
```

### Hizmeti Kaldırma
Bir hizmetin başlangıç bağlantılarını kaldırmak için:
```csh
update-rc.d myservice remove
```

### Hizmeti Etkinleştirme
Bir hizmeti başlatma seviyelerine eklemek için:
```csh
update-rc.d myservice enable
```

### Hizmeti Devre Dışı Bırakma
Bir hizmeti başlatma seviyelerinden çıkarmak için:
```csh
update-rc.d myservice disable
```

## İpuçları
- Hizmetlerin doğru şekilde çalıştığından emin olmak için, her değişiklikten sonra sisteminizi yeniden başlatmayı unutmayın.
- `update-rc.d` komutunu kullanmadan önce, hizmetin doğru bir şekilde yapılandırıldığından emin olun.
- Komutları çalıştırmak için genellikle yönetici (root) yetkilerine ihtiyaç duyarsınız, bu nedenle `sudo` kullanmayı unutmayın.