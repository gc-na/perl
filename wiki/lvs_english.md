# [Unix/Linux] C Shell (csh) lvs uso equivalente: Listar volúmenes lógicos

## Overview
The `lvs` command in C Shell (csh) is used to display information about logical volumes in a Linux environment. It provides a concise overview of the logical volumes managed by the Logical Volume Manager (LVM), including their attributes and status.

## Usage
The basic syntax of the `lvs` command is as follows:

```csh
lvs [options] [arguments]
```

## Common Options
- `-o, --units`: Specify the output format and units for size.
- `-a, --all`: Show all logical volumes, including those that are inactive.
- `-f, --full`: Display full information about each logical volume.
- `-S, --select`: Filter the output based on specific criteria.

## Common Examples
Here are some practical examples of using the `lvs` command:

1. **List all logical volumes:**
   ```csh
   lvs
   ```

2. **Show detailed information about logical volumes:**
   ```csh
   lvs -f
   ```

3. **List logical volumes with specific output columns:**
   ```csh
   lvs -o lv_name,lv_size
   ```

4. **Show all logical volumes, including inactive ones:**
   ```csh
   lvs -a
   ```

5. **Filter logical volumes based on a specific attribute:**
   ```csh
   lvs -S 'lv_size > 10G'
   ```

## Tips
- Always use the `-o` option to customize the output to show only the information you need.
- Combine options for more refined output, such as using `-a` with `-o` to see all volumes with specific attributes.
- Regularly check the status of your logical volumes to ensure they are functioning correctly, especially before performing system maintenance.