# [Linux] C Shell (csh) stat Kullanımı: Dosya bilgilerini görüntüleme

## Overview
`stat` komutu, dosyaların ve dizinlerin ayrıntılı bilgilerini görüntülemek için kullanılır. Bu bilgiler arasında dosyanın boyutu, oluşturulma tarihi, son erişim tarihi ve izinler gibi detaylar bulunur.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
stat [options] [arguments]
```

## Common Options
- `-c` : Özel bir format belirlemek için kullanılır. 
- `-f` : Dosya sistemi bilgilerini görüntülemek için kullanılır.
- `-L` : Sembolik bağlantıların hedef dosyalarının bilgilerini gösterir.
- `--help` : Komut hakkında yardım bilgilerini gösterir.

## Common Examples
Aşağıda `stat` komutunun bazı pratik örnekleri bulunmaktadır:

1. Bir dosyanın bilgilerini görüntülemek:
   ```bash
   stat dosya.txt
   ```

2. Bir dizinin bilgilerini görüntülemek:
   ```bash
   stat /home/kullanici
   ```

3. Özel bir format ile dosya bilgilerini görüntülemek:
   ```bash
   stat -c '%n: %s bytes' dosya.txt
   ```

4. Sembolik bir bağlantının hedef dosyasının bilgilerini görüntülemek:
   ```bash
   stat -L sembolik_baglanti
   ```

## Tips
- `stat` komutunu sık kullandığınız dosyalar için bir alias oluşturabilirsiniz.
- Dosya izinlerini kontrol etmek için `stat` komutunu kullanmak, güvenlik açısından önemlidir.
- Özellikle büyük dosyalarla çalışırken, dosya boyutunu kontrol etmek için `stat` komutunu kullanmak faydalıdır.