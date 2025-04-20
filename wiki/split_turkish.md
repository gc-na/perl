# [Linux] C Shell (csh) split Kullanımı: Dosyaları parçalara ayırma

## Overview
`split` komutu, büyük dosyaları daha küçük parçalara ayırmak için kullanılır. Bu, özellikle büyük veri setleriyle çalışırken veya dosyaları daha yönetilebilir boyutlara bölmek istediğinizde faydalıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```
split [options] [arguments]
```

## Common Options
- `-b SIZE`: Her parçanın boyutunu belirler. Örneğin, `-b 100k` her parçayı 100 kilobayt olarak ayırır.
- `-l LINES`: Her parçanın satır sayısını belirler. Örneğin, `-l 50` her parçayı 50 satır olarak ayırır.
- `-d`: Parça isimlerinde sayıları kullanır. Varsayılan olarak harfler kullanılır.
- `--additional-suffix=SFX`: Parçaların isimlerine ek bir uzantı ekler.

## Common Examples
Aşağıda `split` komutunun bazı yaygın kullanımları verilmiştir:

1. **Dosyayı 100 kilobaytlık parçalara ayırma:**
   ```bash
   split -b 100k büyük_dosya.txt
   ```

2. **Dosyayı 50 satırlık parçalara ayırma:**
   ```bash
   split -l 50 büyük_dosya.txt
   ```

3. **Parça isimlerinde sayılar kullanma:**
   ```bash
   split -d -b 1m büyük_dosya.txt
   ```

4. **Parça isimlerine ek uzantı ekleme:**
   ```bash
   split --additional-suffix=.part büyük_dosya.txt
   ```

## Tips
- Büyük dosyaları parçalara ayırmadan önce, dosyanın boyutunu ve içeriğini kontrol etmek iyi bir fikirdir.
- Parçaları birleştirmek için `cat` komutunu kullanabilirsiniz. Örneğin, `cat x* > birlesik_dosya.txt` ile tüm parçaları birleştirebilirsiniz.
- Parçaların isimlendirme biçimini iyi planlayın, böylece daha sonra dosyaları kolayca bulabilirsiniz.