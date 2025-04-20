# [Linux] C Shell (csh) dstat Kullanımı: Sistem kaynaklarını izleme aracı

## Genel Bakış
dstat komutu, sistem kaynaklarının kullanımını gerçek zamanlı olarak izlemek için kullanılan bir araçtır. CPU, bellek, disk ve ağ gibi sistem bileşenlerinin performansını takip etmenizi sağlar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
dstat [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-c`: CPU kullanımını gösterir.
- `-d`: Disk I/O istatistiklerini gösterir.
- `-n`: Ağ trafiğini gösterir.
- `-m`: Bellek kullanımını gösterir.
- `-t`: Zaman damgası ekler.

## Yaygın Örnekler
Aşağıda dstat komutunun bazı pratik örnekleri verilmiştir:

1. Sadece CPU kullanımını gösterme:
   ```bash
   dstat -c
   ```

2. Disk I/O ve ağ trafiğini izleme:
   ```bash
   dstat -d -n
   ```

3. Tüm sistem kaynaklarını izleme:
   ```bash
   dstat
   ```

4. Zaman damgası ile birlikte bellek ve CPU kullanımını gösterme:
   ```bash
   dstat -c -m -t
   ```

## İpuçları
- dstat komutunu çalıştırmadan önce sistemde yüklü olduğundan emin olun.
- Uzun süreli izleme için çıktı dosyasına yönlendirme yapabilirsiniz:
  ```bash
  dstat > dstat_output.txt
  ```
- Belirli bir süre boyunca izlemek için `--time` seçeneğini kullanabilirsiniz:
  ```bash
  dstat --time 10
  ``` 

Bu bilgilerle dstat komutunu etkili bir şekilde kullanarak sistem kaynaklarınızı izleyebilirsiniz.