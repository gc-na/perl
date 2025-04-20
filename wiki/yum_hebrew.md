# [לינוקס] C Shell (csh) yum שימוש: ניהול חבילות תוכנה

## Overview
הפקודה `yum` (Yellowdog Updater Modified) משמשת לניהול חבילות תוכנה במערכות לינוקס. היא מאפשרת למשתמשים להתקין, לעדכן ולהסיר חבילות בקלות, תוך ניהול תלויות בין חבילות.

## Usage
התחביר הבסיסי של הפקודה הוא:
```
yum [options] [arguments]
```

## Common Options
- `install`: מתקין חבילה חדשה.
- `remove`: מסיר חבילה קיימת.
- `update`: מעדכן חבילה או את כל החבילות המותקנות.
- `search`: מחפש חבילות לפי מילות מפתח.
- `info`: מציג מידע על חבילה מסוימת.

## Common Examples
- התקנת חבילה:
  ```bash
  yum install package_name
  ```

- הסרת חבילה:
  ```bash
  yum remove package_name
  ```

- עדכון חבילה:
  ```bash
  yum update package_name
  ```

- עדכון כל החבילות:
  ```bash
  yum update
  ```

- חיפוש חבילה:
  ```bash
  yum search keyword
  ```

- הצגת מידע על חבילה:
  ```bash
  yum info package_name
  ```

## Tips
- תמיד כדאי לבדוק אם יש עדכונים זמינים לפני התקנה או הסרה של חבילות.
- השתמש באופציה `-y` כדי לאשר אוטומטית את כל הפעולות, לדוגמה: `yum -y update`.
- כדאי לקרוא את המידע על חבילה לפני התקנתה כדי להבין את התלויות שלה.