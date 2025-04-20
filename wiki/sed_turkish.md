# [Linux] C Shell (csh) sed Kullanımı: Metin düzenleme aracı

## Genel Bakış
`sed`, akış düzenleyici olarak bilinen bir komuttur. Metin akışını alır ve belirli kurallara göre düzenler. Genellikle dosya içeriğini değiştirmek, arama yapmak veya metin üzerinde dönüşümler gerçekleştirmek için kullanılır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
sed [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-e`: Birden fazla komut belirtmek için kullanılır.
- `-i`: Dosyayı yerinde düzenler, yani değişiklikleri dosyaya kaydeder.
- `-n`: Varsayılan çıktıyı bastırır; yalnızca belirtilen komutlarla sonuçları gösterir.
- `s/pattern/replacement/`: Belirtilen deseni bulur ve yerine yeni metni koyar.

## Yaygın Örnekler
1. Bir dosyada belirli bir kelimeyi değiştirmek:
   ```bash
   sed 's/eski/yeni/' dosya.txt
   ```

2. Tüm satırlarda belirli bir kelimeyi değiştirmek:
   ```bash
   sed -i 's/eski/yeni/g' dosya.txt
   ```

3. Belirli bir deseni içeren satırları bastırmak:
   ```bash
   sed -n '/desen/p' dosya.txt
   ```

4. Birden fazla değişiklik yapmak:
   ```bash
   sed -e 's/eski/yeni/' -e 's/başka/yeni2/' dosya.txt
   ```

## İpuçları
- `-i` seçeneğini kullanırken dikkatli olun; değişiklikler geri alınamaz.
- Değişikliklerinizi test etmek için önce `-n` seçeneğini kullanarak çıktıyı gözlemleyin.
- Karmaşık düzenlemeler için birden fazla `-e` seçeneği kullanarak birden fazla komut yazabilirsiniz.