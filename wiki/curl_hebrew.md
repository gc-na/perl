# [לינוקס] C Shell (csh) curl שימוש: הורדת תוכן מכתובת URL

## Overview
הפקודה `curl` משמשת להורדת תוכן מכתובת URL או לשליחת בקשות HTTP. היא מאפשרת למשתמשים לתקשר עם שרתים באינטרנט ולהוריד קבצים או נתונים בצורה פשוטה ויעילה.

## Usage
הסינטקס הבסיסי של הפקודה הוא:
```
curl [options] [arguments]
```

## Common Options
- `-O`: הורד קובץ ושמור אותו עם השם המקורי שלו.
- `-L`: עקוב אחרי הפניות (redirects).
- `-d`: שלח נתונים עם בקשת POST.
- `-H`: הוסף כותרת לבקשה.
- `-u`: הוסף שם משתמש וסיסמה (authentication).

## Common Examples
- הורדת קובץ מכתובת URL:
  ```csh
  curl -O http://example.com/file.txt
  ```

- שליחת בקשת GET לכתובת URL:
  ```csh
  curl http://example.com
  ```

- שליחת נתונים עם בקשת POST:
  ```csh
  curl -d "name=value" http://example.com/submit
  ```

- עקוב אחרי הפניות:
  ```csh
  curl -L http://example.com
  ```

- הוספת כותרת לבקשה:
  ```csh
  curl -H "Authorization: Bearer token" http://example.com/api
  ```

## Tips
- השתמש באופציה `-O` כדי לשמור קבצים עם השם המקורי שלהם.
- אם אתה מתמודד עם הפניות רבות, השתמש באופציה `-L` כדי להקל על התהליך.
- תמיד בדוק את תוצאות הבקשה שלך כדי לוודא שההורדה או הבקשה הצליחה.