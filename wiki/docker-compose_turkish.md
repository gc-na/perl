# [Linux] C Shell (csh) docker-compose Kullanımı: Docker konteynerlerini yönetmek için bir araç

## Genel Bakış
`docker-compose` komutu, birden fazla Docker konteynerini tanımlamak ve yönetmek için kullanılan bir araçtır. Bu komut, uygulamaların birden fazla servisten oluştuğu durumlarda, bu servislerin birlikte çalışmasını kolaylaştırır. `docker-compose.yml` dosyası aracılığıyla, konteynerlerin yapılandırmasını ve ilişkilerini tanımlayabilirsiniz.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
docker-compose [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `up`: Tanımlı servisleri başlatır.
- `down`: Çalışan servisleri durdurur ve kaldırır.
- `build`: Servisler için imajları oluşturur.
- `logs`: Servislerin günlüklerini görüntüler.
- `exec`: Çalışan bir konteyner içinde komut çalıştırır.

## Yaygın Örnekler
Aşağıda `docker-compose` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### Servisleri Başlatma
Tüm tanımlı servisleri başlatmak için:

```bash
docker-compose up
```

### Servisleri Arka Planda Çalıştırma
Servisleri arka planda çalıştırmak için:

```bash
docker-compose up -d
```

### Servisleri Durdurma
Çalışan servisleri durdurmak için:

```bash
docker-compose down
```

### Günlükleri Görüntüleme
Bir servisin günlüklerini görüntülemek için:

```bash
docker-compose logs [servis_adı]
```

### Konteyner İçinde Komut Çalıştırma
Bir konteyner içinde belirli bir komut çalıştırmak için:

```bash
docker-compose exec [servis_adı] [komut]
```

## İpuçları
- `docker-compose.yml` dosyanızı iyi yapılandırın; bu, servisler arası bağımlılıkları ve yapılandırmaları yönetmeyi kolaylaştırır.
- `docker-compose up -d` komutunu kullanarak servislerinizi arka planda çalıştırabilir ve terminalinizi serbest bırakabilirsiniz.
- Günlükleri izlemek için `docker-compose logs -f` komutunu kullanarak gerçek zamanlı güncellemeleri takip edebilirsiniz.