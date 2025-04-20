# [Linux] C Shell (csh) pidstat Kullanımı: Süreç istatistiklerini görüntüleme

## Genel Bakış
`pidstat` komutu, sistemdeki süreçlerin performans istatistiklerini görüntülemek için kullanılır. Bu komut, belirli bir süre boyunca süreçlerin CPU, bellek ve diğer kaynak kullanımlarını izlemeye olanak tanır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
pidstat [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-h`: Başlık satırını gösterir.
- `-r`: Bellek kullanımını gösterir.
- `-u`: CPU kullanımını gösterir.
- `-p`: Belirli bir süreç kimliğine (PID) göre istatistikleri görüntüler.
- `-t`: Tüm süreçlerin toplam istatistiklerini gösterir.

## Yaygın Örnekler
Aşağıda `pidstat` komutunun bazı pratik örnekleri bulunmaktadır:

### Örnek 1: Tüm süreçlerin CPU kullanımını görüntüleme
```
pidstat -u 1
```
Bu komut, her saniyede bir tüm süreçlerin CPU kullanımını gösterir.

### Örnek 2: Belirli bir PID için bellek kullanımını izleme
```
pidstat -r -p 1234 1
```
Bu komut, PID'si 1234 olan sürecin bellek kullanımını her saniyede bir gösterir.

### Örnek 3: Tüm süreçlerin istatistiklerini görüntüleme
```
pidstat -t 1
```
Bu komut, her saniyede bir tüm süreçlerin toplam istatistiklerini gösterir.

## İpuçları
- `pidstat` komutunu kullanırken, belirli bir süre aralığı belirlemek için `-r` veya `-u` seçeneklerini kullanarak daha spesifik veriler elde edebilirsiniz.
- Uzun süreli izleme yapmak istiyorsanız, çıktıyı bir dosyaya yönlendirmek için `>` operatörünü kullanabilirsiniz.
- Süreçlerin performansını analiz ederken, `pidstat` ile birlikte diğer sistem izleme araçlarını kullanarak daha kapsamlı bir analiz yapabilirsiniz.