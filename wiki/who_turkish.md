# [Linux] C Shell (csh) who Kullanımı: Kullanıcı oturumlarını görüntüleme

## Overview
`who` komutu, sistemde oturum açmış olan kullanıcıları listelemek için kullanılır. Bu komut, kullanıcıların hangi terminalde oturum açtığını ve oturum açma zamanlarını gösterir.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```
who [options] [arguments]
```

## Common Options
- `-a`: Tüm bilgileri gösterir, kullanıcıların yanı sıra sistem bilgilerini de içerir.
- `-b`: Sistemin en son ne zaman yeniden başlatıldığını gösterir.
- `-q`: Sadece kullanıcı adlarını ve toplam kullanıcı sayısını gösterir.
- `-r`: Sistem durumunu ve runlevel bilgisini gösterir.

## Common Examples
Aşağıda `who` komutunun bazı pratik örnekleri bulunmaktadır:

1. Sistemdeki tüm oturum açmış kullanıcıları listeleme:
   ```bash
   who
   ```

2. Sistemin en son ne zaman yeniden başlatıldığını gösterme:
   ```bash
   who -b
   ```

3. Sadece kullanıcı adlarını ve toplam kullanıcı sayısını gösterme:
   ```bash
   who -q
   ```

4. Tüm bilgileri gösterme:
   ```bash
   who -a
   ```

## Tips
- `who` komutunu sık sık kullanarak sistemdeki aktif kullanıcıları takip edebilirsiniz.
- Eğer daha fazla bilgiye ihtiyaç duyuyorsanız, `man who` komutunu kullanarak detaylı dökümantasyona erişebilirsiniz.
- `who` komutunu, sistem güvenliği ve kullanıcı yönetimi için düzenli olarak kontrol etmek faydalı olabilir.