# [Linux] C Shell (csh) netstat Kullanımı: Ağ bağlantılarını görüntüleme

## Genel Bakış
netstat komutu, ağ bağlantılarını, yönlendirme tablolarını ve ağ arayüzü istatistiklerini görüntülemek için kullanılan bir araçtır. Bu komut, sistemdeki aktif bağlantıları ve bu bağlantılara ilişkin bilgileri sağlar.

## Kullanım
netstat komutunun temel sözdizimi aşağıdaki gibidir:

```csh
netstat [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-a`: Tüm bağlantıları ve dinleme portlarını gösterir.
- `-n`: Adresleri ve port numaralarını sayısal olarak gösterir.
- `-r`: Yönlendirme tablosunu görüntüler.
- `-i`: Ağ arayüzlerinin istatistiklerini gösterir.
- `-p`: Bağlantıların hangi süreçler tarafından kullanıldığını gösterir.

## Yaygın Örnekler
Aşağıda netstat komutunun bazı pratik örnekleri verilmiştir:

1. Tüm aktif bağlantıları ve dinleme portlarını görüntüleme:
   ```csh
   netstat -a
   ```

2. Bağlantıları sayısal formatta gösterme:
   ```csh
   netstat -n
   ```

3. Yönlendirme tablosunu görüntüleme:
   ```csh
   netstat -r
   ```

4. Ağ arayüzü istatistiklerini görüntüleme:
   ```csh
   netstat -i
   ```

5. Belirli bir bağlantının hangi süreç tarafından kullanıldığını gösterme:
   ```csh
   netstat -p
   ```

## İpuçları
- netstat komutunu kullanırken, belirli bir seçeneği ekleyerek daha fazla bilgi alabilirsiniz. Örneğin, `-n` seçeneği ile IP adreslerini ve port numaralarını sayısal olarak görebilirsiniz.
- Ağ sorunlarını teşhis etmek için netstat çıktısını dikkatlice inceleyin. Dinleyen portlar ve aktif bağlantılar, sorunların kaynağını bulmanıza yardımcı olabilir.
- netstat komutunu sık sık kullanıyorsanız, sık kullandığınız seçenekleri bir alias olarak tanımlayarak kullanımınızı kolaylaştırabilirsiniz.