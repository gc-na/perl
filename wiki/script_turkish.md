# [Linux] C Shell (csh) script Kullanımı: Komut çıktısını kaydetme

## Overview
`script` komutu, terminal oturumunuzun çıktısını bir dosyaya kaydetmek için kullanılır. Bu, özellikle komutların çıktısını belgelemek veya daha sonra incelemek için faydalıdır.

## Usage
Temel sözdizimi şu şekildedir:

```csh
script [options] [arguments]
```

## Common Options
- `-a`: Var olan bir dosyaya ekleme yapar, dosyayı silmez.
- `-f`: Çıktıyı anlık olarak gösterir, yani çıktıyı hemen dosyaya yazar.
- `-q`: Komutun başlangıcında bilgi mesajı göstermez.

## Common Examples
Aşağıda `script` komutunun bazı pratik örnekleri verilmiştir:

1. Basit bir oturum kaydetme:
   ```csh
   script oturum.txt
   ```
   Bu komut, terminal oturumunu `oturum.txt` dosyasına kaydeder.

2. Var olan bir dosyaya ekleme yapma:
   ```csh
   script -a oturum.txt
   ```
   Bu komut, mevcut `oturum.txt` dosyasına yeni çıktılar ekler.

3. Çıktıyı anlık olarak gösterme:
   ```csh
   script -f oturum.txt
   ```
   Bu komut, çıktıyı hemen `oturum.txt` dosyasına yazar ve terminalde de gösterir.

4. Bilgi mesajı olmadan oturum kaydetme:
   ```csh
   script -q oturum.txt
   ```
   Bu komut, bilgi mesajı göstermeden oturumu `oturum.txt` dosyasına kaydeder.

## Tips
- `script` komutunu kullanırken, kaydedilen dosyanın adını anlamlı bir şekilde seçmek, daha sonra bulmanızı kolaylaştırır.
- Uzun bir oturum kaydediyorsanız, dosya boyutunu kontrol edin; gerektiğinde dosyayı bölmek iyi bir fikir olabilir.
- Kayıt sırasında terminalde yaptığınız her şey kaydedileceği için, gizli bilgileri girmemeye dikkat edin.