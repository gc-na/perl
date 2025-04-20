# [Linux] C Shell (csh) yum kullanımı: Paket yönetimi aracı

## Genel Bakış
`yum`, Red Hat tabanlı Linux dağıtımlarında kullanılan bir paket yönetim aracıdır. Kullanıcıların yazılımları yüklemelerine, güncellemelerine ve kaldırmalarına olanak tanır. `yum`, bağımlılıkları otomatik olarak yöneterek kullanıcıların işini kolaylaştırır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
yum [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `install`: Belirtilen paketi yükler.
- `remove`: Belirtilen paketi kaldırır.
- `update`: Yüklü paketleri günceller.
- `search`: Belirtilen anahtar kelimeye göre paket arar.
- `info`: Belirtilen paket hakkında bilgi verir.

## Yaygın Örnekler
Aşağıda `yum` komutunun bazı pratik örnekleri bulunmaktadır:

### 1. Paket Yükleme
Belirli bir paketi yüklemek için:

```bash
yum install paket_adi
```

### 2. Paket Kaldırma
Yüklü bir paketi kaldırmak için:

```bash
yum remove paket_adi
```

### 3. Paket Güncelleme
Tüm yüklü paketleri güncellemek için:

```bash
yum update
```

### 4. Paket Arama
Belirli bir anahtar kelimeye göre paket aramak için:

```bash
yum search anahtar_kelime
```

### 5. Paket Bilgisi Alma
Bir paket hakkında detaylı bilgi almak için:

```bash
yum info paket_adi
```

## İpuçları
- `yum` komutunu kullanmadan önce, sisteminizin güncel olduğundan emin olun.
- Paket yüklemeden önce, bağımlılıkların kontrol edilmesi için `yum check-update` komutunu kullanabilirsiniz.
- `yum` ile yapılan işlemler genellikle kök (root) yetkileri gerektirir, bu nedenle `sudo` ile birlikte kullanmayı unutmayın.