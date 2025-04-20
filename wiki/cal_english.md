# [Unix] C Shell (csh) cal Uso: Display a calendar

## Overview
The `cal` command in C Shell (csh) is used to display a calendar in the terminal. It can show the current month, a specific month, or an entire year, making it a handy tool for quick date reference.

## Usage
The basic syntax of the `cal` command is as follows:

```
cal [options] [arguments]
```

## Common Options
- `-m`: Start the week on Monday instead of Sunday.
- `-y`: Display the calendar for the current year.
- `-3`: Show the previous, current, and next month.
- `-j`: Display Julian dates (day of the year).
- `-A [num]`: Show the next [num] months after the current month.
- `-B [num]`: Show the previous [num] months before the current month.

## Common Examples
Here are some practical examples of using the `cal` command:

1. **Display the current month:**
   ```csh
   cal
   ```

2. **Display a specific month and year (e.g., December 2023):**
   ```csh
   cal 12 2023
   ```

3. **Display the entire year (e.g., 2023):**
   ```csh
   cal 2023
   ```

4. **Show the previous, current, and next month:**
   ```csh
   cal -3
   ```

5. **Display the calendar for the current year with Julian dates:**
   ```csh
   cal -y -j
   ```

## Tips
- Use the `-A` and `-B` options to quickly navigate through months when planning events.
- Combine options for more customized views, such as `cal -m -3` to start the week on Monday and show three months.
- Remember that `cal` displays the calendar in a simple format, making it easy to read at a glance.