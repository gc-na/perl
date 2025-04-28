<!--
Meta Description: # الدالة getpeername في Perl: كيفية استخدامها وتفاصيلها ## الملخص تُستخدم الدالة `getpeername` في Perl للحصول على عنوان الشبكة الخاص بالعميل المتصل بع...
Meta Keywords: socket, getpeername, عنوان, الشبكة, perl
-->

# الدالة getpeername في Perl: كيفية استخدامها وتفاصيلها

## الملخص
تُستخدم الدالة `getpeername` في Perl للحصول على عنوان الشبكة الخاص بالعميل المتصل بعملية خادم عبر مقبس، مما يسمح للمطورين بالتعامل مع اتصالات الشبكة بشكل أكثر كفاءة.

## الوثائق
تُعتبر `getpeername` دالة متاحة في مكتبة `IO::Socket` في Perl، وتُستخدم لاسترجاع عنوان الشبكة للعميل المتصل بمقبس معين. يعود استخدام هذه الدالة بالفائدة على تطبيقات الشبكة، حيث يمكن معرفة المعلومات المتعلقة بالاتصال، مثل عنوان IP ورقم المنفذ.

### الاستخدام
```perl
use IO::Socket;

# إنشاء مقبس TCP
my $socket = IO::Socket::INET->new(
    LocalAddr => '0.0.0.0',
    LocalPort => 8080,
    Proto     => 'tcp',
    Listen    => SOMAXCONN,
) or die "لم يتمكن من إنشاء المقبس: $!";

# قبول اتصال
my $client_socket = $socket->accept();

# استرجاع عنوان العميل
my $client_address = getpeername($client_socket);
```

### التفاصيل
- **المدخلات**: تأخذ الدالة مقبس كمدخل.
- **المخرجات**: تعيد عنوان الشبكة، والذي يمكن تحويله إلى عنوان IP ورقم منفذ باستخدام الدالات المناسبة مثل `unpack`.
- **التركيب**: تستخدم `getpeername` عادةً في التطبيقات التي تحتاج إلى إجراء اتصالات الشبكة، مثل خوادم الويب أو خدمات الدردشة.

## الأمثلة

### مثال 1: الحصول على عنوان IP ورقم المنفذ للعميل
```perl
use IO::Socket;
use Socket;

my $server = IO::Socket::INET->new(
    LocalAddr => '0.0.0.0',
    LocalPort => 8080,
    Proto     => 'tcp',
    Listen    => 5,
) or die "فشل في إنشاء المقبس: $!";

while (my $client = $server->accept()) {
    my $client_address = getpeername($client);
    my ($port, $ip) = unpack_sockaddr_in($client_address);
    print "تم الاتصال من: " . inet_ntoa($ip) . ":" . $port . "\n";
}
```

### مثال 2: التعامل مع الأخطاء
```perl
use IO::Socket;
use Socket;

my $socket = IO::Socket::INET->new(
    LocalAddr => 'localhost',
    LocalPort => 8080,
    Proto     => 'tcp',
    Listen    => 1,
) or die "فشل في إنشاء المقبس: $!";

my $client_socket = $socket->accept();

# محاولة استرجاع عنوان العميل
my $client_address = getpeername($client_socket) or die "فشل في الحصول على عنوان العميل: $!";
```

## الشرح
من المهم ملاحظة أن `getpeername` قد تفشل في بعض الحالات، مثل عدم وجود اتصال أو إذا تم استخدام المقبس بشكل غير صحيح. يجب دائمًا التحقق من الأخطاء باستخدام `or die` أو أسلوب مشابه للتأكد من أن البرنامج يتعامل مع الأخطاء بشكل مناسب. 

أيضًا، يجب أن يكون المقبس في حالة متصلة؛ وإلا، فإن استدعاء `getpeername` لن يُعيد عنوانًا صالحًا. يُفضل استخدام `accept` للحصول على المقبس المتصل قبل استدعاء `getpeername`.

## ملخص قصير
تساعد دالة `getpeername` في Perl المطورين على استرجاع عنوان الشبكة للعميل المتصل بمقبس، مما يعزز القدرة على إدارة الاتصالات في تطبيقات الشبكة.