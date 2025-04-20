# [Linux] C Shell (csh) shift Kullanımı: Argümanları sola kaydırma

## Overview
`shift` komutu, C Shell (csh) ortamında, komut satırında tanımlı olan argümanları sola kaydırmak için kullanılır. Bu, argümanların sırasını değiştirmek ve belirli bir argümanı işlemek için yararlıdır.

## Usage
Temel sözdizimi şu şekildedir:

```csh
shift [options] [arguments]
```

## Common Options
- `n`: Argümanları `n` kadar sola kaydırır. Eğer `n` belirtilmezse, varsayılan olarak 1 kaydırma yapılır.

## Common Examples

### Örnek 1: Basit Shift
Aşağıdaki komut, argümanları bir kez sola kaydırır.

```csh
set arg1 = "bir"
set arg2 = "iki"
set arg3 = "üç"
echo $arg1 $arg2 $arg3
shift
echo $arg1 $arg2 $arg3
```

Çıktı:
```
bir iki üç
iki üç
```

### Örnek 2: Çoklu Shift
Bu örnekte, argümanları iki kez sola kaydırıyoruz.

```csh
set arg1 = "elma"
set arg2 = "armut"
set arg3 = "muz"
echo $arg1 $arg2 $arg3
shift 2
echo $arg1 $arg2 $arg3
```

Çıktı:
```
elma armut muz
muz
```

### Örnek 3: Argümanları İşleme
`shift` komutunu bir döngü içinde kullanarak argümanları sırayla işleyebiliriz.

```csh
set args = ("bir" "iki" "üç" "dört")
while ($#args > 0)
    echo "İşlenen argüman: $args[1]"
    shift
end
```

Çıktı:
```
İşlenen argüman: bir
İşlenen argüman: iki
İşlenen argüman: üç
İşlenen argüman: dört
```

## Tips
- `shift` komutunu kullanmadan önce argüman sayısını kontrol etmek için `$#` değişkenini kullanabilirsiniz.
- Argümanları kaydırdıktan sonra, işlemek istediğiniz argümanların doğru sırada olduğundan emin olun.
- `shift` komutunu döngülerle birleştirerek, argümanları daha etkili bir şekilde işleyebilirsiniz.