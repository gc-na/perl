# [Hệ điều hành] C Shell (csh) hostnamectl Sử dụng: Quản lý tên máy chủ

## Tổng quan
Lệnh `hostnamectl` được sử dụng để quản lý tên máy chủ của hệ thống. Nó cho phép người dùng xem và thay đổi tên máy chủ, cũng như thông tin liên quan đến máy chủ.

## Cú pháp
Cú pháp cơ bản của lệnh là:
```
hostnamectl [options] [arguments]
```

## Các tùy chọn phổ biến
- `set-hostname`: Đặt tên máy chủ mới.
- `status`: Hiển thị thông tin hiện tại về tên máy chủ và trạng thái.
- `set-icon-name`: Đặt tên biểu tượng cho máy chủ.
- `set-chassis`: Đặt loại khung máy (ví dụ: desktop, laptop).

## Ví dụ thường gặp
- Để xem thông tin hiện tại về tên máy chủ:
  ```csh
  hostnamectl status
  ```

- Để thay đổi tên máy chủ thành "my-new-host":
  ```csh
  hostnamectl set-hostname my-new-host
  ```

- Để đặt tên biểu tượng cho máy chủ là "desktop":
  ```csh
  hostnamectl set-icon-name desktop
  ```

- Để đặt loại khung máy là "laptop":
  ```csh
  hostnamectl set-chassis laptop
  ```

## Mẹo
- Luôn kiểm tra thông tin hiện tại trước khi thay đổi tên máy chủ để tránh nhầm lẫn.
- Sử dụng quyền quản trị (root) khi thực hiện các thay đổi để đảm bảo lệnh hoạt động chính xác.
- Sau khi thay đổi tên máy chủ, hãy khởi động lại dịch vụ mạng để áp dụng thay đổi.