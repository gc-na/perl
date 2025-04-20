# [Linux] C Shell (csh) tmux Kullanımı: Terminal çoklu oturum yönetimi

## Genel Bakış
tmux, terminal çoklu oturum yönetimi sağlayan bir araçtır. Kullanıcıların birden fazla terminal oturumunu aynı anda yönetmesine ve bu oturumlar arasında kolayca geçiş yapmasına olanak tanır. tmux, özellikle uzaktan bağlantılarda ve uzun süreli görevlerde oldukça faydalıdır.

## Kullanım
tmux komutunun temel sözdizimi aşağıdaki gibidir:

```bash
tmux [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `new`: Yeni bir tmux oturumu oluşturur.
- `attach`: Var olan bir tmux oturumuna bağlanır.
- `list-sessions`: Mevcut tmux oturumlarını listeler.
- `kill-session`: Belirtilen tmux oturumunu kapatır.

## Yaygın Örnekler
Aşağıda tmux kullanımına dair bazı pratik örnekler bulunmaktadır:

### Yeni Oturum Oluşturma
Yeni bir tmux oturumu oluşturmak için:
```bash
tmux new -s oturum_adı
```

### Mevcut Oturuma Bağlanma
Var olan bir oturuma bağlanmak için:
```bash
tmux attach -t oturum_adı
```

### Oturumları Listeleme
Mevcut tmux oturumlarını görmek için:
```bash
tmux list-sessions
```

### Oturumu Kapatma
Belirli bir oturumu kapatmak için:
```bash
tmux kill-session -t oturum_adı
```

## İpuçları
- tmux oturumlarınızı düzenli tutmak için anlamlı isimler verin.
- Oturumlar arasında geçiş yaparken `Ctrl+b` tuş kombinasyonunu kullanarak hızlıca hareket edebilirsiniz.
- tmux yapılandırma dosyası (`~/.tmux.conf`) oluşturarak kişisel ayarlarınızı kaydedebilirsiniz.