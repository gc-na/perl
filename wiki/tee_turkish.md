# [Linux] C Shell (csh) tee Kullanımı: Verileri dosyaya yazma ve ekrana yazdırma

## Genel Bakış
`tee` komutu, standart girdi akışını hem bir dosyaya yazmak hem de ekrana (standart çıkış) yazdırmak için kullanılır. Bu, bir komutun çıktısını kaydederken aynı zamanda kullanıcıya da göstermeyi sağlar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
tee [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-a` : Çıktıyı dosyaya ekler (append) yerine dosyayı üzerine yazar.
- `-i` : Kesintileri yok sayar (ignore interrupts).

## Yaygın Örnekler
1. Bir komutun çıktısını bir dosyaya yazarken ekrana da yazdırma:
   ```csh
   ls -l | tee dosya.txt
   ```

2. Çıktıyı bir dosyaya ekleyerek yazdırma:
   ```csh
   echo "Yeni veri" | tee -a dosya.txt
   ```

3. Birden fazla dosyaya yazma:
   ```csh
   echo "Veri" | tee dosya1.txt dosya2.txt
   ```

## İpuçları
- `tee` komutunu, bir komutun çıktısını kaydederken aynı zamanda başka bir işlemde kullanmak için bir boru (pipe) ile birleştirin.
- Çıktıyı kontrol etmek için `cat` komutunu kullanarak dosyanın içeriğini görüntüleyebilirsiniz.
- `-i` seçeneği, komut çalışırken kullanıcıdan gelen kesintileri göz ardı etmek için faydalıdır, böylece işleminiz kesilmez.