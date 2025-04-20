# [نظام التشغيل] C Shell (csh) helm الاستخدام: إدارة الحزم في Kubernetes

## Overview
أمر `helm` هو أداة لإدارة الحزم في Kubernetes، حيث يساعد المستخدمين في تثبيت وتحديث وإدارة التطبيقات على الكلاود بطريقة سهلة وفعالة.

## Usage
يمكن استخدام الأمر `helm` مع الصيغة الأساسية التالية:

```csh
helm [options] [arguments]
```

## Common Options
- `install`: لتثبيت حزمة جديدة.
- `upgrade`: لترقية حزمة موجودة.
- `uninstall`: لإزالة حزمة.
- `list`: لعرض الحزم المثبتة.
- `repo`: لإدارة مستودعات الحزم.

## Common Examples
- لتثبيت حزمة جديدة:
```csh
helm install my-release my-chart
```

- لترقية حزمة موجودة:
```csh
helm upgrade my-release my-chart
```

- لإزالة حزمة:
```csh
helm uninstall my-release
```

- لعرض الحزم المثبتة:
```csh
helm list
```

- لإضافة مستودع جديد:
```csh
helm repo add my-repo https://example.com/charts
```

## Tips
- تأكد من تحديث مستودعات الحزم بانتظام باستخدام `helm repo update`.
- استخدم `--dry-run` قبل تثبيت أو ترقية الحزم للتحقق من التغييرات دون تنفيذها.
- اقرأ الوثائق الخاصة بكل حزمة للحصول على معلومات دقيقة حول الخيارات المتاحة.