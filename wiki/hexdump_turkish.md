# [Linux] C Shell (csh) hexdump Kullanımı: Dosyaların hex formatında dökümünü alır

## Overview
hexdump komutu, bir dosyanın içeriğini hexadecimal (onaltılık) formatında görüntülemek için kullanılır. Bu komut, dosya içeriğini analiz etmek veya hata ayıklamak için oldukça faydalıdır.

## Usage
hexdump komutunun temel sözdizimi aşağıdaki gibidir:

```
hexdump [options] [arguments]
```

## Common Options
- `-C`: Hexadecimal ve ASCII formatında çıktı verir.
- `-n <bytes>`: Belirtilen bayt sayısı kadar çıktı alır.
- `-e <format>`: Çıktı formatını özelleştirir.
- `-v`: Tüm verileri gösterir, tekrar eden baytları gizlemez.

## Common Examples
Aşağıda hexdump komutunun bazı pratik örnekleri bulunmaktadır:

1. Bir dosyanın hexadecimal çıktısını almak:
   ```csh
   hexdump dosya.txt
   ```

2. Sadece ilk 16 baytı görüntülemek:
   ```csh
   hexdump -n 16 dosya.txt
   ```

3. Hem hexadecimal hem de ASCII çıktısını almak:
   ```csh
   hexdump -C dosya.txt
   ```

4. Özel bir format ile çıktı almak:
   ```csh
   hexdump -e '1/1 "%02x " "\n"' dosya.txt
   ```

## Tips
- Çıktıyı daha iyi anlamak için `-C` seçeneğini kullanarak hem hexadecimal hem de ASCII formatında görüntüleyin.
- Büyük dosyalarla çalışıyorsanız, `-n` seçeneği ile sadece ilgilendiğiniz kısmı görüntüleyerek zaman kazanabilirsiniz.
- Çıktıyı bir dosyaya yönlendirmek için `>` operatörünü kullanabilirsiniz:
  ```csh
  hexdump dosya.txt > cikti.txt
  ```