# [Linux] C Shell (csh) tcpdump Kullanımı: Ağ trafiğini analiz etme aracı

## Genel Bakış
tcpdump, ağ trafiğini izlemek ve analiz etmek için kullanılan bir komut satırı aracıdır. Ağ üzerinde geçen paketleri yakalayarak, bu paketlerin içeriğini görüntülemenizi sağlar. Bu, ağ sorunlarını teşhis etmek veya güvenlik denetimleri yapmak için oldukça yararlıdır.

## Kullanım
tcpdump komutunun temel sözdizimi aşağıdaki gibidir:

```bash
tcpdump [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-i <arayüz>`: Hangi ağ arayüzünün izleneceğini belirtir.
- `-n`: IP adreslerini ve port numaralarını sayısal olarak gösterir, isim çözümlemesi yapmaz.
- `-c <sayı>`: Belirtilen sayıda paketi yakaladıktan sonra tcpdump'ı durdurur.
- `-w <dosya>`: Yakalanan paketleri belirtilen dosyaya kaydeder.
- `-r <dosya>`: Daha önce kaydedilmiş bir dosyadan paketleri okur.

## Yaygın Örnekler
Aşağıda tcpdump komutunun bazı pratik örnekleri bulunmaktadır:

1. Tüm ağ trafiğini izlemek için:
   ```bash
   tcpdump -i eth0
   ```

2. Sadece HTTP trafiğini yakalamak için:
   ```bash
   tcpdump -i eth0 port 80
   ```

3. İlk 10 paketi yakalayıp durdurmak için:
   ```bash
   tcpdump -i eth0 -c 10
   ```

4. Yakalanan verileri bir dosyaya kaydetmek için:
   ```bash
   tcpdump -i eth0 -w yakalanan_paketler.pcap
   ```

5. Kaydedilmiş bir dosyadan paketleri okumak için:
   ```bash
   tcpdump -r yakalanan_paketler.pcap
   ```

## İpuçları
- tcpdump kullanırken, ağ trafiğini izlemek için yeterli izinlere sahip olduğunuzdan emin olun; genellikle root yetkileri gereklidir.
- Ağ trafiğini izlerken, yalnızca gerekli bilgileri yakalamaya odaklanın; bu, daha az gürültü ve daha anlamlı sonuçlar elde etmenizi sağlar.
- Yakalanan verilerin boyutunu kontrol edin; çok fazla veri toplamak, analiz yapmayı zorlaştırabilir.