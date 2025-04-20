# [Linux] C Shell (csh) iostat Kullanımı: Disk ve CPU istatistiklerini izleme

## Overview
iostat komutu, sistemin disk ve CPU kullanımını izlemek için kullanılır. Bu komut, sistem performansını değerlendirmek ve potansiyel darboğazları tespit etmek için yararlıdır.

## Usage
Temel sözdizimi şu şekildedir:
```csh
iostat [options] [arguments]
```

## Common Options
- `-c`: Sadece CPU istatistiklerini gösterir.
- `-d`: Sadece disk istatistiklerini gösterir.
- `-x`: Genişletilmiş disk istatistiklerini gösterir.
- `-h`: İnsan tarafından okunabilir formatta çıktı verir.
- `-t`: Zaman damgası ile birlikte çıktı verir.

## Common Examples
Aşağıda iostat komutunun bazı pratik örnekleri bulunmaktadır:

1. Temel disk ve CPU istatistiklerini görüntüleme:
   ```csh
   iostat
   ```

2. Sadece CPU istatistiklerini gösterme:
   ```csh
   iostat -c
   ```

3. Genişletilmiş disk istatistiklerini görüntüleme:
   ```csh
   iostat -x
   ```

4. İnsan tarafından okunabilir formatta çıktı alma:
   ```csh
   iostat -h
   ```

5. Zaman damgası ile birlikte istatistikleri görüntüleme:
   ```csh
   iostat -t
   ```

## Tips
- iostat komutunu düzenli olarak çalıştırarak sistem performansını izleyin.
- Özellikle yoğun iş yükü altında, disk ve CPU kullanımını analiz etmek için genişletilmiş istatistikleri kullanın.
- Çıktıları bir dosyaya yönlendirerek zamanla karşılaştırmalar yapabilirsiniz:
  ```csh
  iostat -x > istatistikler.txt
  ```