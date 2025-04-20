# [Linux] C Shell (csh) diff Kullanımı: Dosyalar arasındaki farkları karşılaştırma

## Genel Bakış
`diff` komutu, iki dosya arasındaki farklılıkları karşılaştırmak için kullanılır. Bu komut, dosyaların içeriğindeki değişiklikleri göstererek, kullanıcıların dosyalar arasındaki değişiklikleri anlamalarına yardımcı olur.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```csh
diff [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-u`: Birleştirilmiş formatta çıktı verir.
- `-i`: Büyük/küçük harf duyarsız karşılaştırma yapar.
- `-w`: Boşlukları dikkate almaz.
- `-b`: Boşluk değişikliklerini göz ardı eder.

## Yaygın Örnekler
Aşağıda `diff` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. İki dosya arasındaki farkları görmek için:
   ```csh
   diff dosya1.txt dosya2.txt
   ```

2. Birleştirilmiş formatta farkları görüntülemek için:
   ```csh
   diff -u dosya1.txt dosya2.txt
   ```

3. Büyük/küçük harf duyarsız karşılaştırma yapmak için:
   ```csh
   diff -i dosya1.txt dosya2.txt
   ```

4. Boşlukları göz ardı ederek karşılaştırma yapmak için:
   ```csh
   diff -w dosya1.txt dosya2.txt
   ```

## İpuçları
- `diff` çıktısını daha okunabilir hale getirmek için `-u` seçeneğini kullanmayı deneyin.
- Farkları bir dosyaya kaydetmek için çıktı yönlendirmesini kullanabilirsiniz:
  ```csh
  diff dosya1.txt dosya2.txt > farklar.txt
  ```
- `diff` komutunu sık kullandığınız dosyalar için bir alias oluşturmayı düşünebilirsiniz, bu sayede daha hızlı erişim sağlayabilirsiniz.