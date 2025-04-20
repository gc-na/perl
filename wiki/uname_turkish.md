# [Linux] C Shell (csh) uname Kullanımı: Sistem bilgilerini görüntüleme

## Overview
`uname` komutu, sistem hakkında bilgi almak için kullanılan bir komuttur. Bu komut, işletim sistemi adı, sürüm numarası, makine türü gibi çeşitli bilgileri görüntülemenizi sağlar.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```
uname [options] [arguments]
```

## Common Options
- `-a`: Tüm bilgileri bir arada gösterir.
- `-s`: İşletim sistemi adını gösterir.
- `-n`: Ağ ana bilgisayar adını gösterir.
- `-r`: İşletim sistemi sürümünü gösterir.
- `-m`: Makine türünü gösterir.

## Common Examples
Aşağıda `uname` komutunun bazı pratik örnekleri bulunmaktadır:

1. İşletim sistemi adını görüntüleme:
   ```csh
   uname -s
   ```

2. Tüm sistem bilgilerini görüntüleme:
   ```csh
   uname -a
   ```

3. İşletim sistemi sürümünü görüntüleme:
   ```csh
   uname -r
   ```

4. Ağ ana bilgisayar adını görüntüleme:
   ```csh
   uname -n
   ```

5. Makine türünü görüntüleme:
   ```csh
   uname -m
   ```

## Tips
- `uname -a` komutunu kullanarak sistem hakkında kapsamlı bilgi alabilirsiniz.
- Komutları çalıştırmadan önce, hangi bilgilere ihtiyaç duyduğunuzu belirlemek, gereksiz bilgi yükünden kaçınmanıza yardımcı olur.
- Eğer bir betik yazıyorsanız, `uname` komutunu kullanarak sistemin özelliklerine göre farklı işlemler gerçekleştirebilirsiniz.