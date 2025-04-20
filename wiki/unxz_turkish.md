# [Linux] C Shell (csh) unxz Kullanımı: Sıkıştırılmış dosyaları açma

## Genel Bakış
`unxz`, `.xz` uzantılı dosyaları açmak için kullanılan bir komuttur. Bu komut, XZ sıkıştırma formatında olan dosyaları dekomprese ederek orijinal dosyayı geri getirir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
unxz [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-k`: Sıkıştırılmış dosyayı silmeden açar.
- `-f`: Zorla açma işlemi yapar, mevcut dosyaların üzerine yazabilir.
- `-v`: Ayrıntılı çıktı verir, işlem sırasında neler olduğunu gösterir.

## Yaygın Örnekler
Aşağıda `unxz` komutunun bazı pratik örnekleri bulunmaktadır:

### Örnek 1: Basit Kullanım
Bir `.xz` dosyasını açmak için:

```bash
unxz dosya.xz
```

### Örnek 2: Dosyayı Silmeden Açma
Sıkıştırılmış dosyayı açarken orijinal dosyayı korumak için:

```bash
unxz -k dosya.xz
```

### Örnek 3: Zorla Açma
Mevcut dosyaların üzerine yazmak için:

```bash
unxz -f dosya.xz
```

### Örnek 4: Ayrıntılı Çıktı
İşlem sırasında ayrıntılı bilgi almak için:

```bash
unxz -v dosya.xz
```

## İpuçları
- `unxz` komutunu kullanmadan önce dosyanızın yedeğini almak iyi bir uygulamadır.
- Sıkıştırılmış dosyaların bulunduğu dizinde çalıştığınızdan emin olun.
- Eğer birden fazla dosyayı açmak istiyorsanız, dosya adlarını boşlukla ayırarak listeleyebilirsiniz. Örneğin: `unxz dosya1.xz dosya2.xz`.