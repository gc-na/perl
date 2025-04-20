# [Hệ điều hành Linux] C Shell (csh) yum cách sử dụng: Quản lý gói phần mềm

## Tổng quan
Lệnh `yum` (Yellowdog Updater, Modified) là một công cụ quản lý gói phần mềm trên các hệ điều hành dựa trên RPM (Red Hat Package Manager). Nó giúp người dùng cài đặt, cập nhật và gỡ bỏ các gói phần mềm một cách dễ dàng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `yum` như sau:
```
yum [options] [arguments]
```

## Các tùy chọn phổ biến
- `install`: Cài đặt một gói phần mềm.
- `remove`: Gỡ bỏ một gói phần mềm.
- `update`: Cập nhật gói phần mềm đã cài đặt.
- `list`: Liệt kê các gói phần mềm có sẵn hoặc đã cài đặt.
- `search`: Tìm kiếm gói phần mềm theo tên hoặc mô tả.

## Ví dụ phổ biến
- Cài đặt một gói phần mềm:
  ```bash
  yum install httpd
  ```
- Gỡ bỏ một gói phần mềm:
  ```bash
  yum remove httpd
  ```
- Cập nhật tất cả các gói phần mềm:
  ```bash
  yum update
  ```
- Liệt kê tất cả các gói đã cài đặt:
  ```bash
  yum list installed
  ```
- Tìm kiếm một gói phần mềm:
  ```bash
  yum search nginx
  ```

## Mẹo
- Luôn chạy `yum update` thường xuyên để đảm bảo hệ thống của bạn được cập nhật với các bản vá bảo mật mới nhất.
- Sử dụng `yum clean all` để xóa bộ nhớ cache và giải phóng không gian đĩa.
- Kiểm tra các gói phụ thuộc trước khi cài đặt để tránh xung đột.