# [Linux] C Shell (csh) renice Kullanımı: İşlem önceliğini değiştirme

## Overview
`renice` komutu, çalışan bir işlemin önceliğini değiştirmek için kullanılır. Bu, sistem kaynaklarının nasıl dağıtılacağını etkileyerek, belirli bir işlemin diğerlerine göre daha fazla veya daha az kaynak almasını sağlar.

## Usage
Temel sözdizimi şu şekildedir:

```csh
renice [options] [arguments]
```

## Common Options
- `-n`: Yeni öncelik değerini belirtir. Bu değer, işlemin önceliğini artırmak veya azaltmak için kullanılır.
- `-p`: Önceliği değiştirilecek işlemin PID'sini belirtir.
- `-g`: Belirli bir grup ID'sine ait tüm işlemlerin önceliğini değiştirir.
- `-u`: Belirli bir kullanıcıya ait tüm işlemlerin önceliğini değiştirir.

## Common Examples
Aşağıda `renice` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Belirli bir işlemin önceliğini artırmak:
   ```csh
   renice -n -5 -p 1234
   ```

2. Belirli bir işlemin önceliğini azaltmak:
   ```csh
   renice -n 10 -p 5678
   ```

3. Belirli bir kullanıcıya ait tüm işlemlerin önceliğini değiştirmek:
   ```csh
   renice -n 5 -u kullanıcı_adı
   ```

4. Belirli bir grup ID'sine ait tüm işlemlerin önceliğini değiştirmek:
   ```csh
   renice -n 3 -g grup_id
   ```

## Tips
- `renice` komutunu kullanmadan önce, işlemin PID'sini öğrenmek için `ps` komutunu kullanabilirsiniz.
- Öncelik değerleri -20 ile 19 arasında değişir; -20 en yüksek önceliği, 19 ise en düşük önceliği temsil eder.
- Dikkatli olun; yüksek öncelik atamak, sistemin diğer işlemlerinin performansını olumsuz etkileyebilir.