# [Linux] C Shell (csh) watch Kullanımı: Komutların sürekli izlenmesi

## Overview
`watch` komutu, belirli bir komutu belirli aralıklarla çalıştırarak çıktısını sürekli olarak izlemeye yarar. Bu, sistem durumunu veya belirli bir işlemi takip etmek için oldukça kullanışlıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```csh
watch [options] [arguments]
```

## Common Options
- `-n <saniye>`: Komutun her ne kadar saniyede bir çalıştırılacağını belirler. Varsayılan değer 2 saniyedir.
- `-d`: Çıktıdaki değişiklikleri vurgular, böylece hangi kısımların değiştiğini kolayca görebilirsiniz.
- `-t`: Başlık bilgisini gizler, böylece yalnızca komutun çıktısı gösterilir.

## Common Examples
Aşağıda `watch` komutunun bazı pratik örnekleri bulunmaktadır:

### Örnek 1: Sistem Durumunu İzleme
Sistem kaynaklarını izlemek için `top` komutunu kullanabilirsiniz:

```csh
watch -n 5 top -b -n 1
```
Bu komut, her 5 saniyede bir `top` çıktısını gösterir.

### Örnek 2: Disk Kullanımını Kontrol Etme
Disk kullanımını izlemek için `df` komutunu kullanabilirsiniz:

```csh
watch -d df -h
```
Bu komut, disk kullanımını her 2 saniyede bir güncelleyerek değişiklikleri vurgular.

### Örnek 3: Belirli Bir Dosyanın İçeriğini İzleme
Bir dosyanın içeriğini sürekli olarak kontrol etmek için `cat` komutunu kullanabilirsiniz:

```csh
watch -n 1 cat /path/to/file.txt
```
Bu komut, belirtilen dosyanın içeriğini her saniyede bir günceller.

## Tips
- `watch` komutunu kullanırken, izlemek istediğiniz komutun çıktısının çok fazla veri üretmediğinden emin olun, aksi takdirde ekranınız karmaşık hale gelebilir.
- `-d` seçeneğini kullanarak değişiklikleri vurgulamak, özellikle çıktıda önemli değişiklikleri hızlıca görmek için faydalıdır.
- İzlemek istediğiniz komutun süresini ayarlamak için `-n` seçeneğini kullanarak daha uygun bir zaman aralığı belirleyebilirsiniz.