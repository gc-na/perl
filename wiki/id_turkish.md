# [Linux] C Shell (csh) id Kullanımı: Kullanıcı kimliğini görüntüleme

## Genel Bakış
`id` komutu, kullanıcı kimliği (UID) ve grup kimliği (GID) bilgilerini görüntülemek için kullanılır. Bu komut, sistemdeki kullanıcıların ve grupların kimlik bilgilerini hızlı bir şekilde kontrol etmenizi sağlar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
id [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-u`: Kullanıcının UID'sini gösterir.
- `-g`: Kullanıcının GID'sini gösterir.
- `-G`: Kullanıcının ait olduğu tüm grup kimliklerini gösterir.
- `-n`: Kullanıcı veya grup adını gösterir.

## Yaygın Örnekler
Aşağıda `id` komutunun bazı pratik örnekleri verilmiştir:

1. Kullanıcı kimliğini ve grup bilgilerini görüntüleme:
   ```bash
   id
   ```

2. Belirli bir kullanıcının UID ve GID bilgilerini görüntüleme:
   ```bash
   id kullanıcı_adı
   ```

3. Sadece kullanıcı UID'sini görüntüleme:
   ```bash
   id -u kullanıcı_adı
   ```

4. Kullanıcının ait olduğu tüm grup kimliklerini görüntüleme:
   ```bash
   id -G kullanıcı_adı
   ```

5. Kullanıcı adı ile birlikte UID ve GID bilgilerini görüntüleme:
   ```bash
   id -n kullanıcı_adı
   ```

## İpuçları
- `id` komutunu kullanarak, bir kullanıcının hangi gruplara ait olduğunu hızlıca öğrenebilirsiniz.
- Özellikle sistem yöneticileri için, kullanıcıların izinlerini kontrol etmek amacıyla `id` komutu oldukça faydalıdır.
- `id` komutunu sık kullanıyorsanız, alias tanımlayarak daha kısa bir komut oluşturabilirsiniz. Örneğin:
  ```bash
  alias uid='id -u'
  ```