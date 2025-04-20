# [Linux] C Shell (csh) find Kullanımı: Dosya adlarını bulma

## Genel Bakış
`find` komutu, belirli bir dizin içinde dosya ve dizinleri aramak için kullanılır. Kullanıcıların belirli kriterlere göre dosyaları bulmasını sağlar, bu da dosya yönetimini kolaylaştırır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```csh
find [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-name`: Belirtilen isimle eşleşen dosyaları bulur.
- `-type`: Belirli bir dosya türünü (örneğin, dosya veya dizin) arar.
- `-size`: Belirtilen boyutta dosyaları bulur.
- `-mtime`: Belirtilen gün sayısı içinde değiştirilmiş dosyaları bulur.
- `-exec`: Bulunan dosyalar üzerinde belirtilen komutu çalıştırır.

## Yaygın Örnekler
Aşağıda `find` komutunun bazı pratik örnekleri bulunmaktadır:

1. Belirli bir isimle dosyaları bulma:
   ```csh
   find /home/kullanici -name "belge.txt"
   ```

2. Sadece dizinleri bulma:
   ```csh
   find /home/kullanici -type d
   ```

3. 1 MB'den büyük dosyaları bulma:
   ```csh
   find /home/kullanici -size +1M
   ```

4. Son 7 gün içinde değiştirilmiş dosyaları bulma:
   ```csh
   find /home/kullanici -mtime -7
   ```

5. Bulunan dosyalar üzerinde bir komut çalıştırma:
   ```csh
   find /home/kullanici -name "*.log" -exec rm {} \;
   ```

## İpuçları
- `find` komutunu kullanırken, arama dizinini daraltmak için kesin yollar kullanmak, arama süresini kısaltabilir.
- `-print` seçeneği varsayılan olarak etkindir, ancak çıktıyı özelleştirmek için kullanılabilir.
- `-delete` seçeneği ile dosyaları bulduktan sonra doğrudan silebilirsiniz, ancak dikkatli olun; bu işlem geri alınamaz.