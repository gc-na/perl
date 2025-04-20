# [Linux] C Shell (csh) nslookup Kullanımı: Alan adı sorgulama aracı

## Genel Bakış
nslookup komutu, bir alan adının IP adresini veya bir IP adresinin alan adını sorgulamak için kullanılan bir araçtır. DNS (Domain Name System) sunucuları ile etkileşimde bulunarak, alan adı çözümlemesi yapar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```csh
nslookup [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-type=TYPE`: Sorgulamak istediğiniz kayıt türünü belirtir (örneğin, A, MX, CNAME).
- `-timeout=NUM`: Zaman aşımını saniye cinsinden ayarlar.
- `-port=NUM`: DNS sunucusuna bağlanmak için kullanılacak port numarasını belirtir.

## Yaygın Örnekler
1. Bir alan adının IP adresini sorgulamak:
   ```csh
   nslookup example.com
   ```

2. Belirli bir DNS sunucusunu kullanarak sorgulama yapmak:
   ```csh
   nslookup example.com 8.8.8.8
   ```

3. MX kayıtlarını sorgulamak:
   ```csh
   nslookup -type=MX example.com
   ```

4. Bir IP adresinin alan adını sorgulamak:
   ```csh
   nslookup 93.184.216.34
   ```

## İpuçları
- Sorgulama yapmadan önce doğru DNS sunucusunu seçmek, daha doğru sonuçlar almanıza yardımcı olabilir.
- Sık kullanılan alan adlarını ve IP adreslerini kaydedin, böylece hızlı sorgulama yapabilirsiniz.
- Hatalı sorgulamalarda, DNS sunucusunun çalıştığından emin olun ve doğru alan adını kullandığınızdan emin olun.