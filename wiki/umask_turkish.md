# [Linux] C Shell (csh) umask Kullanımı: Dosya izinlerini ayarlama

## Overview
`umask` komutu, yeni oluşturulan dosya ve dizinlerin varsayılan izinlerini belirlemek için kullanılır. Bu komut, kullanıcıların dosya ve dizinlerinin kimler tarafından erişilebileceğini kontrol etmelerine yardımcı olur.

## Usage
Temel sözdizimi şu şekildedir:
```csh
umask [options] [arguments]
```

## Common Options
- `-S`: Umask değerini sembolik olarak gösterir.
- `-p`: Mevcut umask değerini gösterir.

## Common Examples
1. Mevcut umask değerini görüntüleme:
   ```csh
   umask
   ```

2. Umask değerini 022 olarak ayarlama (diğer kullanıcıların yazma iznini kaldırma):
   ```csh
   umask 022
   ```

3. Umask değerini sembolik olarak görüntüleme:
   ```csh
   umask -S
   ```

4. Umask değerini 007 olarak ayarlama (sadece sahibi ve grup üyeleri için okuma/yazma izni):
   ```csh
   umask 007
   ```

## Tips
- Umask değerini ayarlarken, dosya ve dizin izinlerini dikkatlice düşünün; yanlış ayarlar, istenmeyen erişim kısıtlamalarına yol açabilir.
- Umask ayarlarını, kullanıcı oturumunuzun başlangıcında `.cshrc` dosyasına ekleyerek kalıcı hale getirebilirsiniz.
- Umask değerini kontrol etmek için sık sık `umask` komutunu kullanarak mevcut ayarları gözden geçirin.