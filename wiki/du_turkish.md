# [Linux] C Shell (csh) du Kullanımı: Disk kullanımını gösterir

## Overview
`du` komutu, bir dosya veya dizinin disk alanını nasıl kullandığını gösterir. Bu komut, sistem yöneticileri ve kullanıcılar için disk alanı yönetimini kolaylaştırır.

## Usage
Temel sözdizimi şu şekildedir:

```csh
du [options] [arguments]
```

## Common Options
- `-h`: İnsan tarafından okunabilir formatta boyutları gösterir (örneğin, KB, MB).
- `-s`: Toplam boyutu özetler ve alt dizinleri göstermez.
- `-a`: Tüm dosyaların boyutlarını gösterir, yalnızca dizinler yerine.
- `-c`: Toplam boyutları hesaplar ve en sonunda toplamı gösterir.

## Common Examples
Aşağıda `du` komutunun bazı yaygın kullanımları bulunmaktadır:

1. Belirli bir dizinin disk kullanımını gösterme:
   ```csh
   du /path/to/directory
   ```

2. İnsan tarafından okunabilir formatta disk kullanımını gösterme:
   ```csh
   du -h /path/to/directory
   ```

3. Sadece toplam boyutu gösterme:
   ```csh
   du -sh /path/to/directory
   ```

4. Tüm dosyaların boyutlarını gösterme:
   ```csh
   du -a /path/to/directory
   ```

5. Dizinlerin toplam boyutunu hesaplama:
   ```csh
   du -ch /path/to/directory
   ```

## Tips
- Disk kullanımını analiz ederken, `-h` seçeneğini kullanarak sonuçları daha kolay yorumlayabilirsiniz.
- Büyük dizinlerde işlem yaparken, `-s` seçeneği ile sadece özet bilgileri alarak zaman kazanabilirsiniz.
- `du` komutunu sık sık kullanıyorsanız, belirli dizinler için alias tanımlamak işinizi kolaylaştırabilir.