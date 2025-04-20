# [Linux] C Shell (csh) tr Kullanımı: Karakterleri Dönüştürme

## Overview
`tr` komutu, bir dosyadaki veya standart girdideki karakterleri dönüştürmek veya silmek için kullanılır. Genellikle metin işleme görevlerinde faydalıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```csh
tr [options] [arguments]
```

## Common Options
- `-d`: Belirtilen karakterleri siler.
- `-s`: Ardışık aynı karakterleri tek bir karakterle birleştirir.
- `-c`: Belirtilen karakterler dışındaki tüm karakterleri işler.

## Common Examples
1. **Karakter Dönüştürme**: Küçük harfleri büyük harflere dönüştürme.
   ```csh
   echo "merhaba dünya" | tr 'a-z' 'A-Z'
   ```
   Çıktı: `MERHABA DÜNYA`

2. **Karakter Silme**: Belirli karakterleri silme.
   ```csh
   echo "merhaba dünya" | tr -d 'a'
   ```
   Çıktı: `merhb dny`

3. **Ardışık Boşlukları Tek Boşluğa Dönüştürme**:
   ```csh
   echo "merhaba    dünya" | tr -s ' '
   ```
   Çıktı: `merhaba dünya`

4. **Karakterleri Tersine Çevirme**: Belirli karakterler dışındaki tüm karakterleri dönüştürme.
   ```csh
   echo "merhaba dünya" | tr -c 'a-zA-Z' ' '
   ```
   Çıktı: `merhaba dünya`

## Tips
- `tr` komutunu kullanırken, girdi verisinin doğru formatta olduğundan emin olun.
- Çok büyük dosyalarla çalışıyorsanız, `tr` komutunu bir dosya üzerinde kullanmak için dosya adını doğrudan belirtebilirsiniz.
- `tr` komutunu diğer komutlarla birleştirerek daha karmaşık metin işleme görevleri gerçekleştirebilirsiniz.