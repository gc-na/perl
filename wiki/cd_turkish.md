# [Linux] C Shell (csh) cd Kullanımı: Dizinler arasında geçiş yapma

## Genel Bakış
`cd` komutu, kullanıcıların dosya sisteminde dizinler arasında geçiş yapmasını sağlar. Bu komut, terminalde çalışırken hangi dizinde olduğunuzu değiştirmenize olanak tanır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
cd [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `..` : Bir üst dizine geçiş yapar.
- `-` : Önceki dizine geri döner.
- `~` : Kullanıcının ana dizinine geçiş yapar.

## Yaygın Örnekler
- Ana dizine geçiş yapmak için:
  ```csh
  cd ~
  ```
  
- Bir üst dizine geçiş yapmak için:
  ```csh
  cd ..
  ```

- Belirli bir dizine geçiş yapmak için:
  ```csh
  cd /path/to/directory
  ```

- Önceki dizine geri dönmek için:
  ```csh
  cd -
  ```

## İpuçları
- `cd` komutunu kullanmadan önce mevcut dizininizi kontrol etmek için `pwd` komutunu kullanabilirsiniz.
- Hedef dizinin tam yolunu kullanmak, yanlışlıkla başka bir dizine geçiş yapmanızı engelleyebilir.
- Dizin adlarında boşluk varsa, dizin adını tırnak içinde yazmayı unutmayın. Örneğin:
  ```csh
  cd "My Documents"
  ```