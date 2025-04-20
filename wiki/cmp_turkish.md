# [Linux] C Shell (csh) cmp Kullanımı: İki dosyayı karşılaştırma

## Overview
`cmp` komutu, iki dosyanın içeriklerini karşılaştırmak için kullanılır. Bu komut, dosyalar arasındaki farklılıkları belirlemek ve hangi dosyanın daha önce veya sonra değiştirildiğini görmek için oldukça faydalıdır.

## Usage
Temel sözdizimi şu şekildedir:

```csh
cmp [options] [arguments]
```

## Common Options
- `-l`: Farklılıkları byte olarak gösterir.
- `-s`: Hiçbir çıktı üretmeden sadece dosyaların eşit olup olmadığını kontrol eder.
- `-i`: Belirtilen bayttan itibaren karşılaştırma yapar.

## Common Examples
Aşağıda `cmp` komutunun yaygın kullanım örnekleri bulunmaktadır:

1. İki dosyanın karşılaştırılması:
   ```csh
   cmp dosya1.txt dosya2.txt
   ```

2. Farklılıkları byte olarak gösterme:
   ```csh
   cmp -l dosya1.txt dosya2.txt
   ```

3. Dosyaların eşit olup olmadığını kontrol etme (sessiz mod):
   ```csh
   cmp -s dosya1.txt dosya2.txt
   ```

4. Belirli bir bayttan itibaren karşılaştırma yapma:
   ```csh
   cmp -i 10 dosya1.txt dosya2.txt
   ```

## Tips
- `cmp` komutunu kullanmadan önce dosyaların var olduğundan emin olun.
- Büyük dosyalarla çalışıyorsanız, `-s` seçeneğini kullanarak sadece eşitlik kontrolü yapabilirsiniz; bu, zaman kazandırır.
- Farklılıkları daha iyi analiz etmek için `-l` seçeneğini kullanarak hangi byte'ların farklı olduğunu görebilirsiniz.