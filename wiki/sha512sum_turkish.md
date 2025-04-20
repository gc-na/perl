# [Linux] C Shell (csh) sha512sum Kullanımı: Dosya bütünlüğünü kontrol etme

## Genel Bakış
`sha512sum` komutu, dosyaların SHA-512 hash değerlerini hesaplamak için kullanılır. Bu, dosyaların bütünlüğünü kontrol etmek ve verilerin değiştirilip değiştirilmediğini doğrulamak için yararlıdır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```csh
sha512sum [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-b`: Dosyayı ikili modda işle.
- `-c`: Hash değerlerini kontrol et.
- `-h`: Yardım bilgilerini göster.
- `--tag`: Hash değerini dosya adı ile birlikte göster.

## Yaygın Örnekler
Aşağıda `sha512sum` komutunun bazı pratik örnekleri bulunmaktadır:

### 1. Bir dosyanın SHA-512 hash değerini hesaplama
```csh
sha512sum dosya.txt
```

### 2. Birden fazla dosyanın hash değerlerini hesaplama
```csh
sha512sum dosya1.txt dosya2.txt
```

### 3. Hash değerlerini kontrol etme
Önceden oluşturulmuş bir hash dosyasını kontrol etmek için:
```csh
sha512sum -c hash_dosyası.txt
```

### 4. Hash değerini bir dosyaya yazma
```csh
sha512sum dosya.txt > hash_dosyası.txt
```

## İpuçları
- Hash değerlerini kontrol etmek için her zaman bir hash dosyası oluşturun ve bu dosyayı güvenli bir yerde saklayın.
- Dosyaların bütünlüğünü sağlamak için hash değerlerini düzenli olarak kontrol edin.
- `-b` seçeneğini kullanarak ikili dosyalarla çalışırken doğru sonuçlar elde ettiğinizden emin olun.