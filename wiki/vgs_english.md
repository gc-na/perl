# [Linux] C Shell (csh) vgs Uso: Display volume group information

## Overview
The `vgs` command is used to display information about volume groups in a Logical Volume Manager (LVM) setup. It provides a summary of the volume groups available on the system, including details such as the number of logical volumes, physical volumes, and their sizes.

## Usage
The basic syntax of the `vgs` command is as follows:

```bash
vgs [options] [arguments]
```

## Common Options
- `-o`: Specify which columns to display in the output.
- `--units`: Set the units for size output (e.g., k, m, g).
- `-h`: Display output in a human-readable format.
- `-a`: Show all volume groups, including inactive ones.

## Common Examples

1. **Display basic volume group information:**
   ```bash
   vgs
   ```

2. **Show detailed information with specific columns:**
   ```bash
   vgs -o vg_name,lv_count,pv_count,vg_size
   ```

3. **Display information in human-readable format:**
   ```bash
   vgs -h
   ```

4. **Show all volume groups, including inactive ones:**
   ```bash
   vgs -a
   ```

5. **Display volume group information with size in gigabytes:**
   ```bash
   vgs --units g
   ```

## Tips
- Use the `-o` option to customize the output and focus on the information that matters most to you.
- Combine `vgs` with other LVM commands like `lvdisplay` and `pvdisplay` for comprehensive management of your storage.
- Regularly check your volume groups to ensure they have enough space and are functioning correctly.