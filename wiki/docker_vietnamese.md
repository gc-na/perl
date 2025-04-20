# [Hệ điều hành] C Shell (csh) docker cách sử dụng: Quản lý và triển khai container

## Tổng quan
Lệnh `docker` được sử dụng để quản lý và triển khai các container. Docker cho phép người dùng tạo, triển khai và chạy các ứng dụng trong môi trường ảo hóa nhẹ, giúp tăng cường tính nhất quán và khả năng mở rộng.

## Cách sử dụng
Cú pháp cơ bản của lệnh docker như sau:
```
docker [options] [arguments]
```

## Các tùy chọn phổ biến
- `run`: Tạo và chạy một container mới.
- `ps`: Liệt kê các container đang chạy.
- `stop`: Dừng một hoặc nhiều container.
- `rm`: Xóa một hoặc nhiều container.
- `images`: Liệt kê các hình ảnh Docker có sẵn trên hệ thống.

## Ví dụ phổ biến
- Tạo và chạy một container mới từ hình ảnh Ubuntu:
  ```bash
  docker run -it ubuntu
  ```
  
- Liệt kê các container đang chạy:
  ```bash
  docker ps
  ```

- Dừng một container với ID là `abc123`:
  ```bash
  docker stop abc123
  ```

- Xóa một container đã dừng:
  ```bash
  docker rm abc123
  ```

- Liệt kê các hình ảnh Docker có sẵn:
  ```bash
  docker images
  ```

## Mẹo
- Luôn kiểm tra các container đang chạy trước khi thực hiện các thao tác dừng hoặc xóa để tránh mất dữ liệu.
- Sử dụng `docker-compose` để quản lý nhiều container một cách dễ dàng hơn.
- Thường xuyên cập nhật hình ảnh Docker để đảm bảo bạn có các bản vá bảo mật mới nhất.