# [Linux] C Shell (csh) ftp Kullanımı: Dosya transferi için bir komut

## Genel Bakış
`ftp` komutu, dosyaları bir bilgisayardan diğerine aktarmak için kullanılan bir protokoldür. Bu komut, kullanıcıların dosya yüklemesine veya indirmesine olanak tanır ve genellikle uzak sunucularla etkileşimde bulunmak için kullanılır.

## Kullanım
`ftp` komutunun temel sözdizimi aşağıdaki gibidir:

```
ftp [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-i`: Pasif modda çalışır, yani dosya transferi sırasında etkileşim istemez.
- `-v`: Ayrıntılı modda çalışır, daha fazla bilgi gösterir.
- `-n`: Oturum açmadan önce bağlantı kurar, bu sayede kullanıcı adı ve şifre girmeden bağlantı sağlar.
- `-g`: Dosya transferi sırasında dosya adlarında genişletme yapılmasını engeller.

## Yaygın Örnekler
Aşağıda `ftp` komutunun bazı pratik örnekleri verilmiştir:

### 1. Uzak bir sunucuya bağlanma
```bash
ftp ftp.example.com
```

### 2. Kullanıcı adı ve şifre ile bağlanma
```bash
ftp -n ftp.example.com
```
Ardından, kullanıcı adı ve şifreyi girin.

### 3. Dosya indirme
```bash
get dosya.txt
```

### 4. Dosya yükleme
```bash
put dosya.txt
```

### 5. Tüm dosyaları indirme
```bash
mget *
```

## İpuçları
- Uzak sunucuya bağlanmadan önce, bağlantı bilgilerinizi (sunucu adı, kullanıcı adı, şifre) hazırlayın.
- `binary` modunu kullanarak ikili dosyaları aktarırken veri kaybını önleyin.
- Aktarım işlemleri sırasında bağlantının kesilmemesi için sabit bir internet bağlantısı kullanın.