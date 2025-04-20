# [Linux] C Shell (csh) basename Kullanımı: Dosya adlarını ayıklama

## Overview
`basename` komutu, bir dosya yolundan dosya adını ayıklamak için kullanılır. Bu komut, genellikle dosya yollarını işlemek ve sadece dosya adını elde etmek için faydalıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```csh
basename [options] [arguments]
```

## Common Options
- `-a`: Birden fazla dosya adı verirken, her birini ayrı ayrı işler.
- `-s`: Belirtilen bir uzantıyı dosya adından kaldırır.

## Common Examples
Aşağıda `basename` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### Örnek 1: Basit Kullanım
Bir dosya yolundan sadece dosya adını almak için:

```csh
basename /home/kullanici/dosya.txt
```
Çıktı:
```
dosya.txt
```

### Örnek 2: Uzantıyı Kaldırma
Bir dosya adından uzantıyı kaldırmak için:

```csh
basename /home/kullanici/dosya.txt .txt
```
Çıktı:
```
dosya
```

### Örnek 3: Birden Fazla Dosya Adı İşleme
Birden fazla dosya adı vererek işlem yapmak için:

```csh
basename -a /home/kullanici/dosya1.txt /home/kullanici/dosya2.txt
```
Çıktı:
```
dosya1.txt
dosya2.txt
```

## Tips
- `basename` komutunu, dosya adlarını işlemek için bir betik yazarken kullanışlı hale getirebilirsiniz.
- Uzantıları kaldırmak için `-s` seçeneğini kullanarak dosya adlarını daha temiz bir şekilde elde edebilirsiniz.
- Birden fazla dosya ile çalışırken `-a` seçeneğini kullanarak işlemleri hızlandırabilirsiniz.