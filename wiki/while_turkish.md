# [Linux] C Shell (csh) while kullanımı: Döngüsel işlemler gerçekleştirme

## Overview
`while` komutu, belirli bir koşul doğru olduğu sürece sürekli olarak bir komut veya komutlar grubunu çalıştırmak için kullanılır. Bu, döngüsel işlemler gerçekleştirmek için oldukça yararlıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```csh
while (koşul)
    komutlar
end
```

## Common Options
`while` komutunun kendine özgü seçenekleri yoktur, ancak koşul ifadesi için kullanılabilecek bazı operatörler vardır:
- `==` : Eşitlik kontrolü.
- `!=` : Eşitsizlik kontrolü.
- `-lt` : Küçükse.
- `-gt` : Büyüksa.
- `-le` : Küçük veya eşitse.
- `-ge` : Büyük veya eşitse.

## Common Examples

### Örnek 1: Basit bir döngü
Aşağıdaki örnekte, `i` değişkeni 1'den 5'e kadar olan sayıları yazdırır.

```csh
set i = 1
while ($i <= 5)
    echo $i
    @ i++
end
```

### Örnek 2: Kullanıcıdan girdi alma
Bu örnekte, kullanıcı "exit" yazana kadar sürekli olarak bir mesaj gösterilir.

```csh
set input = ""
while ($input != "exit")
    echo "Bir şey yazın (çıkmak için 'exit' yazın):"
    set input = $< 
end
```

### Örnek 3: Dosya kontrolü
Bu örnek, belirli bir dosyanın varlığını kontrol eder ve dosya mevcut olduğu sürece bir mesaj gösterir.

```csh
set filename = "test.txt"
while (-e $filename)
    echo "$filename dosyası mevcut."
    sleep 5
end
```

## Tips
- `while` döngülerini kullanırken, koşulun her zaman doğru bir şekilde güncellendiğinden emin olun; aksi takdirde sonsuz döngüye girebilirsiniz.
- Döngü içinde karmaşık işlemler yapıyorsanız, kodun okunabilirliğini artırmak için komutları ayrı bir dosyaya yazıp çağırmayı düşünebilirsiniz.
- Performans açısından, döngü içinde gereksiz yere işlem yapmaktan kaçının; mümkünse döngü koşulunu en başta kontrol edin.