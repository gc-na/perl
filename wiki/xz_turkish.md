# [Linux] C Shell (csh) xz Kullanımı: Dosyaları sıkıştırma ve açma

## Genel Bakış
`xz` komutu, dosyaları sıkıştırmak ve açmak için kullanılan bir araçtır. Yüksek sıkıştırma oranları sunarak, dosyaların boyutunu önemli ölçüde azaltabilir.

## Kullanım
Temel sözdizimi şu şekildedir:
```csh
xz [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-d`, `--decompress`: Sıkıştırılmış dosyayı açar.
- `-k`, `--keep`: Orijinal dosyayı koruyarak sıkıştırma işlemi yapar.
- `-f`, `--force`: Zaten sıkıştırılmış dosyaları zorla sıkıştırır.
- `-9`: En yüksek sıkıştırma seviyesini kullanır.

## Yaygın Örnekler
Aşağıda `xz` komutunun bazı pratik örnekleri bulunmaktadır:

### 1. Bir dosyayı sıkıştırma
```csh
xz dosya.txt
```

### 2. Sıkıştırılmış bir dosyayı açma
```csh
xz -d dosya.txt.xz
```

### 3. Orijinal dosyayı koruyarak sıkıştırma
```csh
xz -k dosya.txt
```

### 4. En yüksek sıkıştırma seviyesini kullanarak sıkıştırma
```csh
xz -9 dosya.txt
```

## İpuçları
- Sıkıştırma işlemi sırasında dosya boyutunu göz önünde bulundurun; bazı dosyalar için sıkıştırma oranı düşük olabilir.
- `-k` seçeneğini kullanarak orijinal dosyayı kaybetmeden sıkıştırma yapabilirsiniz.
- Sıkıştırılmış dosyaları açarken, `-d` seçeneğini kullanmayı unutmayın; aksi takdirde dosya açılmaz.