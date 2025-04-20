# [Linux] C Shell (csh) mv Kullanımı: Dosya ve dizin taşımak veya yeniden adlandırmak

## Genel Bakış
`mv` komutu, dosyaları veya dizinleri taşımak veya yeniden adlandırmak için kullanılır. Bu komut, belirli bir dosyanın veya dizinin yerini değiştirmek ya da ismini güncellemek için oldukça faydalıdır.

## Kullanım
Temel sözdizimi şu şekildedir:

```csh
mv [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-i`: Hedef dosya mevcutsa, üzerine yazmadan önce onay ister.
- `-u`: Sadece kaynak dosya, hedef dosyadan daha yeni ise taşır.
- `-v`: Taşıma işlemi sırasında hangi dosyaların taşındığını gösterir.

## Yaygın Örnekler
Aşağıda `mv` komutunun bazı pratik kullanımları verilmiştir:

1. **Bir dosyayı yeniden adlandırma:**
   ```csh
   mv eski_dosya.txt yeni_dosya.txt
   ```

2. **Bir dosyayı başka bir dizine taşıma:**
   ```csh
   mv dosya.txt /hedef/dizin/
   ```

3. **Bir dizini yeniden adlandırma:**
   ```csh
   mv eski_dizin yeni_dizin
   ```

4. **Birden fazla dosyayı bir dizine taşıma:**
   ```csh
   mv dosya1.txt dosya2.txt /hedef/dizin/
   ```

## İpuçları
- Dosyaları taşımadan önce, hedef dizinin var olduğundan emin olun.
- `-i` seçeneğini kullanarak yanlışlıkla üzerine yazma işlemlerinden kaçının.
- Taşıma işlemi sırasında `-v` seçeneği ile hangi dosyaların taşındığını takip edebilirsiniz.