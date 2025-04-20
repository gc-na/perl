# [Linux] C Shell (csh) xargs Kullanımı: Komut satırı argümanlarını işlemek için

## Genel Bakış
`xargs` komutu, standart girişten okunan verileri alarak bunları bir komutun argümanları olarak kullanmak için kullanılır. Bu, özellikle çok sayıda dosya veya veri ile çalışırken faydalıdır.

## Kullanım
Temel sözdizimi şu şekildedir:
```csh
xargs [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-n [N]`: Her seferinde N argüman ile komutu çalıştırır.
- `-d [AYIRICI]`: Giriş verilerini belirtilen ayırıcı ile ayırır.
- `-p`: Her komut çalıştırılmadan önce kullanıcıdan onay ister.
- `-0`: Null karakter ile ayrılmış girişleri işler (genellikle `find -print0` ile birlikte kullanılır).

## Yaygın Örnekler
1. Bir dizindeki tüm `.txt` dosyalarını silmek için:
    ```csh
    find . -name "*.txt" | xargs rm
    ```

2. Bir dizindeki tüm dosyaların boyutunu listelemek için:
    ```csh
    ls | xargs du -h
    ```

3. Her bir dosya için `wc -l` komutunu çalıştırarak satır sayısını bulmak için:
    ```csh
    find . -type f | xargs wc -l
    ```

4. Belirli bir ayırıcı ile dosya isimlerini işlemek için:
    ```csh
    echo "file1,file2,file3" | xargs -d ',' echo
    ```

## İpuçları
- `xargs` kullanırken, çok sayıda dosya ile çalışıyorsanız, `-n` seçeneğini kullanarak her seferinde belirli sayıda argüman ile komutu çalıştırmayı düşünebilirsiniz.
- Uzun dosya isimleri veya özel karakterler içeren dosyalarla çalışırken `-0` seçeneğini kullanarak güvenli bir şekilde işlem yapabilirsiniz.
- Komutların doğru çalıştığından emin olmak için `-p` seçeneği ile onay almayı tercih edebilirsiniz.