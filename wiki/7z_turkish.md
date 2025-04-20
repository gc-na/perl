# [Linux] C Shell (csh) 7z Kullanımı: Dosyaları sıkıştırma ve açma aracı

## Genel Bakış
7z, dosyaları sıkıştırmak ve açmak için kullanılan güçlü bir komut satırı aracıdır. Özellikle yüksek sıkıştırma oranları sunan 7-Zip formatını destekler. Ayrıca, birçok farklı dosya formatını da açabilir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
7z [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `a`: Yeni bir arşiv oluşturur ve dosyaları ekler.
- `x`: Arşivden dosyaları çıkartır.
- `t`: Arşiv dosyasını test eder.
- `l`: Arşiv içeriğini listeler.
- `d`: Arşivden dosyaları siler.

## Yaygın Örnekler
1. **Bir dosyayı sıkıştırmak:**
   ```bash
   7z a arşiv.7z dosya.txt
   ```

2. **Bir arşivden dosyaları çıkartmak:**
   ```bash
   7z x arşiv.7z
   ```

3. **Arşiv içeriğini listelemek:**
   ```bash
   7z l arşiv.7z
   ```

4. **Arşivi test etmek:**
   ```bash
   7z t arşiv.7z
   ```

5. **Arşivden belirli bir dosyayı silmek:**
   ```bash
   7z d arşiv.7z dosya.txt
   ```

## İpuçları
- Sıkıştırma işlemi sırasında `-mx=9` seçeneğini kullanarak en yüksek sıkıştırma oranını elde edebilirsiniz.
- Arşiv dosyalarınızı düzenli tutmak için anlamlı isimler vermeye özen gösterin.
- Büyük dosyalarla çalışırken, işlemlerinizi arka planda gerçekleştirmek için `&` sembolünü kullanabilirsiniz.