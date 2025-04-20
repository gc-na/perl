# [Linux] C Shell (csh) fdisk Kullanımı: Disk bölümlerini yönetme aracı

## Genel Bakış
`fdisk`, disk bölümlerini yönetmek için kullanılan bir komuttur. Bu komut, disklerdeki bölümleri oluşturma, silme ve düzenleme işlemlerini gerçekleştirmenizi sağlar. Genellikle, disk yapılandırmalarını değiştirmek veya yeni bölümler eklemek için kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
fdisk [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-l`: Tüm diskleri ve bölümlerini listelemek için kullanılır.
- `-u`: Boyutları sektör cinsinden gösterir.
- `-n`: Yeni bir bölüm oluşturmak için kullanılır.
- `-d`: Mevcut bir bölümü silmek için kullanılır.
- `-p`: Mevcut bölümleri yazdırmak için kullanılır.

## Yaygın Örnekler
Aşağıda `fdisk` komutunun bazı pratik örnekleri verilmiştir:

1. Tüm diskleri ve bölümleri listeleme:
   ```bash
   fdisk -l
   ```

2. Yeni bir bölüm oluşturma:
   ```bash
   fdisk /dev/sda
   ```
   Ardından, `n` tuşuna basarak yeni bir bölüm oluşturma işlemini başlatabilirsiniz.

3. Mevcut bir bölümü silme:
   ```bash
   fdisk /dev/sda
   ```
   Ardından, `d` tuşuna basarak silmek istediğiniz bölümü seçebilirsiniz.

4. Mevcut bölümleri yazdırma:
   ```bash
   fdisk -p /dev/sda
   ```

## İpuçları
- `fdisk` komutunu kullanmadan önce, disk ve bölüm yapınızı yedeklemeniz önemlidir.
- Yanlışlıkla veri kaybını önlemek için dikkatli olun ve hangi bölümü sildiğinizi veya değiştirdiğinizi not edin.
- Disk bölümleme işlemlerini gerçekleştirmeden önce, sisteminizin mevcut durumunu kontrol etmek için `df -h` komutunu kullanabilirsiniz.