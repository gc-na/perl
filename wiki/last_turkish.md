# [Linux] C Shell (csh) last komutu: Kullanıcı oturum geçmişini görüntüleme

## Overview
`last` komutu, sistemdeki kullanıcıların oturum açma ve kapama geçmişini görüntülemek için kullanılır. Bu komut, kullanıcıların ne zaman oturum açtığını ve kapattığını gösterir, böylece sistem yöneticileri için kullanıcı etkinliğini takip etmek kolaylaşır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```
last [options] [arguments]
```

## Common Options
- `-n [number]`: Son [number] oturumu gösterir.
- `-R`: Host adlarını gizler.
- `-x`: Kapalı oturumları da gösterir.
- `-f [file]`: Belirtilen dosyadan oturum geçmişini okur.

## Common Examples
Aşağıda `last` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Tüm oturum geçmişini görüntüleme:
   ```csh
   last
   ```

2. Son 5 oturumu görüntüleme:
   ```csh
   last -n 5
   ```

3. Kapalı oturumları da gösterme:
   ```csh
   last -x
   ```

4. Belirli bir kullanıcı için oturum geçmişini görüntüleme:
   ```csh
   last username
   ```

5. Belirli bir dosyadan oturum geçmişini okuma:
   ```csh
   last -f /var/log/wtmp
   ```

## Tips
- `last` komutunu sık sık kullanarak kullanıcı etkinliğini takip edebilir ve sistem güvenliğini artırabilirsiniz.
- Komutun çıktısını daha iyi anlamak için, kullanıcı adları ve oturum süreleri hakkında bilgi sahibi olun.
- Eğer bir kullanıcıyı belirli bir süre boyunca izlemek istiyorsanız, `last` komutunu düzenli aralıklarla çalıştırarak bir kayıt tutabilirsiniz.