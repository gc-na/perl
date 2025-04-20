# [Linux] C Shell (csh) comm kullanımı: İki dosya arasındaki farklılıkları karşılaştırma

## Genel Bakış
`comm` komutu, iki sıralı dosya arasındaki satırları karşılaştırarak ortak ve farklı satırları gösterir. Bu komut, özellikle metin dosyaları arasındaki farklılıkları analiz etmek için kullanışlıdır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
comm [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-1`: İlk dosyada bulunan ancak ikinci dosyada bulunmayan satırları göstermez.
- `-2`: İkinci dosyada bulunan ancak ilk dosyada bulunmayan satırları göstermez.
- `-3`: Her iki dosyada da bulunan satırları göstermez.
- `-i`: Büyük/küçük harf duyarsız karşılaştırma yapar.

## Yaygın Örnekler
Aşağıda `comm` komutunun bazı pratik örnekleri verilmiştir:

### Örnek 1: İki dosya arasındaki farkları gösterme
```bash
comm dosya1.txt dosya2.txt
```

### Örnek 2: Sadece birinci dosyadaki satırları gösterme
```bash
comm -13 dosya1.txt dosya2.txt
```

### Örnek 3: Sadece ikinci dosyadaki satırları gösterme
```bash
comm -12 dosya1.txt dosya2.txt
```

### Örnek 4: Büyük/küçük harf duyarsız karşılaştırma
```bash
comm -i dosya1.txt dosya2.txt
```

## İpuçları
- Dosyaların sıralı olduğundan emin olun; aksi takdirde `comm` beklenmeyen sonuçlar verebilir.
- `sort` komutunu kullanarak dosyaları sıralayabilirsiniz:
  ```bash
  sort dosya1.txt > sıralı_dosya1.txt
  sort dosya2.txt > sıralı_dosya2.txt
  comm sıralı_dosya1.txt sıralı_dosya2.txt
  ```
- Çıktıyı bir dosyaya yönlendirmek için `>` operatörünü kullanabilirsiniz:
  ```bash
  comm dosya1.txt dosya2.txt > farklar.txt
  ```