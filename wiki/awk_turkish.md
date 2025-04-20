# [Linux] C Shell (csh) awk Kullanımı: Metin işleme aracı

## Genel Bakış
`awk`, metin dosyalarını işlemek ve analiz etmek için kullanılan güçlü bir programlama dilidir. Genellikle veri biçimlendirme, filtreleme ve raporlama işlemleri için kullanılır. `awk`, satır bazında çalışarak, belirli desenlere uyan verileri seçebilir ve bu veriler üzerinde işlemler gerçekleştirebilir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
awk [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-F`: Girdi dosyasında alan ayırıcıyı belirtir. Örneğin, `-F,` virgül ile ayrılmış dosyalar için kullanılır.
- `-v`: Değişken tanımlamak için kullanılır. Örneğin, `-v name=value`.
- `-f`: Bir dosyadan `awk` komutlarını yüklemek için kullanılır.

## Yaygın Örnekler
1. **Bir dosyadaki tüm satırları yazdırma:**
   ```bash
   awk '{print}' dosya.txt
   ```

2. **Belirli bir alanı yazdırma (örneğin, ikinci alan):**
   ```bash
   awk '{print $2}' dosya.txt
   ```

3. **Virgülle ayrılmış bir dosyadan belirli bir alanı yazdırma:**
   ```bash
   awk -F, '{print $1}' dosya.csv
   ```

4. **Bir koşula göre satırları filtreleme (örneğin, 100'den büyük sayılar):**
   ```bash
   awk '$1 > 100' sayilar.txt
   ```

5. **Bir dosyadaki belirli bir kelimeyi sayma:**
   ```bash
   awk '/kelime/ {count++} END {print count}' dosya.txt
   ```

## İpuçları
- `awk` komutunu kullanırken, alanları belirtmek için `$1`, `$2` gibi ifadeleri kullanarak belirli alanlara erişebilirsiniz.
- Girdi dosyanızın formatını iyi anlayarak, uygun alan ayırıcıları kullanmak işlemlerinizi kolaylaştırır.
- `awk` ile karmaşık işlemler yapmak için döngüler ve koşullu ifadeler kullanabilirsiniz, bu da onu güçlü bir araç haline getirir.