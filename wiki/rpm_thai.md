# [Linux] C Shell (csh) rpm การใช้งาน: คำสั่งจัดการแพ็กเกจ

## Overview
คำสั่ง `rpm` (Red Hat Package Manager) ใช้สำหรับติดตั้ง, อัปเดต, ลบ, และจัดการแพ็กเกจซอฟต์แวร์ในระบบที่ใช้ RPM (Red Hat Package Manager) เช่น Red Hat, CentOS, และ Fedora

## Usage
รูปแบบพื้นฐานของคำสั่ง `rpm` คือ:

```bash
rpm [options] [arguments]
```

## Common Options
- `-i` : ติดตั้งแพ็กเกจ
- `-U` : อัปเดตแพ็กเกจ
- `-e` : ลบแพ็กเกจ
- `-q` : ตรวจสอบแพ็กเกจที่ติดตั้งอยู่
- `-l` : แสดงไฟล์ที่อยู่ในแพ็กเกจ
- `--help` : แสดงข้อมูลช่วยเหลือเกี่ยวกับคำสั่ง

## Common Examples
- ติดตั้งแพ็กเกจ:
    ```bash
    rpm -i package.rpm
    ```

- อัปเดตแพ็กเกจ:
    ```bash
    rpm -U package.rpm
    ```

- ลบแพ็กเกจ:
    ```bash
    rpm -e package_name
    ```

- ตรวจสอบแพ็กเกจที่ติดตั้ง:
    ```bash
    rpm -q package_name
    ```

- แสดงไฟล์ในแพ็กเกจ:
    ```bash
    rpm -ql package_name
    ```

## Tips
- ตรวจสอบความถูกต้องของแพ็กเกจก่อนติดตั้งโดยใช้ `rpm --checksig package.rpm`
- ใช้ `-v` เพื่อแสดงข้อมูลเพิ่มเติมในระหว่างการติดตั้งหรืออัปเดต
- ควรใช้คำสั่ง `yum` หรือ `dnf` สำหรับการจัดการแพ็กเกจในระบบที่รองรับ เนื่องจากจะจัดการการพึ่งพาอาศัยได้ดีกว่า