# [Linux] C Shell (csh) lvextend การขยาย Logical Volume: ขยายขนาดของ Logical Volume

## Overview
คำสั่ง `lvextend` ใช้สำหรับขยายขนาดของ Logical Volume ในระบบจัดการดิสก์ LVM (Logical Volume Manager) ซึ่งช่วยให้ผู้ใช้สามารถเพิ่มพื้นที่เก็บข้อมูลใน Logical Volume ได้ตามต้องการ

## Usage
รูปแบบพื้นฐานของคำสั่ง `lvextend` คือ:

```csh
lvextend [options] [arguments]
```

## Common Options
- `-L +size` : เพิ่มขนาดของ Logical Volume โดยระบุขนาดที่ต้องการเพิ่ม
- `-l +number` : เพิ่ม Logical Extents จำนวนที่ระบุ
- `-r` : ขยายระบบไฟล์โดยอัตโนมัติหลังจากขยาย Logical Volume
- `--resizefs` : ขยายระบบไฟล์หลังจากขยาย Logical Volume (เหมือนกับ `-r`)

## Common Examples
1. ขยาย Logical Volume โดยเพิ่มขนาด 10GB:
   ```csh
   lvextend -L +10G /dev/vg_name/lv_name
   ```

2. ขยาย Logical Volume โดยเพิ่ม 5 Logical Extents:
   ```csh
   lvextend -l +5 /dev/vg_name/lv_name
   ```

3. ขยาย Logical Volume และขยายระบบไฟล์โดยอัตโนมัติ:
   ```csh
   lvextend -r -L +20G /dev/vg_name/lv_name
   ```

4. ขยาย Logical Volume โดยระบุขนาดใหม่เป็น 50GB:
   ```csh
   lvextend -L 50G /dev/vg_name/lv_name
   ```

## Tips
- ตรวจสอบพื้นที่ว่างใน Volume Group ก่อนที่จะขยาย Logical Volume เพื่อให้แน่ใจว่ามีพื้นที่เพียงพอ
- ใช้ตัวเลือก `-r` หรือ `--resizefs` เพื่อทำให้การขยาย Logical Volume และระบบไฟล์เป็นไปโดยอัตโนมัติ
- ควรทำการสำรองข้อมูลก่อนที่จะทำการขยาย Logical Volume เพื่อป้องกันการสูญหายของข้อมูลในกรณีที่เกิดข้อผิดพลาด