# [Linux] C Shell (csh) udevadm การใช้งาน: คำสั่งสำหรับจัดการอุปกรณ์ในระบบ

## Overview
คำสั่ง `udevadm` ใช้สำหรับจัดการและตรวจสอบอุปกรณ์ในระบบ Linux โดยเฉพาะการจัดการกับ udev ซึ่งเป็นระบบที่ใช้ในการจัดการอุปกรณ์ที่เชื่อมต่อกับเครื่องคอมพิวเตอร์

## Usage
รูปแบบพื้นฐานของคำสั่ง `udevadm` คือ:

```
udevadm [options] [arguments]
```

## Common Options
- `info` : แสดงข้อมูลเกี่ยวกับอุปกรณ์
- `trigger` : กระตุ้นให้ udev สร้างอุปกรณ์ใหม่
- `settle` : รอให้ udev จัดการอุปกรณ์ทั้งหมดเสร็จสิ้น
- `control` : ควบคุมการทำงานของ udev daemon

## Common Examples
1. แสดงข้อมูลเกี่ยวกับอุปกรณ์:
   ```bash
   udevadm info --query=all --name=/dev/sda
   ```

2. กระตุ้นให้ udev สร้างอุปกรณ์ใหม่:
   ```bash
   udevadm trigger
   ```

3. รอให้ udev จัดการอุปกรณ์ทั้งหมดเสร็จสิ้น:
   ```bash
   udevadm settle
   ```

4. ควบคุมการทำงานของ udev daemon:
   ```bash
   udevadm control --reload-rules
   ```

## Tips
- ใช้ `udevadm info` เพื่อค้นหาข้อมูลที่เฉพาะเจาะจงเกี่ยวกับอุปกรณ์ที่คุณสนใจ
- ควรใช้ `udevadm trigger` หลังจากที่คุณได้เปลี่ยนแปลงกฎของ udev เพื่อให้การเปลี่ยนแปลงมีผล
- ตรวจสอบสถานะของ udev daemon ด้วยคำสั่ง `udevadm control --status` เพื่อให้แน่ใจว่าทำงานอย่างถูกต้อง