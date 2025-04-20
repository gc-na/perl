# [Linux] C Shell (csh) head Kullanımı: Dosya içeriğinin başlangıcını görüntüleme

## Genel Bakış
`head` komutu, bir dosyanın veya bir komutun çıktısının en üst kısmındaki belirli sayıda satırı görüntülemek için kullanılır. Genellikle dosyanın içeriğini hızlıca gözden geçirmek için faydalıdır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```csh
head [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-n [sayı]`: Görüntülenecek satır sayısını belirtir. Varsayılan olarak ilk 10 satırı gösterir.
- `-q`: Çıktıda dosya adlarını göstermez.
- `-v`: Çıktıda dosya adlarını gösterir.

## Yaygın Örnekler
Aşağıda `head` komutunun bazı pratik örnekleri bulunmaktadır:

1. **Varsayılan olarak ilk 10 satırı görüntüleme:**
   ```csh
   head dosya.txt
   ```

2. **İlk 5 satırı görüntüleme:**
   ```csh
   head -n 5 dosya.txt
   ```

3. **Birden fazla dosyanın ilk 10 satırını görüntüleme:**
   ```csh
   head dosya1.txt dosya2.txt
   ```

4. **Çıktıda dosya adlarını göstermek:**
   ```csh
   head -v dosya.txt
   ```

5. **Bir komutun çıktısının ilk 10 satırını görüntüleme:**
   ```csh
   ls -l | head
   ```

## İpuçları
- `head` komutunu kullanarak dosyaların içeriğini hızlıca gözden geçirebilir ve dosya boyutunu kontrol edebilirsiniz.
- Uzun dosyalarla çalışırken, `-n` seçeneği ile istediğiniz satır sayısını belirlemek, gereksiz bilgileri atlamanıza yardımcı olur.
- `head` komutunu diğer komutlarla birleştirerek, daha karmaşık veri işleme görevlerini kolaylaştırabilirsiniz.