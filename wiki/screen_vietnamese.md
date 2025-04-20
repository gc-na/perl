# [Hệ điều hành] C Shell (csh) screen: Quản lý phiên làm việc trên terminal

## Overview
Lệnh `screen` cho phép người dùng tạo và quản lý nhiều phiên làm việc trong một terminal. Điều này rất hữu ích khi bạn muốn chạy các tác vụ lâu dài mà không cần giữ terminal mở liên tục. Bạn có thể tách rời phiên làm việc và quay lại bất cứ lúc nào.

## Usage
Cú pháp cơ bản của lệnh `screen` như sau:
```
screen [options] [arguments]
```

## Common Options
- `-S <name>`: Đặt tên cho phiên làm việc.
- `-d -r`: Tách rời và khôi phục một phiên làm việc đã bị tách rời.
- `-list`: Liệt kê tất cả các phiên làm việc đang chạy.
- `-h <lines>`: Thiết lập số dòng lịch sử mà `screen` sẽ lưu trữ.

## Common Examples
- Tạo một phiên làm việc mới:
  ```bash
  screen
  ```

- Tạo một phiên với tên cụ thể:
  ```bash
  screen -S mysession
  ```

- Tách rời phiên làm việc:
  Nhấn `Ctrl + A`, sau đó nhấn `D`.

- Khôi phục phiên làm việc đã tách rời:
  ```bash
  screen -r mysession
  ```

- Liệt kê tất cả các phiên làm việc:
  ```bash
  screen -list
  ```

## Tips
- Sử dụng tên phiên để dễ dàng quản lý nhiều phiên làm việc.
- Nhớ lưu lại công việc của bạn trước khi tách rời phiên.
- Thường xuyên kiểm tra các phiên làm việc đang chạy để tránh lãng phí tài nguyên hệ thống.