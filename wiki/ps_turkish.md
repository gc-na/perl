# [Linux] C Shell (csh) ps Kullanımı: Çalışan süreçleri görüntüleme

## Genel Bakış
`ps` komutu, sistemde çalışan süreçlerin durumunu görüntülemek için kullanılır. Bu komut, kullanıcıların hangi süreçlerin aktif olduğunu ve bu süreçlerin kaynak kullanımını görmelerine olanak tanır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```
ps [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-e`: Tüm süreçleri gösterir.
- `-f`: Tam süreç bilgilerini gösterir.
- `-u [kullanıcı]`: Belirtilen kullanıcıya ait süreçleri listeler.
- `-p [PID]`: Belirtilen süreç kimliğine (PID) sahip süreci gösterir.
- `aux`: Tüm kullanıcıların süreçlerini detaylı bir şekilde gösterir.

## Yaygın Örnekler
Aşağıda `ps` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. Tüm süreçleri görüntülemek için:
   ```bash
   ps -e
   ```

2. Kullanıcıya ait süreçleri listelemek için:
   ```bash
   ps -u kullanıcı_adı
   ```

3. Belirli bir süreç kimliğine (PID) sahip süreci görüntülemek için:
   ```bash
   ps -p 1234
   ```

4. Tüm süreçleri detaylı bir şekilde görüntülemek için:
   ```bash
   ps aux
   ```

## İpuçları
- `ps` komutunu `grep` ile birleştirerek belirli bir süreci bulabilirsiniz:
  ```bash
  ps aux | grep sürec_adı
  ```
- Süreçlerin sürekli güncellenmiş görünümünü istiyorsanız, `top` komutunu kullanmayı düşünebilirsiniz.
- `ps` çıktısını daha okunabilir hale getirmek için `less` komutunu kullanabilirsiniz:
  ```bash
  ps aux | less
  ```