# [Linux] C Shell (csh) grep Kullanımı: Metin içinde desen arama

## Genel Bakış
`grep` komutu, bir dosya veya standart girdi içinde belirli bir deseni aramak için kullanılır. Genellikle metin dosyalarında belirli kelimeleri veya ifadeleri bulmak için kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```csh
grep [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-i`: Büyük/küçük harf duyarsız arama yapar.
- `-v`: Belirtilen desene uymayan satırları gösterir.
- `-r`: Alt dizinler dahil olmak üzere dizin içinde arama yapar.
- `-n`: Eşleşen satırların numaralarını gösterir.
- `-l`: Eşleşen dosyaların adlarını listeler.

## Yaygın Örnekler
Aşağıda `grep` komutunun bazı pratik örnekleri bulunmaktadır:

1. Belirli bir kelimeyi bir dosyada arama:
   ```csh
   grep "kelime" dosya.txt
   ```

2. Büyük/küçük harf duyarsız arama:
   ```csh
   grep -i "kelime" dosya.txt
   ```

3. Eşleşmeyen satırları gösterme:
   ```csh
   grep -v "kelime" dosya.txt
   ```

4. Bir dizin içinde alt dizinlerle birlikte arama:
   ```csh
   grep -r "kelime" /path/to/dizin
   ```

5. Eşleşen satırların numaralarını gösterme:
   ```csh
   grep -n "kelime" dosya.txt
   ```

## İpuçları
- Arama yaparken, aradığınız kelimenin tam olarak ne olduğunu bildiğinizden emin olun.
- Büyük/küçük harf duyarsız arama yapmak için `-i` seçeneğini kullanın.
- Çok sayıda dosyada arama yaparken, sonuçları daha iyi anlamak için `-n` veya `-l` seçeneklerini eklemeyi düşünün.