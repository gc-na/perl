# [Linux] C Shell (csh) yes Kullanımı: Sürekli bir metin çıktısı üretir

## Genel Bakış
`yes` komutu, belirli bir metni sürekli olarak çıktılar. Genellikle, bir komutun veya işlemin sürekli olarak belirli bir girdiye ihtiyaç duyduğu durumlarda kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```csh
yes [options] [arguments]
```

## Yaygın Seçenekler
- `-n`: Herhangi bir metin üretmeden sadece "evet" kelimesini üretir.
- `-h`: Yardım mesajını gösterir.

## Yaygın Örnekler
Aşağıda `yes` komutunun bazı pratik örnekleri bulunmaktadır:

1. **Sürekli "evet" yazdırma:**
   ```csh
   yes
   ```

2. **Belirli bir metni sürekli yazdırma:**
   ```csh
   yes "Bu bir test mesajıdır."
   ```

3. **Bir komut ile birlikte kullanma:**
   ```csh
   yes | rm -i dosya.txt
   ```
   Bu komut, `rm` komutuna sürekli "evet" yanıtı vererek dosyanın silinmesini onaylar.

## İpuçları
- `yes` komutunu, etkileşimli komutları otomatikleştirmek için kullanabilirsiniz.
- Çok fazla çıktı üretebileceğinden, çıktıyı bir dosyaya yönlendirmek iyi bir fikir olabilir:
  ```csh
  yes "Onay" > onaylar.txt
  ```
- `yes` komutunu dikkatli kullanın; yanlışlıkla önemli dosyaları silebilir veya istenmeyen sonuçlara yol açabilir.