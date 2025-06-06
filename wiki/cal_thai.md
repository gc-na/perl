# [ระบบปฏิบัติการ] C Shell (csh) cal การใช้งาน: แสดงปฏิทิน

## Overview
คำสั่ง `cal` ใช้สำหรับแสดงปฏิทินในรูปแบบที่เข้าใจง่าย โดยสามารถแสดงปฏิทินของเดือนหรือปีที่กำหนดได้

## Usage
รูปแบบพื้นฐานของคำสั่งคือ:
```
cal [options] [arguments]
```

## Common Options
- `-m` : แสดงปฏิทินในรูปแบบที่มีการเน้นวันอาทิตย์
- `-y` : แสดงปฏิทินทั้งปี
- `-3` : แสดงปฏิทินของเดือนปัจจุบันและเดือนก่อนหน้าและถัดไป
- `-j` : แสดงวันในปี (วันที่ 1 ถึง 365/366)

## Common Examples
- แสดงปฏิทินของเดือนปัจจุบัน:
  ```csh
  cal
  ```
  
- แสดงปฏิทินของเดือนธันวาคม 2023:
  ```csh
  cal 12 2023
  ```

- แสดงปฏิทินทั้งปี 2023:
  ```csh
  cal -y 2023
  ```

- แสดงปฏิทินของเดือนปัจจุบันและเดือนก่อนหน้าและถัดไป:
  ```csh
  cal -3
  ```

## Tips
- ใช้ `cal -y` เพื่อดูปฏิทินทั้งปีในครั้งเดียว
- หากต้องการดูวันในปี ให้ใช้ `cal -j` เพื่อให้เห็นวันต่างๆ ในปี
- การใช้ `cal` ร่วมกับ `more` หรือ `less` สามารถช่วยให้คุณเลื่อนดูปฏิทินที่ยาวขึ้นได้ง่ายขึ้น