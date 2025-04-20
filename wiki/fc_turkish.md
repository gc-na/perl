# [Linux] C Shell (csh) fc Kullanımı: Komut geçmişini düzenleme

## Overview
`fc` komutu, C Shell (csh) ortamında komut geçmişini düzenlemek ve çalıştırmak için kullanılır. Bu komut, kullanıcıların geçmişteki komutları kolayca bulup düzenlemesine ve yeniden çalıştırmasına olanak tanır.

## Usage
Temel sözdizimi şu şekildedir:
```csh
fc [options] [arguments]
```

## Common Options
- `-l`: Geçmişteki komutları listelemek için kullanılır.
- `-r`: Komutları ters sırada listelemek için kullanılır.
- `-n`: Komut numaralarını göstermeden listelemek için kullanılır.
- `-e`: Belirtilen bir editörü kullanarak komutları düzenlemek için kullanılır.

## Common Examples
Aşağıda `fc` komutunun bazı pratik örnekleri bulunmaktadır:

1. Son 5 komutu listeleme:
   ```csh
   fc -l -5
   ```

2. Geçmişteki tüm komutları listeleme:
   ```csh
   fc -l
   ```

3. Son komutu düzenleme (varsayılan editör ile):
   ```csh
   fc
   ```

4. Belirli bir komutu düzenleme (örneğin, 10 numaralı komut):
   ```csh
   fc 10
   ```

5. Komutları ters sırada listeleme:
   ```csh
   fc -r -l
   ```

## Tips
- `fc` komutunu kullanmadan önce, hangi komutları düzenlemek istediğinizi belirlemek için `fc -l` komutunu kullanarak geçmişinizi gözden geçirin.
- Düzenleme yaparken, varsayılan editörünüzü değiştirmek isterseniz, `EDITOR` ortam değişkenini ayarlayabilirsiniz.
- `fc` komutunu sık kullanıyorsanız, belirli komutları hızlıca düzenlemek için alias'lar oluşturmayı düşünebilirsiniz.