# [Linux] C Shell (csh) traceroute6 Kullanımı: IPv6 ağ yollarını izleme

## Genel Bakış
traceroute6 komutu, bir IPv6 ağı üzerindeki bir hedefe giden yol boyunca geçen yönlendiricileri ve ağ cihazlarını izlemek için kullanılır. Bu komut, ağ bağlantı sorunlarını teşhis etmek ve ağın performansını değerlendirmek için oldukça faydalıdır.

## Kullanım
Komutun temel sözdizimi aşağıdaki gibidir:

```csh
traceroute6 [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-m <sayı>`: İzlenecek maksimum atlama sayısını belirler.
- `-p <port>`: Hedefe gönderilecek UDP paketlerinin port numarasını ayarlar.
- `-w <saniye>`: Her bir atlama için zaman aşımını saniye cinsinden ayarlar.

## Yaygın Örnekler
Aşağıda traceroute6 komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. Belirli bir IPv6 adresine giden yolu izleme:
   ```csh
   traceroute6 2001:db8::1
   ```

2. Maksimum 15 atlama ile bir hedefe izleme:
   ```csh
   traceroute6 -m 15 2001:db8::1
   ```

3. Belirli bir port numarası ile izleme:
   ```csh
   traceroute6 -p 80 2001:db8::1
   ```

4. Zaman aşımını 2 saniye olarak ayarlama:
   ```csh
   traceroute6 -w 2 2001:db8::1
   ```

## İpuçları
- Ağ sorunlarını teşhis ederken, farklı hedefler üzerinde traceroute6 komutunu deneyerek sorunun kaynağını daha iyi anlayabilirsiniz.
- Yüksek atlama sayıları kullanmak, daha fazla yönlendirici ve ağ cihazı hakkında bilgi almanızı sağlar, ancak bu işlem daha uzun sürebilir.
- Hedefin yanıt vermediği durumlarda, zaman aşımını artırarak daha fazla bilgi elde edebilirsiniz.