# [Linux] C Shell (csh) shutdown Kullanımı: Sistemi kapatmak için kullanılan bir komut

## Overview
`shutdown` komutu, bir sistemi kapatmak veya yeniden başlatmak için kullanılır. Bu komut, sistem yöneticileri tarafından genellikle bakım veya güncelleme işlemleri sırasında kullanılır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```
shutdown [options] [arguments]
```

## Common Options
- `-h`: Sistemi kapatır.
- `-r`: Sistemi yeniden başlatır.
- `now`: Komutun hemen uygulanmasını sağlar.
- `+m`: Belirtilen dakika sayısı sonra kapatma işlemini gerçekleştirir.

## Common Examples
Aşağıda `shutdown` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Sistemi hemen kapatmak için:
   ```csh
   shutdown -h now
   ```

2. Sistemi 5 dakika sonra yeniden başlatmak için:
   ```csh
   shutdown -r +5
   ```

3. Sistemi 1 dakika sonra kapatmak için:
   ```csh
   shutdown -h +1
   ```

4. Sistemi hemen yeniden başlatmak için:
   ```csh
   shutdown -r now
   ```

## Tips
- Sistemi kapatmadan önce açık olan uygulamaları kontrol edin ve kaydedilmemiş verilerinizi kaydedin.
- `shutdown` komutunu kullanmadan önce yeterli izinlere sahip olduğunuzdan emin olun; genellikle bu komut için yönetici (root) yetkileri gereklidir.
- Kapatma işlemi sırasında diğer kullanıcıları bilgilendirmek için bir mesaj ekleyebilirsiniz. Örneğin:
  ```csh
  shutdown -h +5 "Sistem 5 dakika içinde kapatılacaktır."
  ```