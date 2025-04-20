# [Linux] C Shell (csh) sqlite3 Kullanımı: SQLite veritabanı ile etkileşim

## Genel Bakış
`sqlite3` komutu, SQLite veritabanı dosyalarıyla etkileşimde bulunmak için kullanılan bir komuttur. Bu komut, veritabanı oluşturma, sorgulama yapma ve verileri yönetme gibi işlemleri gerçekleştirmenizi sağlar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```csh
sqlite3 [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-init <dosya>`: Başlangıçta çalıştırılacak SQL komutlarını içeren bir dosya belirtir.
- `-batch`: Komut satırı etkileşimini devre dışı bırakır ve sonuçları doğrudan çıktıya yazar.
- `-header`: Sorgu sonuçlarında sütun başlıklarını gösterir.
- `-version`: SQLite sürümünü gösterir.

## Yaygın Örnekler
Aşağıda `sqlite3` komutunun bazı pratik örnekleri bulunmaktadır:

1. Yeni bir veritabanı oluşturma:
   ```csh
   sqlite3 mydatabase.db
   ```

2. Bir tablo oluşturma:
   ```csh
   sqlite3 mydatabase.db "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);"
   ```

3. Veritabanına veri ekleme:
   ```csh
   sqlite3 mydatabase.db "INSERT INTO users (name) VALUES ('Ali');"
   ```

4. Verileri sorgulama:
   ```csh
   sqlite3 mydatabase.db "SELECT * FROM users;"
   ```

5. Veritabanını bir dosyadan başlatma:
   ```csh
   sqlite3 -init init.sql mydatabase.db
   ```

## İpuçları
- Veritabanı dosyalarının yedeğini almak için dosyayı kopyalayın.
- Sorgularınızı test etmeden önce bir test veritabanı kullanarak denemeler yapın.
- Sık kullanılan sorguları bir dosyada saklayarak `-init` seçeneği ile hızlı bir şekilde çalıştırabilirsiniz.