# [Linux] C Shell (csh) sftp Kullanımı: Dosya aktarımı için güvenli bir protokol

## Genel Bakış
sftp (Secure File Transfer Protocol), güvenli bir dosya aktarım protokolüdür. SSH (Secure Shell) üzerinden çalışan bu komut, dosyaların güvenli bir şekilde aktarılmasını sağlar. sftp, kullanıcıların uzak bir sunucuya bağlanarak dosya yüklemelerine, indirmelerine ve yönetmelerine olanak tanır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
sftp [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-o`: Seçenekleri belirtmek için kullanılır.
- `-P`: Uzak sunucunun port numarasını belirtir.
- `-v`: Ayrıntılı çıktı almak için kullanılır.
- `-b`: Bir dosyadan komutları topluca çalıştırmak için kullanılır.

## Yaygın Örnekler
1. Uzak bir sunucuya bağlanmak:
   ```bash
   sftp kullanıcı_adı@sunucu_adresi
   ```

2. Dosya indirmek:
   ```bash
   sftp kullanıcı_adı@sunucu_adresi:/uzak/dosya.txt /yerel/dosya.txt
   ```

3. Dosya yüklemek:
   ```bash
   sftp /yerel/dosya.txt kullanıcı_adı@sunucu_adresi:/uzak/dosya.txt
   ```

4. Uzak sunucudaki dosyaları listelemek:
   ```bash
   sftp kullanıcı_adı@sunucu_adresi
   ls
   ```

5. Birden fazla komut çalıştırmak için bir dosya kullanmak:
   ```bash
   sftp -b komutlar.txt kullanıcı_adı@sunucu_adresi
   ```

## İpuçları
- Bağlantı sırasında güvenlik için her zaman güçlü bir şifre kullanın.
- Dosya aktarımından önce uzak sunucudaki dosya izinlerini kontrol edin.
- SFTP oturumunu kapatmayı unutmayın; `exit` veya `bye` komutları ile çıkabilirsiniz.