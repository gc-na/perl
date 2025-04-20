# [Linux] C Shell (csh) parted Kullanımı: Disk bölümlerini yönetme aracı

## Genel Bakış
`parted` komutu, disk bölümlerini yönetmek için kullanılan bir araçtır. Bu komut, disk alanını düzenlemek, yeni bölümler oluşturmak, mevcut bölümleri değiştirmek ve silmek gibi işlemleri gerçekleştirmenizi sağlar.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
parted [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-l` veya `--list`: Sistemdeki tüm diskleri ve bölümleri listele.
- `mkpart`: Yeni bir bölüm oluştur.
- `rm`: Mevcut bir bölümü sil.
- `resizepart`: Bir bölümün boyutunu değiştir.
- `print`: Mevcut bölümlerin bilgilerini göster.

## Yaygın Örnekler
Aşağıda `parted` komutunun bazı pratik kullanımları bulunmaktadır:

### 1. Diskleri Listeleme
Tüm diskleri ve bölümleri listelemek için:

```bash
parted -l
```

### 2. Yeni Bölüm Oluşturma
Bir disk üzerinde yeni bir bölüm oluşturmak için:

```bash
parted /dev/sda mkpart primary ext4 1MiB 100MiB
```

### 3. Bölüm Silme
Bir bölümü silmek için:

```bash
parted /dev/sda rm 1
```

### 4. Bölüm Boyutunu Değiştirme
Bir bölümün boyutunu değiştirmek için:

```bash
parted /dev/sda resizepart 1 200MiB
```

### 5. Mevcut Bölümleri Görüntüleme
Mevcut bölümlerin bilgilerini görüntülemek için:

```bash
parted /dev/sda print
```

## İpuçları
- `parted` komutunu kullanmadan önce, önemli verilerinizi yedeklemeyi unutmayın.
- Disk bölümleri üzerinde değişiklik yaparken dikkatli olun; yanlış bir işlem veri kaybına neden olabilir.
- `parted` komutunu çalıştırmadan önce, hangi disk üzerinde işlem yapacağınızı net bir şekilde belirleyin.