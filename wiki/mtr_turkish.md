# [Linux] C Shell (csh) mtr Kullanımı: Ağ bağlantılarını izleme aracı

## Genel Bakış
mtr (My Traceroute), ağ bağlantılarını izlemek ve analiz etmek için kullanılan bir araçtır. Hem ping hem de traceroute işlevselliğini birleştirerek, hedefe giden yol boyunca her bir ağ cihazının performansını gösterir.

## Kullanım
Temel komut yapısı aşağıdaki gibidir:
```csh
mtr [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-r`: Rapor modunu etkinleştirir; sonuçları bir rapor formatında gösterir.
- `-c [sayı]`: Belirtilen sayıda deneme yapar ve ardından çıkış yapar.
- `-i [saniye]`: Ping aralığını saniye cinsinden ayarlar.
- `-p`: Port numarasını belirtmek için kullanılır.

## Yaygın Örnekler
Aşağıda mtr komutunun bazı pratik örnekleri bulunmaktadır:

1. Basit bir mtr komutu ile bir hedefe bağlantıyı izleme:
   ```csh
   mtr example.com
   ```

2. Rapor modunda belirli bir hedefe bağlantıyı izleme:
   ```csh
   mtr -r example.com
   ```

3. 10 ping denemesi yaparak bir hedefi izleme:
   ```csh
   mtr -c 10 example.com
   ```

4. Ping aralığını 2 saniye olarak ayarlayarak bir hedefi izleme:
   ```csh
   mtr -i 2 example.com
   ```

## İpuçları
- Ağ sorunlarını teşhis etmek için mtr komutunu kullanarak, hangi ağ cihazının sorun çıkardığını hızlıca belirleyebilirsiniz.
- Uzun süreli izleme yapmak istiyorsanız, `-c` seçeneği ile belirli bir deneme sayısı belirleyin.
- Rapor modunu kullanarak, sonuçları daha okunabilir bir formatta elde edebilirsiniz.