# [Linux] C Shell (csh) pwd Kullanımı: Mevcut dizini gösterir

## Overview
`pwd` (print working directory), mevcut çalışma dizininizin tam yolunu gösteren bir komuttur. Terminalde hangi dizinde bulunduğunuzu hızlıca öğrenmek için kullanılır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```
pwd [options] [arguments]
```

## Common Options
- `-L`: Mantıksal yolun gösterilmesini sağlar. Eğer sembolik bağlantılar varsa, bu seçenek ile bağlantının gösterildiği dizin görüntülenir.
- `-P`: Fiziksel yolun gösterilmesini sağlar. Bu seçenek ile sembolik bağlantılar takip edilmez ve gerçek dizin yolu gösterilir.

## Common Examples
Aşağıda `pwd` komutunun bazı pratik örnekleri verilmiştir:

### Örnek 1: Basit kullanım
Mevcut dizini görüntülemek için:
```csh
pwd
```

### Örnek 2: Mantıksal yol gösterimi
Mantıksal yolu görüntülemek için:
```csh
pwd -L
```

### Örnek 3: Fiziksel yol gösterimi
Fiziksel yolu görüntülemek için:
```csh
pwd -P
```

## Tips
- `pwd` komutunu sık sık kullanarak bulunduğunuz dizini kontrol edebilir ve dosya yönetiminizi kolaylaştırabilirsiniz.
- Eğer birden fazla terminal penceresi açtıysanız, her birinde `pwd` komutunu kullanarak hangi dizinde çalıştığınızı hızlıca öğrenebilirsiniz.
- Sembolik bağlantılarla çalışıyorsanız, `-P` seçeneğini kullanarak gerçek dizin yolunu görmek faydalı olabilir.