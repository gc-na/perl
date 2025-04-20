# [לינוקס] C Shell (csh) dig שימוש: קבלת מידע על DNS

## Overview
הפקודה `dig` (Domain Information Groper) משמשת לביצוע שאילתות DNS (Domain Name System). היא מאפשרת למשתמשים לקבל מידע על כתובות IP, רשומות DNS שונות ועוד.

## Usage
הסינטקס הבסיסי של הפקודה הוא:
```
dig [אפשרויות] [ארגומנטים]
```

## Common Options
- `@server` - מציין שרת DNS ספציפי לשאילתא.
- `-t type` - קובע את סוג הרשומה (למשל A, MX, TXT).
- `+short` - מחזיר תוצאה מקוצרת.
- `+trace` - עוקב אחרי כל שלב בשאילתת DNS.

## Common Examples
- **שאילתא על כתובת IP של דומיין:**
  ```csh
  dig example.com
  ```

- **קבלת רשומת MX לדומיין:**
  ```csh
  dig -t MX example.com
  ```

- **שימוש בשרת DNS ספציפי:**
  ```csh
  dig @8.8.8.8 example.com
  ```

- **קבלת תוצאה מקוצרת:**
  ```csh
  dig +short example.com
  ```

- **מעקב אחרי שאילתת DNS:**
  ```csh
  dig +trace example.com
  ```

## Tips
- השתמש באפשרות `+short` כדי לקבל תוצאות מהירות וברורות.
- אם אתה נתקל בבעיות, נסה להשתמש בשרת DNS אחר כמו 8.8.8.8 (Google DNS).
- למידע נוסף על סוגי רשומות DNS, עיין בתיעוד של DNS או השתמש בפקודה `dig -t ANY example.com` כדי לקבל את כל הרשומות.