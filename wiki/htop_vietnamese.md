# [Hệ điều hành] C Shell (csh) htop: [quản lý tiến trình tương tác]

## Tổng quan
Lệnh `htop` là một công cụ mạnh mẽ để theo dõi và quản lý các tiến trình đang chạy trên hệ thống. Nó cung cấp một giao diện người dùng trực quan, cho phép người dùng dễ dàng xem thông tin về CPU, bộ nhớ, và các tiến trình, cũng như thực hiện các thao tác như dừng hoặc thay đổi ưu tiên của tiến trình.

## Cách sử dụng
Cú pháp cơ bản của lệnh `htop` như sau:
```
htop [tùy chọn] [tham số]
```

## Tùy chọn phổ biến
- `-h`, `--help`: Hiển thị thông tin trợ giúp về lệnh `htop`.
- `-C`, `--no-color`: Chạy `htop` mà không có màu sắc.
- `-d`, `--delay`: Đặt độ trễ giữa các bản cập nhật (tính bằng giây).
- `-p`, `--pid`: Chỉ định một hoặc nhiều PID để theo dõi.

## Ví dụ phổ biến
- Chạy `htop` đơn giản:
  ```bash
  htop
  ```

- Chạy `htop` với độ trễ 2 giây:
  ```bash
  htop -d 2
  ```

- Chạy `htop` để theo dõi một tiến trình cụ thể với PID 1234:
  ```bash
  htop -p 1234
  ```

## Mẹo
- Sử dụng phím F3 để tìm kiếm tiến trình theo tên.
- Nhấn F9 để gửi tín hiệu đến tiến trình (ví dụ: dừng hoặc thoát).
- Bạn có thể sắp xếp các tiến trình theo CPU hoặc bộ nhớ bằng cách nhấn vào tiêu đề cột tương ứng.