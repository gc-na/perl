# [Linux] C Shell (csh) mkdir Kullanımı: Klasör oluşturma komutu

## Overview
`mkdir` komutu, C Shell (csh) ortamında yeni dizinler (klasörler) oluşturmak için kullanılır. Bu komut, kullanıcıların dosya sisteminde düzenli bir yapı kurmasına yardımcı olur.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```csh
mkdir [options] [arguments]
```

## Common Options
- `-p`: Ara dizinleri oluşturur. Yani, belirtilen yol boyunca eksik olan dizinleri de oluşturur.
- `-m`: Oluşturulan dizinin izinlerini belirler. Örneğin, `-m 755` ile dizin 755 izinleriyle oluşturulur.

## Common Examples
Aşağıda `mkdir` komutunun bazı pratik örnekleri verilmiştir:

1. Basit bir dizin oluşturma:
   ```csh
   mkdir yeni_klasor
   ```

2. Birden fazla dizin oluşturma:
   ```csh
   mkdir klasor1 klasor2 klasor3
   ```

3. Ara dizinlerle birlikte dizin oluşturma:
   ```csh
   mkdir -p ana_klasor/alt_klasor
   ```

4. Belirli izinlerle dizin oluşturma:
   ```csh
   mkdir -m 700 gizli_klasor
   ```

## Tips
- Dizin adlarında boşluk kullanıyorsanız, dizin adını tırnak içine almayı unutmayın. Örneğin:
  ```csh
  mkdir "Yeni Klasör"
  ```
- `-p` seçeneğini kullanarak birden fazla seviyede dizin oluşturmak, karmaşık dizin yapıları oluştururken işinizi kolaylaştırır.
- Oluşturduğunuz dizinlerin izinlerini kontrol etmek için `ls -l` komutunu kullanabilirsiniz.