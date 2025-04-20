# [Linux] C Shell (csh) export Kullanımı: Ortam Değişkenlerini Ayarlama

## Genel Bakış
`export` komutu, C Shell (csh) ortamında değişkenleri tanımlamak ve bu değişkenlerin alt süreçlerde kullanılabilmesini sağlamak için kullanılır. Bu sayede, belirli bir değişkenin değerini tüm alt süreçlere aktarabilirsiniz.

## Kullanım
`export` komutunun temel sözdizimi aşağıdaki gibidir:

```
export [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-n`: Değişkenin dışa aktarımını iptal eder.
- `-p`: Dışa aktarılan tüm değişkenleri listelemek için kullanılır.

## Yaygın Örnekler

1. Bir değişkeni dışa aktarma:
   ```csh
   set MY_VAR="Merhaba Dünya"
   export MY_VAR
   ```

2. Dışa aktarılan değişkeni kontrol etme:
   ```csh
   echo $MY_VAR
   ```

3. Dışa aktarılan değişkenleri listeleme:
   ```csh
   export -p
   ```

4. Dışa aktarılan bir değişkenin dışa aktarımını iptal etme:
   ```csh
   export -n MY_VAR
   ```

## İpuçları
- Değişkenlerinizi dışa aktarmadan önce doğru şekilde tanımladığınızdan emin olun.
- Dışa aktarılan değişkenlerinizi kontrol etmek için `export -p` komutunu kullanarak mevcut durumu gözden geçirin.
- Ortam değişkenlerini kullanarak uygulamalarınız arasında veri paylaşımını kolaylaştırabilirsiniz.