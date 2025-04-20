# [Linux] C Shell (csh) mysql Kullanımı: Veritabanı yönetimi için bir araç

## Overview
`mysql` komutu, MySQL veritabanı yönetim sistemine bağlanmak ve SQL sorguları çalıştırmak için kullanılan bir komuttur. Bu komut, veritabanları üzerinde işlem yapmayı kolaylaştırır ve kullanıcıların verileri yönetmesine olanak tanır.

## Usage
Temel sözdizimi şu şekildedir:
```bash
mysql [options] [arguments]
```

## Common Options
- `-u [kullanıcı_adı]`: MySQL sunucusuna bağlanmak için kullanılacak kullanıcı adını belirtir.
- `-p`: Şifre girişi için bir istem oluşturur. Kullanıcı şifresini girmek için bu seçeneği kullanmalısınız.
- `-h [sunucu_adresi]`: Bağlanılacak MySQL sunucusunun adresini belirtir. Varsayılan olarak localhost kullanılır.
- `-D [veritabanı_adı]`: Belirli bir veritabanına doğrudan bağlanmak için kullanılır.
- `--execute`: Belirtilen SQL sorgusunu doğrudan çalıştırır ve ardından çıkış yapar.

## Common Examples
Aşağıda `mysql` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. MySQL sunucusuna bağlanma:
   ```bash
   mysql -u root -p
   ```

2. Belirli bir veritabanına bağlanma:
   ```bash
   mysql -u kullanıcı_adı -p -D veritabanı_adı
   ```

3. SQL sorgusu çalıştırma:
   ```bash
   mysql -u kullanıcı_adı -p -e "SELECT * FROM tablo_adı;"
   ```

4. Belirli bir sunucuya bağlanma:
   ```bash
   mysql -h sunucu_adresi -u kullanıcı_adı -p
   ```

## Tips
- Şifrelerinizi güvenli bir şekilde saklayın ve komut satırında açık bir şekilde yazmamaya özen gösterin.
- Sık kullandığınız sorguları bir dosyaya kaydedip, `mysql` ile bu dosyayı çalıştırarak zaman kazanabilirsiniz.
- Veritabanı yedeklemesi yaparken `mysqldump` komutunu kullanmayı unutmayın.