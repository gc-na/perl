# [Linux] C Shell (csh) nice Kullanımı: İşlem önceliğini ayarlama

## Overview
`nice` komutu, bir işlemin CPU zamanını kullanma önceliğini ayarlamak için kullanılır. Bu, sistem kaynaklarının daha verimli bir şekilde dağıtılmasına yardımcı olur ve daha düşük öncelikli işlemlerin sistem üzerinde daha az etkisi olmasını sağlar.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```
nice [options] [arguments]
```

## Common Options
- `-n, --adjustment`: Öncelik ayarlaması. Varsayılan olarak 10'dur. Daha düşük bir değer daha yüksek öncelik, daha yüksek bir değer daha düşük öncelik anlamına gelir.
- `-h, --help`: Yardım mesajını gösterir.
- `-v, --version`: Versiyon bilgisini gösterir.

## Common Examples
Aşağıda `nice` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Varsayılan öncelikle bir işlem başlatma:
   ```csh
   nice myscript.sh
   ```

2. Önceliği 5 olarak ayarlayarak bir işlem başlatma:
   ```csh
   nice -n 5 myscript.sh
   ```

3. Önceliği -10 olarak ayarlayarak bir işlem başlatma (daha yüksek öncelik):
   ```csh
   nice -n -10 myscript.sh
   ```

4. Bir komutun önceliğini kontrol etme:
   ```csh
   ps -o pid,nice,cmd
   ```

## Tips
- `nice` komutunu kullanarak sistem kaynaklarını daha verimli yönetebilirsiniz; yoğun kaynak kullanan işlemleri düşük önceliklerle başlatmak iyi bir uygulamadır.
- Öncelik ayarlarken, sistemin genel performansını etkilememek için dikkatli olun.
- `renice` komutunu kullanarak zaten çalışan bir işlemin önceliğini değiştirebilirsiniz.