# [Linux] C Shell (csh) top Kullanımı: Sistem kaynaklarını izleme

## Genel Bakış
`top` komutu, sistemdeki işlemleri ve kaynak kullanımını gerçek zamanlı olarak izlemek için kullanılır. Bu komut, CPU ve bellek kullanımı gibi önemli sistem bilgilerini görüntüleyerek kullanıcıların sistem performansını değerlendirmesine yardımcı olur.

## Kullanım
`top` komutunun temel sözdizimi aşağıdaki gibidir:

```csh
top [options] [arguments]
```

## Yaygın Seçenekler
- `-d <saniye>`: Güncelleme süresini saniye cinsinden ayarlar.
- `-n <sayı>`: Belirtilen sayı kadar güncelleme yapar ve ardından çıkış yapar.
- `-u <kullanıcı>`: Belirtilen kullanıcıya ait işlemleri gösterir.
- `-p <PID>`: Belirtilen işlem kimliğine (PID) ait bilgileri görüntüler.

## Yaygın Örnekler
Aşağıda `top` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. **Temel top komutunu çalıştırma:**
   ```csh
   top
   ```

2. **Güncelleme süresini 2 saniye olarak ayarlama:**
   ```csh
   top -d 2
   ```

3. **Sadece belirli bir kullanıcıya ait işlemleri görüntüleme:**
   ```csh
   top -u kullanıcı_adı
   ```

4. **Belirli bir PID'ye ait bilgileri görüntüleme:**
   ```csh
   top -p 1234
   ```

5. **5 güncelleme sonrası çıkış yapma:**
   ```csh
   top -n 5
   ```

## İpuçları
- `top` arayüzünde, `h` tuşuna basarak yardım alabilirsiniz.
- `k` tuşuna basarak bir işlemi sonlandırabilirsiniz; ardından PID'yi girmeniz gerekecektir.
- `M` tuşuna basarak işlemleri bellek kullanımına göre sıralayabilirsiniz.
- `P` tuşuna basarak işlemleri CPU kullanımına göre sıralamak mümkündür.

Bu bilgilerle `top` komutunu etkili bir şekilde kullanarak sistem kaynaklarınızı izleyebilirsiniz.