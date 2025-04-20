# [Linux] C Shell (csh) ss Kullanımı: Ağ soketlerini görüntüleme

## Genel Bakış
`ss` komutu, ağ soketleri hakkında bilgi almak için kullanılan bir araçtır. Bu komut, aktif bağlantıları, dinleyen soketleri ve diğer ağ bağlantı durumlarını hızlı bir şekilde görüntülemenizi sağlar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
ss [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-t`: TCP soketlerini gösterir.
- `-u`: UDP soketlerini gösterir.
- `-l`: Dinleyen soketleri listeler.
- `-p`: Soketlerle ilişkili süreçleri gösterir.
- `-n`: Adresleri ve port numaralarını sayısal olarak gösterir.

## Yaygın Örnekler
Aşağıda `ss` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. Tüm aktif TCP bağlantılarını görüntüleme:
   ```bash
   ss -t
   ```

2. Dinleyen UDP soketlerini listeleme:
   ```bash
   ss -u -l
   ```

3. Tüm soketleri ve ilişkili süreçleri gösterme:
   ```bash
   ss -p
   ```

4. Sayısal adres ve port numaraları ile tüm dinleyen soketleri görüntüleme:
   ```bash
   ss -l -n
   ```

## İpuçları
- `ss` komutunu kullanırken, belirli bir protokolü hedeflemek için `-t` veya `-u` seçeneklerini kullanarak çıktıyı daraltabilirsiniz.
- Ağ sorunlarını teşhis etmek için `ss -t -p` komutunu kullanarak hangi süreçlerin hangi bağlantıları kullandığını görebilirsiniz.
- Çıktıyı daha okunabilir hale getirmek için `grep` komutunu kullanarak belirli bir bağlantıyı veya durumu filtreleyebilirsiniz. Örneğin:
  ```bash
  ss -t | grep ESTAB
  ```