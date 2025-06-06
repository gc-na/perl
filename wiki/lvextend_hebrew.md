# [לינוקס] C Shell (csh) lvextend שימוש: הגדלת גודל מחיצות לוגיות

## Overview
הפקודה `lvextend` משמשת להגדלת גודל מחיצות לוגיות במערכות קבצים בלינוקס. היא מאפשרת למשתמש להרחיב את שטח האחסון של מחיצה לוגית קיימת, מה שמסייע בניהול טוב יותר של משאבי האחסון.

## Usage
התחביר הבסיסי של הפקודה הוא:
```
lvextend [options] [arguments]
```

## Common Options
- `-L +size`: מגדיל את גודל המחיצה ב-size (למשל, `+10G` להוספת 10 גיגה-בייט).
- `-l +size`: מגדיל את גודל המחיצה במספר לוגיים (למשל, `+100` להוספת 100 לוגיים).
- `-r`: מבצע הרחבה של מערכת הקבצים באופן אוטומטי לאחר הרחבת המחיצה.

## Common Examples
- להגדיל מחיצה לוגית ב-10 גיגה-בייט:
  ```bash
  lvextend -L +10G /dev/vg_name/lv_name
  ```

- להגדיל מחיצה לוגית ב-100 לוגיים:
  ```bash
  lvextend -l +100 /dev/vg_name/lv_name
  ```

- להגדיל מחיצה לוגית ב-5 גיגה-בייט ולהרחיב את מערכת הקבצים אוטומטית:
  ```bash
  lvextend -L +5G -r /dev/vg_name/lv_name
  ```

## Tips
- תמיד גבה את הנתונים שלך לפני ביצוע שינויים במערכות קבצים.
- השתמש באופציה `-r` כדי לחסוך זמן על ידי הרחבת מערכת הקבצים מיד לאחר הרחבת המחיצה.
- בדוק את מצב המחיצות שלך לאחר השינויים כדי לוודא שהכל מתפקד כראוי.