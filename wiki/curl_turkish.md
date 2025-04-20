# [Linux] C Shell (csh) curl Kullanımı: HTTP istekleri yapmak için kullanılan bir komut

## Genel Bakış
`curl`, URL'ler üzerinden veri transferi yapmak için kullanılan bir komuttur. Genellikle HTTP, HTTPS, FTP gibi protokollerle çalışır ve web sunucularına istek göndermek veya dosya indirmek için kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
curl [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-O`: İndirilen dosyayı, URL'deki dosya adıyla kaydeder.
- `-L`: Yönlendirmeleri takip eder.
- `-d`: POST isteği ile veri gönderir.
- `-H`: Özel başlıklar ekler.
- `-u`: Temel kimlik doğrulaması için kullanıcı adı ve şifre belirtir.

## Yaygın Örnekler
Aşağıda `curl` komutunun bazı pratik örnekleri bulunmaktadır:

### 1. Basit bir GET isteği
```bash
curl http://example.com
```

### 2. Dosya indirme
```bash
curl -O http://example.com/dosya.zip
```

### 3. POST isteği ile veri gönderme
```bash
curl -d "param1=değer1&param2=değer2" http://example.com/api
```

### 4. Yönlendirmeleri takip etme
```bash
curl -L http://example.com
```

### 5. Özel başlık ekleme
```bash
curl -H "Authorization: Bearer token" http://example.com/api
```

## İpuçları
- `curl` ile birlikte `-v` seçeneğini kullanarak isteğin ayrıntılı çıktısını görebilirsiniz. Bu, hata ayıklama için faydalıdır.
- İndirdiğiniz dosyaların adını değiştirmek istemiyorsanız, `-O` seçeneğini kullanmayı unutmayın.
- Güvenlik gereksinimleri için HTTPS kullanmak her zaman daha iyidir.