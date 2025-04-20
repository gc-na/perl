# [Linux] C Shell (csh) iconv Kullanımı: Karakter kodlamalarını dönüştürme aracı

## Genel Bakış
`iconv`, farklı karakter kodlamaları arasında dönüşüm yapmaya yarayan bir komuttur. Özellikle metin dosyalarının farklı platformlarda veya sistemlerde uyumlu hale getirilmesi için kullanılır.

## Kullanım
Temel sözdizimi şu şekildedir:
```csh
iconv [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-f, --from-code=KOD`: Dönüştürülecek dosyanın mevcut karakter kodlamasını belirtir.
- `-t, --to-code=KOD`: Dönüştürülen dosyanın hedef karakter kodlamasını belirtir.
- `-o, --output=DOSYA`: Dönüştürülmüş çıktının kaydedileceği dosya adını belirtir.
- `-l, --list`: Desteklenen tüm karakter kodlamalarının listesini gösterir.

## Yaygın Örnekler
1. UTF-8'den ISO-8859-1'e dönüştürme:
   ```csh
   iconv -f UTF-8 -t ISO-8859-1 input.txt -o output.txt
   ```

2. UTF-16'dan UTF-8'e dönüştürme:
   ```csh
   iconv -f UTF-16 -t UTF-8 input.txt -o output.txt
   ```

3. Desteklenen karakter kodlamalarının listesini görüntüleme:
   ```csh
   iconv -l
   ```

4. Hedef dosya belirtmeden standart çıktıya yazdırma:
   ```csh
   iconv -f UTF-8 -t ASCII input.txt
   ```

## İpuçları
- Dönüştürme işlemi sırasında hata alıyorsanız, kaynak ve hedef kodlamalarının doğru olduğundan emin olun.
- Büyük dosyalarla çalışırken, dönüşüm işleminin tamamlanmasını bekleyin; aksi takdirde dosya bozulabilir.
- `iconv` komutunu sıkça kullanıyorsanız, sık kullandığınız kodlamaları not alarak zaman kazanabilirsiniz.