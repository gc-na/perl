# [Linux] C Shell (csh) kullanıcıları <Kullanıcıları listele>: Kullanıcıları görüntüleme komutu

## Genel Bakış
`users` komutu, sistemde oturum açmış olan kullanıcıların adlarını listelemek için kullanılır. Bu komut, sistem yöneticileri ve kullanıcılar için anlık olarak kimlerin oturum açtığını görmek açısından faydalıdır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```csh
users [options] [arguments]
```

## Yaygın Seçenekler
- `-n`: Kullanıcı adlarını sadece bir kez gösterir, tekrar eden kullanıcı adlarını filtreler.
- `-u`: Kullanıcıların oturum açma zamanlarını gösterir.

## Yaygın Örnekler
Aşağıda `users` komutunun bazı pratik örnekleri bulunmaktadır:

1. Sistemde oturum açmış olan kullanıcıları listeleme:
   ```csh
   users
   ```

2. Tekrar eden kullanıcı adlarını filtreleyerek listeleme:
   ```csh
   users -n
   ```

3. Kullanıcıların oturum açma zamanlarını gösterme:
   ```csh
   users -u
   ```

## İpuçları
- `users` komutunu sık sık kullanarak sistemdeki aktif kullanıcıları takip edebilirsiniz.
- Eğer sistemde çok sayıda kullanıcı varsa, `users -n` seçeneği ile daha temiz bir liste elde edebilirsiniz.
- Bu komut, sistem kaynaklarını yönetirken kullanıcıların durumunu gözlemlemek için faydalı olabilir.