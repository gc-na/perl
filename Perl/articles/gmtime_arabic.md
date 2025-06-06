<!--
Meta Description: # gmtime في Perl: الاستخدام والأهمية ## ملخص الدالة `gmtime` في Perl تُستخدم لتحويل الوقت بالتنسيق الزمني (Unix timestamp) إلى تنسيق الوقت العالمي (UT...
Meta Keywords: gmtime, gmt_time, الوقت, array, السنة
-->

# gmtime في Perl: الاستخدام والأهمية

## ملخص
الدالة `gmtime` في Perl تُستخدم لتحويل الوقت بالتنسيق الزمني (Unix timestamp) إلى تنسيق الوقت العالمي (UTC)، مما يسمح للمطورين بمعالجة التواريخ والأوقات بطريقة دقيقة.

## الوثائق
### الغرض
تقدم دالة `gmtime` وسيلة لتفسير الوقت الذي يُعبر عنه بعدد الثواني منذ 1 يناير 1970 (توقيت Unix) وتحويله إلى مصفوفة تحتوي على مكونات الوقت (الساعة، والدقيقة، والثانية، واليوم، والشهر، والسنة) بالتوقيت العالمي.

### الاستخدام
تُستخدم الدالة `gmtime` بالشكل التالي:
```perl
gmtime($epoch_time);
```
حيث `$epoch_time` هو عدد الثواني منذ 1 يناير 1970.

### التفاصيل
- تعيد الدالة `gmtime` مصفوفة تحتوي على مكونات الوقت التالية:
  - `$array[0]` - الثانية (0-59)
  - `$array[1]` - الدقيقة (0-59)
  - `$array[2]` - الساعة (0-23)
  - `$array[3]` - اليوم (1-31)
  - `$array[4]` - الشهر (0-11، حيث 0 هو يناير)
  - `$array[5]` - السنة (السنة الحالية - 1900)
  - `$array[6]` - اليوم في الأسبوع (0-6، حيث 0 هو الأحد)
  - `$array[7]` - اليوم في السنة (0-365)
  - `$array[8]` - التوقيت الصيفي (0 أو 1)

## الأمثلة
### المثال 1: تحويل الوقت الحالي
```perl
my $current_time = time();
my @gmt_time = gmtime($current_time);
print "الوقت بالتوقيت العالمي: $gmt_time[2]:$gmt_time[1]:$gmt_time[0] يوم $gmt_time[3] في الشهر " . ($gmt_time[4] + 1) . " من السنة " . ($gmt_time[5] + 1900);
```

### المثال 2: تحويل تاريخ محدد
```perl
my $specific_time = 1672531199;  # يمثل 31 ديسمبر 2022
my @gmt_time = gmtime($specific_time);
print "التاريخ بالتوقيت العالمي: $gmt_time[3]/$gmt_time[4]/" . ($gmt_time[5] + 1900);
```

## الشرح
### الأخطاء الشائعة
- **تداخل مع `localtime`**: من المهم ملاحظة الفرق بين `gmtime` و `localtime`. `gmtime` تُعيد الوقت بالتوقيت العالمي، بينما `localtime` تُعيد الوقت بالتوقيت المحلي.
- **التعامل مع السنة**: يجب الانتباه إلى أن السنة التي تُعيدها `gmtime` هي السنة الحالية ناقص 1900، مما يعني أنه يجب إضافة 1900 للحصول على السنة الكاملة.

### ملاحظات إضافية
- تكون النتيجة من `gmtime` مصفوفة، لذا يجب استخدام المؤشرات المناسبة للوصول إلى العناصر المطلوبة.
- يُفضل استخدام `gmtime` عند الحاجة إلى التوقيت العالمي، خاصة في التطبيقات التي تتطلب التنسيق الزمني الدولي.

## ملخص بجملة واحدة
تُستخدم دالة `gmtime` في Perl لتحويل توقيت Unix إلى تنسيق الوقت العالمي الذي يُسهل التعامل مع التواريخ والأوقات بدقة.