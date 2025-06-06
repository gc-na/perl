<!--
Meta Description: # تحويل الحروف في Perl باستخدام tr///: الدليل الكامل ## ملخص إن الدالة `tr///` في لغة البرمجة Perl تُستخدم لتحويل مجموعة من الأحرف إلى مجموعة أخرى بشك...
Meta Keywords: الأحرف, text, perl, تحويل, مجموعة
-->

# تحويل الحروف في Perl باستخدام tr///: الدليل الكامل

## ملخص 
إن الدالة `tr///` في لغة البرمجة Perl تُستخدم لتحويل مجموعة من الأحرف إلى مجموعة أخرى بشكل سريع وفعال. تُعتبر هذه الوظيفة أداة قوية لمعالجة النصوص، حيث تُستخدم بشكل شائع لتعديل النصوص أو استبدال الأحرف.

## الوثائق

### الغرض
تُستخدم دالة `tr///` لتحويل أحرف معينة في سلسلة نصية إلى أحرف أخرى. على عكس الدوال الأخرى مثل `s///` التي تستبدل نصًا بنص آخر، فإن `tr///` تركز فقط على تحويل الأحرف.

### الاستخدام
تتمثل الصيغة الأساسية لدالة `tr///` في:
```perl
$string =~ tr/أحرف_المدخلات/أحرف_الإخراج/;
```

حيث:
- `أحرف_المدخلات` هي مجموعة الأحرف التي تريد تحويلها.
- `أحرف_الإخراج` هي مجموعة الأحرف التي سيتم استخدامها بدلاً من الأحرف المدخلة.

### التفاصيل
- عدد الأحرف في `أحرف_المدخلات` يجب أن يتطابق مع عدد الأحرف في `أحرف_الإخراج`. إذا كان عدد الأحرف مختلفًا، سيتم تجاهل الأحرف الزائدة في `أحرف_الإخراج`.
- هذه الدالة تُعيد عدد الأحرف التي تم تحويلها.

## الأمثلة

### مثال 1: تحويل الأحرف
```perl
my $text = "hello world";
$text =~ tr/a-z/A-Z/;
print $text;  # الناتج: "HELLO WORLD"
```

### مثال 2: استبدال أحرف محددة
```perl
my $text = "12345";
$text =~ tr/123/abc/;
print $text;  # الناتج: "abc45"
```

### مثال 3: تحويل الأحرف باستخدام مجموعة من الأحرف
```perl
my $text = "apple";
$text =~ tr/a/e/;
print $text;  # الناتج: "epple"
```

## الشرح
تعتبر `tr///` أداة فعالة، ولكن هناك بعض الأمور التي يجب الانتباه إليها:
- إذا كان لديك حرف في `أحرف_المدخلات` غير موجود في `أحرف_الإخراج`، فلن يحدث أي تغيير لهذا الحرف.
- تأكد من التعامل مع الأحرف الكبيرة والصغيرة بعناية، حيث أن `tr///` ليست حساسة لحالة الأحرف. إذا كنت ترغب في تحويل الأحرف الكبيرة فقط، يجب عليك تحديدها بشكل صحيح.
- لا تدعم `tr///` التعبيرات العادية، لذا عليك استخدام الدالة `s///` إذا كنت بحاجة إلى أنماط أكثر تعقيدًا.

## ملخص بجملة واحدة
تُعتبر دالة `tr///` في Perl وسيلة فعالة لتحويل أحرف نصية بسرعة، مما يجعلها أداة مهمة لمعالجة النصوص.