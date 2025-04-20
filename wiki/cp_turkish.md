# [Linux] C Shell (csh) cp Kullanımı: Dosya kopyalama komutu

## Genel Bakış
`cp` komutu, dosyaları ve dizinleri bir yerden başka bir yere kopyalamak için kullanılır. Bu komut, kullanıcıların dosyalarını yedeklemek veya başka bir konuma taşımak için oldukça faydalıdır.

## Kullanım
Temel sözdizimi şu şekildedir:
```csh
cp [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-r`: Dizinleri ve içindeki tüm dosyaları kopyalamak için kullanılır.
- `-i`: Hedef dosya mevcutsa, üzerine yazmadan önce kullanıcıdan onay ister.
- `-u`: Yalnızca kaynak dosya, hedef dosyadan daha yeni ise kopyalama işlemi yapar.
- `-v`: Kopyalama işlemi sırasında hangi dosyaların kopyalandığını gösterir.

## Yaygın Örnekler
Aşağıda `cp` komutunun bazı pratik kullanım örnekleri verilmiştir:

1. Bir dosyayı başka bir konuma kopyalamak:
   ```csh
   cp dosya.txt /hedef/konum/
   ```

2. Bir dizini ve içindeki tüm dosyaları kopyalamak:
   ```csh
   cp -r dizin/ /hedef/dizin/
   ```

3. Mevcut dosya üzerine yazmadan önce onay almak:
   ```csh
   cp -i dosya.txt /hedef/konum/
   ```

4. Yalnızca daha yeni dosyaları kopyalamak:
   ```csh
   cp -u dosya.txt /hedef/konum/
   ```

5. Kopyalama işlemi sırasında hangi dosyaların kopyalandığını görmek:
   ```csh
   cp -v dosya.txt /hedef/konum/
   ```

## İpuçları
- Kopyalama işlemi yapmadan önce hedef dizinin var olduğundan emin olun.
- `-i` seçeneğini kullanarak yanlışlıkla üzerine yazma riskini azaltabilirsiniz.
- Büyük dosyalarla çalışırken, kopyalama işleminin tamamlanmasını bekleyin ve dosya bütünlüğünü kontrol edin.