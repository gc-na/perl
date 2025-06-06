# [Linux] C Shell (csh) lsblk การใช้งาน: แสดงข้อมูลบล็อกอุปกรณ์

## Overview
คำสั่ง `lsblk` ใช้เพื่อแสดงรายการอุปกรณ์บล็อกในระบบ เช่น ฮาร์ดดิสก์, พาร์ติชัน, และอุปกรณ์เสริมต่าง ๆ โดยแสดงข้อมูลที่สำคัญเกี่ยวกับอุปกรณ์เหล่านี้ เช่น ขนาด, ประเภท, และสถานะการเชื่อมต่อ

## Usage
รูปแบบพื้นฐานของคำสั่ง `lsblk` มีดังนี้:
```
lsblk [options] [arguments]
```

## Common Options
- `-a` : แสดงอุปกรณ์ทั้งหมด รวมถึงอุปกรณ์ที่ไม่เชื่อมต่อ
- `-f` : แสดงข้อมูลเกี่ยวกับระบบไฟล์
- `-l` : แสดงข้อมูลในรูปแบบรายการ
- `-o` : กำหนดคอลัมน์ที่จะแสดง
- `-p` : แสดงชื่ออุปกรณ์แบบเต็ม

## Common Examples
- แสดงรายการอุปกรณ์บล็อกทั้งหมด:
  ```bash
  lsblk
  ```

- แสดงข้อมูลเกี่ยวกับระบบไฟล์:
  ```bash
  lsblk -f
  ```

- แสดงอุปกรณ์ทั้งหมดรวมถึงอุปกรณ์ที่ไม่เชื่อมต่อ:
  ```bash
  lsblk -a
  ```

- แสดงข้อมูลในรูปแบบรายการ:
  ```bash
  lsblk -l
  ```

- แสดงเฉพาะคอลัมน์ที่ต้องการ เช่น ชื่อ, ขนาด, และประเภท:
  ```bash
  lsblk -o NAME,SIZE,TYPE
  ```

## Tips
- ใช้ `lsblk -f` เพื่อดูข้อมูลระบบไฟล์ที่เชื่อมต่อกับอุปกรณ์บล็อก
- หากต้องการดูข้อมูลในรูปแบบที่เข้าใจง่ายขึ้น สามารถใช้ `lsblk -p` เพื่อแสดงชื่ออุปกรณ์แบบเต็ม
- คำสั่ง `lsblk` สามารถใช้ร่วมกับคำสั่งอื่น ๆ เช่น `grep` เพื่อกรองข้อมูลที่ต้องการได้