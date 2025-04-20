# [Linux] C Shell (csh) rsync Kullanımı: Dosya senkronizasyonu

## Genel Bakış
rsync, dosyaları ve dizinleri yerel veya uzak sistemler arasında senkronize etmek için kullanılan bir komuttur. Verimli bir şekilde çalışarak yalnızca değişiklikleri aktarır, bu da ağ trafiğini azaltır ve işlem süresini kısaltır.

## Kullanım
rsync komutunun temel sözdizimi aşağıdaki gibidir:

```bash
rsync [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-a`: Arşiv modu; dosyaların tüm özelliklerini (izinler, zaman damgaları vb.) korur.
- `-v`: Ayrıntılı çıktı; işlemin ne yaptığını gösterir.
- `-z`: Verileri sıkıştırarak aktarır, bu da ağ üzerinden daha hızlı transfer sağlar.
- `-r`: Alt dizinlerle birlikte dizinleri kopyalar.
- `--delete`: Hedef dizinde, kaynakta olmayan dosyaları siler.

## Yaygın Örnekler
1. Yerel bir dizinden başka bir dizine dosya kopyalama:
   ```bash
   rsync -av /kaynak/dizin/ /hedef/dizin/
   ```

2. Uzak bir sunucuya dosya gönderme:
   ```bash
   rsync -av /yerel/dosya.txt kullanıcı@sunucu:/uzak/dizin/
   ```

3. Uzak bir sunucudan yerel bir dizine dosya indirme:
   ```bash
   rsync -av kullanıcı@sunucu:/uzak/dosya.txt /yerel/dizin/
   ```

4. Sadece değişiklikleri senkronize etme:
   ```bash
   rsync -av --delete /kaynak/dizin/ /hedef/dizin/
   ```

## İpuçları
- Uzun dosya transferleri sırasında, işlemi durdurmak ve devam ettirmek için `--partial` seçeneğini kullanabilirsiniz.
- Ağ bağlantınızın hızını artırmak için `-z` seçeneğini kullanarak verileri sıkıştırabilirsiniz.
- Büyük veri setleri ile çalışıyorsanız, `--progress` seçeneği ile ilerlemeyi takip edebilirsiniz.