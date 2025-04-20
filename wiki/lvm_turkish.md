# [Linux] C Shell (csh) lvm Kullanımı: Disk alanı yönetimi

## Overview
lvm (Logical Volume Manager), Linux sistemlerinde disk alanını yönetmek için kullanılan bir komut ve araçtır. Bu komut, fiziksel diskleri mantıksal hacimlere dönüştürerek daha esnek bir depolama yönetimi sağlar.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```csh
lvm [options] [arguments]
```

## Common Options
- `create`: Yeni bir mantıksal hacim oluşturur.
- `remove`: Var olan bir mantıksal hacmi siler.
- `extend`: Mevcut bir mantıksal hacmin boyutunu artırır.
- `reduce`: Mevcut bir mantıksal hacmin boyutunu azaltır.
- `list`: Mevcut mantıksal hacimleri ve özelliklerini gösterir.

## Common Examples
Aşağıda lvm komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### 1. Yeni Mantıksal Hacim Oluşturma
```csh
lvm create -n my_volume -L 10G my_volume_group
```

### 2. Mantıksal Hacim Silme
```csh
lvm remove my_volume
```

### 3. Mantıksal Hacmi Genişletme
```csh
lvm extend -L +5G my_volume
```

### 4. Mantıksal Hacmi Küçültme
```csh
lvm reduce -L -5G my_volume
```

### 5. Mevcut Mantıksal Hacimleri Listeleme
```csh
lvm list
```

## Tips
- Mantıksal hacimlerle çalışmadan önce mevcut yedeklerinizi almayı unutmayın.
- Hacim boyutlarını değiştirmeden önce dosya sisteminin uygun şekilde küçültüldüğünden emin olun.
- lvm komutlarını çalıştırırken root yetkilerine sahip olduğunuzdan emin olun.