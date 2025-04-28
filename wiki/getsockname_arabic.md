<!--
Meta Description: # دالة getsockname في Perl: الاستخدامات والتطبيقات ## الملخص دالة `getsockname` في Perl تُستخدم لاسترجاع عنوان الشبكة (IP) ورقم المنفذ (Port) المرتبط ...
Meta Keywords: socket, getsockname, perl, المقبس, address
-->

# دالة getsockname في Perl: الاستخدامات والتطبيقات

## الملخص
دالة `getsockname` في Perl تُستخدم لاسترجاع عنوان الشبكة (IP) ورقم المنفذ (Port) المرتبط بملف المقبس (Socket) المفتوح.

## الوثائق
تُعتبر دالة `getsockname` جزءًا من وحدة `IO::Socket` في Perl، والتي تُستخدم للتعامل مع الشبكات. تهدف هذه الدالة إلى توفير معلومات حول عنوان الشبكة الذي تم من خلاله إنشاء المقبس.

### الغرض
تُستخدم `getsockname` لاسترجاع عنوان الشبكة ورقم المنفذ الخاص بمقبس معين، مما يمكن من معرفة كيفية الوصول إلى الخدمة المستضافة على ذلك المقبس.

### الاستخدام
للاستخدام، يجب أولاً فتح مقبس باستخدام `IO::Socket::INET`، ثم يمكنك استدعاء `getsockname` للحصول على المعلومات المطلوبة.

### التفاصيل
تُستخدم الدالة بالشكل التالي:
```perl
my $address = getsockname($socket);
```
- `$socket`: هو المقبس الذي تم إنشاؤه باستخدام `IO::Socket`.
- `$address`: يحتوي على العنوان ورقم المنفذ الخاص بالمقبس.

## الأمثلة

### مثال 1: استرجاع عنوان IP ورقم المنفذ
```perl
use IO::Socket;

# إنشاء مقبس TCP
my $socket = IO::Socket::INET->new(
    LocalPort => 5000,
    Proto     => 'tcp',
    Listen    => 5
) or die "Could not create socket: $!";

# استرجاع عنوان الشبكة ورقم المنفذ
my $address = getsockname($socket);
print "Socket address: $address\n";
```

### مثال 2: استخدام getsockname مع دالة unpack
```perl
use IO::Socket;

my $socket = IO::Socket::INET->new(
    LocalPort => 6000,
    Proto     => 'udp'
) or die "Could not create socket: $!";

my $address = getsockname($socket);
my ($port, $ip) = unpack_sockaddr_in($address);
print "IP: $ip, Port: $port\n";
```

## الشرح
- **المشاكل الشائعة**: قد يواجه المستخدمون مشاكل في الحصول على المعلومات الصحيحة إذا لم يكن المقبس مفتوحًا أو إذا كان مغلقًا.
- **نقاط يجب الانتباه لها**: من المهم التأكد من أن المقبس قد تم إنشاؤه بنجاح قبل استدعاء `getsockname`. في حال كانت هناك أخطاء، يمكن استخدام `die` للإبلاغ عنها.

## ملخص من سطر واحد
تُستخدم دالة `getsockname` في Perl لاسترجاع عنوان الشبكة ورقم المنفذ من المقبس المفتوح، مما يسهل عملية التعامل مع الشبكات.