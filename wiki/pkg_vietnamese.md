# [Hệ điều hành] C Shell (csh) pkg: Quản lý gói phần mềm

## Tổng quan
Lệnh `pkg` trong C Shell (csh) được sử dụng để quản lý các gói phần mềm trên hệ thống. Nó cho phép người dùng cài đặt, gỡ bỏ và quản lý các gói phần mềm một cách dễ dàng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `pkg` như sau:

```
pkg [options] [arguments]
```

## Tùy chọn phổ biến
- `install`: Cài đặt một gói phần mềm.
- `remove`: Gỡ bỏ một gói phần mềm.
- `list`: Liệt kê các gói đã cài đặt.
- `update`: Cập nhật các gói phần mềm đã cài đặt.

## Ví dụ thường gặp
- Cài đặt một gói phần mềm:
  ```csh
  pkg install tên-gói
  ```

- Gỡ bỏ một gói phần mềm:
  ```csh
  pkg remove tên-gói
  ```

- Liệt kê các gói đã cài đặt:
  ```csh
  pkg list
  ```

- Cập nhật các gói phần mềm:
  ```csh
  pkg update
  ```

## Mẹo
- Luôn kiểm tra các gói đã cài đặt trước khi gỡ bỏ để tránh xóa nhầm.
- Sử dụng tùy chọn `-y` để tự động xác nhận khi cài đặt hoặc gỡ bỏ gói.
- Đọc tài liệu hướng dẫn của từng gói để hiểu rõ hơn về chức năng và cách sử dụng của chúng.