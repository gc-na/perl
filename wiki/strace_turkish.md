# [Linux] C Shell (csh) strace Kullanımı: Sistem çağrılarını izleme aracı

## Genel Bakış
`strace`, bir programın sistem çağrılarını ve sinyallerini izlemek için kullanılan bir araçtır. Bu komut, bir programın çalışması sırasında hangi sistem çağrılarını yaptığını görmek için oldukça faydalıdır. Hata ayıklama ve performans analizi için yaygın olarak kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
strace [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-c`: Sistem çağrılarının istatistiklerini toplar ve özetler.
- `-e`: Belirli bir sistem çağrısını izlemek için kullanılır. Örneğin, `-e trace=open` yalnızca `open` çağrılarını izler.
- `-o <dosya>`: Çıktıyı belirtilen dosyaya yönlendirir.
- `-p <pid>`: Belirtilen işlem kimliğine (PID) bağlı bir işlemi izler.
- `-f`: Çocuk süreçleri de dahil olmak üzere tüm süreçleri izler.

## Yaygın Örnekler
Aşağıda `strace` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### 1. Basit bir programı izleme
```bash
strace ls
```
Bu komut, `ls` programının çalışması sırasında yaptığı sistem çağrılarını gösterir.

### 2. Çıktıyı bir dosyaya yönlendirme
```bash
strace -o strace_output.txt ls
```
`ls` komutunun sistem çağrılarını `strace_output.txt` dosyasına kaydeder.

### 3. Belirli bir sistem çağrısını izleme
```bash
strace -e trace=open ls
```
Sadece `ls` komutunun `open` sistem çağrılarını izler.

### 4. Bir işlemi izleme
```bash
strace -p 1234
```
PID'si 1234 olan bir işlemi izler.

### 5. İstatistik toplama
```bash
strace -c ls
```
`ls` komutunun sistem çağrılarının istatistiklerini toplar ve özetler.

## İpuçları
- `strace` kullanırken, çıktının çok fazla bilgi içerebileceğini unutmayın. Belirli sistem çağrılarını izlemek için `-e` seçeneğini kullanmak, çıktıyı daha yönetilebilir hale getirebilir.
- Performans sorunlarını analiz ederken, `-c` seçeneği ile istatistik toplamak, hangi sistem çağrılarının en çok zaman aldığını anlamanıza yardımcı olabilir.
- Çıktıyı bir dosyaya yönlendirmek, daha sonra incelemek için faydalı olabilir. Özellikle uzun çıktılarda bu yöntem oldukça kullanışlıdır.