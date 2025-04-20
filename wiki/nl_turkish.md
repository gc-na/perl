# [Linux] C Shell (csh) nl Kullanımı: Satır numaraları ekleme

## Overview
`nl` komutu, bir dosyanın içeriğine satır numaraları ekleyerek çıktısını oluşturur. Bu, metin dosyalarının okunabilirliğini artırmak ve belirli satırları kolayca referans almak için kullanışlıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```
nl [options] [arguments]
```

## Common Options
- `-b` : Satır numarası ekleme biçimini belirler. Örneğin, `-b a` tüm satırlara numara ekler.
- `-f` : Boş satırların numaralandırılmasını kontrol eder. `-f n` ile boş satırlar numaralandırılmaz.
- `-n` : Satır numaralarının biçimini ayarlar. `-n ln` ile numaralar soldan hizalanır.
- `-w` : Satır numaralarının genişliğini ayarlamak için kullanılır. Örneğin, `-w 4` ile numaralar 4 karakter genişliğinde olur.

## Common Examples
Aşağıda `nl` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Basit bir dosyaya satır numarası eklemek:
   ```bash
   nl dosya.txt
   ```

2. Tüm satırlara numara eklemek için:
   ```bash
   nl -b a dosya.txt
   ```

3. Boş satırları numaralandırmadan çıktı almak:
   ```bash
   nl -f n dosya.txt
   ```

4. Satır numaralarının genişliğini ayarlamak:
   ```bash
   nl -w 4 dosya.txt
   ```

## Tips
- `nl` komutunu kullanırken, dosyanın içeriğini daha iyi anlamak için farklı seçenekleri bir arada kullanmayı deneyin.
- Çıktıyı başka bir dosyaya yönlendirmek için `>` operatörünü kullanabilirsiniz:
  ```bash
  nl dosya.txt > numaralandirilmis_dosya.txt
  ```
- `man nl` komutunu kullanarak daha fazla bilgi ve seçenekler hakkında yardım alabilirsiniz.