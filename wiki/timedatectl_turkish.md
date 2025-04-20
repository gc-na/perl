# [Linux] C Shell (csh) timedatectl Kullanımı: Zaman ve tarih ayarlarını yönetme

## Genel Bakış
`timedatectl` komutu, sistemin zaman ve tarih ayarlarını yönetmek için kullanılan bir araçtır. Bu komut, sistem saatini, tarihini ve zaman dilimini ayarlamanıza olanak tanır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```csh
timedatectl [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `set-time`: Sistemin saatini ayarlamak için kullanılır.
- `set-timezone`: Zaman dilimini değiştirmek için kullanılır.
- `status`: Mevcut zaman ve tarih ayarlarını görüntüler.
- `list-timezones`: Tüm mevcut zaman dilimlerini listeler.

## Yaygın Örnekler
Aşağıda `timedatectl` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### 1. Mevcut Zaman ve Tarih Bilgilerini Görüntüleme
```csh
timedatectl status
```

### 2. Sistemin Zaman Dilimini Ayarlama
```csh
timedatectl set-timezone Europe/Istanbul
```

### 3. Sistemin Saatini Ayarlama
```csh
timedatectl set-time '2023-10-01 12:00:00'
```

### 4. Tüm Zaman Dilimlerini Listeleme
```csh
timedatectl list-timezones
```

## İpuçları
- Zaman dilimlerini ayarlamadan önce mevcut zaman diliminizi kontrol etmek iyi bir uygulamadır.
- Saat ayarlamalarını yaparken, sistem saatinin doğru olduğundan emin olun.
- `timedatectl` komutunu kullanmadan önce yönetici (root) yetkilerine sahip olduğunuzdan emin olun.