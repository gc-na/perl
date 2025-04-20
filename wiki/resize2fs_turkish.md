# [Linux] C Shell (csh) resize2fs Kullanımı: Dosya sistemini boyutlandırma aracı

## Genel Bakış
`resize2fs`, bir dosya sisteminin boyutunu değiştirmek için kullanılan bir komuttur. Genellikle, bir dosya sisteminin boyutunu artırmak veya azaltmak için kullanılır ve ext2, ext3 ve ext4 dosya sistemleri ile uyumludur.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
resize2fs [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-f`: Zorla boyutlandırma işlemi yapar.
- `-p`: İşlem sırasında ilerleme durumunu gösterir.
- `-s`: Dosya sistemini boyutlandırırken, mevcut boyutunu korur.
- `-M`: Dosya sistemini minimum boyuta küçültür.

## Yaygın Örnekler
Aşağıda `resize2fs` komutunun bazı pratik kullanımları bulunmaktadır:

### Dosya Sistemini Büyütme
Bir dosya sistemini mevcut disk alanı ile büyütmek için:

```bash
resize2fs /dev/sda1
```

### Dosya Sistemini Küçültme
Bir dosya sistemini belirli bir boyuta küçültmek için:

```bash
resize2fs /dev/sda1 10G
```

### İlerleme Durumunu Gösterme
Boyutlandırma işlemi sırasında ilerlemeyi görmek için:

```bash
resize2fs -p /dev/sda1
```

### Zorla Boyutlandırma
Eğer boyutlandırma işlemi başarısız olursa zorla devam etmek için:

```bash
resize2fs -f /dev/sda1
```

## İpuçları
- Boyutlandırma işlemi öncesinde dosya sisteminin yedeğini almak iyi bir uygulamadır.
- Dosya sistemini küçültmeden önce, dosya sisteminin en az %10'unun boş olduğundan emin olun.
- Boyutlandırma işlemi sırasında dosya sisteminin bağlı olmadığından emin olun; bu, veri kaybını önlemek için önemlidir.