# [Linux] C Shell (csh) systemctl Kullanımı: Sistem hizmetlerini yönetme aracı

## Genel Bakış
`systemctl`, Linux sistemlerinde hizmetleri ve birim dosyalarını yönetmek için kullanılan bir komuttur. Bu komut, sistemin durumunu kontrol etme, hizmetleri başlatma veya durdurma ve sistem birimlerini yönetme gibi işlevleri yerine getirir.

## Kullanım
Temel sözdizimi şu şekildedir:

```csh
systemctl [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `start`: Belirtilen hizmeti başlatır.
- `stop`: Belirtilen hizmeti durdurur.
- `restart`: Belirtilen hizmeti yeniden başlatır.
- `status`: Belirtilen hizmetin durumunu gösterir.
- `enable`: Hizmeti sistem başlangıcında otomatik olarak başlatmak için etkinleştirir.
- `disable`: Hizmeti sistem başlangıcında otomatik olarak başlatmaktan devre dışı bırakır.

## Yaygın Örnekler
Aşağıda `systemctl` komutunun bazı pratik örnekleri verilmiştir:

- Bir hizmeti başlatmak için:
```csh
systemctl start httpd
```

- Bir hizmeti durdurmak için:
```csh
systemctl stop httpd
```

- Bir hizmetin durumunu kontrol etmek için:
```csh
systemctl status httpd
```

- Bir hizmeti yeniden başlatmak için:
```csh
systemctl restart httpd
```

- Bir hizmeti sistem başlangıcında otomatik olarak başlatmak için:
```csh
systemctl enable httpd
```

- Bir hizmetin otomatik başlatılmasını devre dışı bırakmak için:
```csh
systemctl disable httpd
```

## İpuçları
- Hizmetlerin durumunu düzenli olarak kontrol etmek, sisteminizin sağlığını korumanıza yardımcı olur.
- `systemctl` komutunu kullanmadan önce, gerekli izinlere sahip olduğunuzdan emin olun; genellikle `sudo` ile çalıştırmak gerekebilir.
- Hizmetlerin günlüklerini kontrol etmek için `journalctl` komutunu kullanabilirsiniz; bu, sorun giderme sürecinde faydalı olabilir.