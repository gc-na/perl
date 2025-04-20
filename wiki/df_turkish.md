# [Linux] C Shell (csh) df Kullanımı: Disk alanı bilgilerini görüntüleme

## Overview
`df` komutu, dosya sistemlerinin disk alanı kullanımını görüntülemek için kullanılır. Bu komut, her bir dosya sisteminin toplam, kullanılan ve boş alan miktarını gösterir.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```csh
df [options] [arguments]
```

## Common Options
- `-h`: İnsan tarafından okunabilir formatta (örneğin, MB veya GB cinsinden) çıktı verir.
- `-T`: Dosya sisteminin türünü gösterir.
- `-a`: Tüm dosya sistemlerini, boş olanlar dahil, listeler.
- `-i`: İnode kullanımını gösterir.

## Common Examples
Aşağıda `df` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Tüm dosya sistemlerinin disk alanı kullanımını görüntüleme:
   ```csh
   df
   ```

2. İnsan tarafından okunabilir formatta disk alanı bilgilerini görüntüleme:
   ```csh
   df -h
   ```

3. Belirli bir dosya sisteminin türü ile birlikte disk alanı bilgilerini görüntüleme:
   ```csh
   df -T
   ```

4. Tüm dosya sistemlerini, boş olanlar dahil, listeleme:
   ```csh
   df -a
   ```

5. İnode kullanımını gösterme:
   ```csh
   df -i
   ```

## Tips
- `df` komutunu sık sık kullanarak sisteminizin disk alanı durumunu takip edebilirsiniz.
- Disk alanı dolmaya başladığında, gereksiz dosyaları temizlemek için `df -h` çıktısını kontrol edin.
- Uzun süreli izleme için `df -h` komutunu bir betik içinde kullanarak düzenli aralıklarla çıktı alabilirsiniz.