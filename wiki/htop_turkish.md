# [Linux] C Shell (csh) htop Kullanımı: Sistem kaynaklarını izlemek için bir araç

## Genel Bakış
htop, sistem kaynaklarını gerçek zamanlı olarak izlemek için kullanılan bir komut satırı aracıdır. Kullanıcı dostu bir arayüze sahip olan htop, CPU, bellek kullanımı ve çalışan işlemler hakkında bilgi sağlar. Ayrıca, işlemleri yönetmek için etkileşimli bir ortam sunar.

## Kullanım
htop komutunun temel sözdizimi aşağıdaki gibidir:

```bash
htop [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-h`, `--help`: Yardım bilgilerini gösterir.
- `-s`, `--sort`: Görüntülenen işlemleri belirtilen kritere göre sıralar.
- `-p`, `--pid`: Belirtilen işlem kimlikleri için htop'u başlatır.
- `-u`, `--user`: Belirtilen kullanıcıya ait işlemleri gösterir.

## Yaygın Örnekler
Aşağıda htop komutunun bazı pratik örnekleri bulunmaktadır:

### 1. Temel htop Kullanımı
```bash
htop
```
Bu komut, htop'un varsayılan görünümünü başlatır ve sistem kaynaklarınızı izlemeye başlarsınız.

### 2. Belirli Bir Kullanıcının İşlemlerini Görüntüleme
```bash
htop -u kullanıcı_adı
```
Bu komut, belirtilen kullanıcının işlemlerini gösterir.

### 3. İşlemleri Belirli Bir Kriterle Sıralama
```bash
htop -s MEM
```
Bu komut, işlemleri bellek kullanımına göre sıralar.

### 4. Belirli İşlem Kimlikleri ile Htop'u Başlatma
```bash
htop -p 1234,5678
```
Bu komut, belirtilen işlem kimliklerine sahip işlemleri görüntüler.

## İpuçları
- htop arayüzünde ok tuşlarıyla gezinerek işlemler arasında geçiş yapabilirsiniz.
- Bir işlemi sonlandırmak için, işlemi seçip `F9` tuşuna basarak kill menüsüne erişebilirsiniz.
- Görünüm ayarlarını değiştirmek için `F2` tuşuna basarak yapılandırma menüsüne girebilirsiniz.