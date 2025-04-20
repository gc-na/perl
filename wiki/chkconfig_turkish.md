# [Linux] C Shell (csh) chkconfig Kullanımı: Servislerin yönetimi

## Overview
`chkconfig` komutu, sistemdeki hizmetlerin (servislerin) başlatılma durumlarını yönetmek için kullanılır. Bu komut, belirli bir hizmetin hangi çalışma seviyelerinde (runlevel) etkinleştirileceğini veya devre dışı bırakılacağını ayarlamak için idealdir.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```csh
chkconfig [options] [arguments]
```

## Common Options
- `--list`: Tüm hizmetlerin mevcut durumunu listeler.
- `--add`: Yeni bir hizmeti sistemin başlatma yönetimine ekler.
- `--del`: Mevcut bir hizmeti sistemin başlatma yönetiminden kaldırır.
- `--level`: Belirli bir çalışma seviyesinde hizmetin durumunu ayarlamak için kullanılır.

## Common Examples
Aşağıda `chkconfig` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### Tüm Hizmetlerin Durumunu Listeleme
```csh
chkconfig --list
```

### Yeni Bir Hizmeti Eklemek
```csh
chkconfig --add myservice
```

### Bir Hizmeti Kaldırmak
```csh
chkconfig --del myservice
```

### Belirli Bir Çalışma Seviyesinde Hizmeti Etkinleştirmek
```csh
chkconfig --level 345 myservice on
```

### Belirli Bir Çalışma Seviyesinde Hizmeti Devre Dışı Bırakmak
```csh
chkconfig --level 012 myservice off
```

## Tips
- Hizmetlerin durumunu kontrol etmek için `chkconfig --list` komutunu düzenli olarak kullanın.
- Yeni bir hizmet eklerken, hizmetin başlangıç dosyasının doğru bir şekilde yapılandırıldığından emin olun.
- Çalışma seviyelerini anlamak, hangi hizmetlerin hangi durumlarda başlatılacağını yönetmek için önemlidir.