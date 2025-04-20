# [Hệ điều hành] C Shell (csh) iotop Cách sử dụng: Theo dõi hoạt động I/O của hệ thống

## Overview
Lệnh `iotop` được sử dụng để theo dõi hoạt động I/O (Input/Output) của các tiến trình đang chạy trên hệ thống. Nó cho phép người dùng xem các tiến trình nào đang tiêu tốn tài nguyên I/O, giúp xác định các vấn đề về hiệu suất liên quan đến đĩa.

## Usage
Cú pháp cơ bản của lệnh `iotop` như sau:
```
iotop [options] [arguments]
```

## Common Options
- `-o` hoặc `--only`: Chỉ hiển thị các tiến trình đang sử dụng I/O.
- `-b` hoặc `--batch`: Chạy trong chế độ batch, thích hợp cho việc ghi lại thông tin vào file.
- `-d <seconds>`: Đặt khoảng thời gian giữa các lần cập nhật thông tin (mặc định là 1 giây).
- `-p <pid>`: Theo dõi một tiến trình cụ thể theo ID tiến trình (PID).

## Common Examples
- Để xem hoạt động I/O của tất cả các tiến trình:
  ```bash
  iotop
  ```

- Để chỉ hiển thị các tiến trình đang sử dụng I/O:
  ```bash
  iotop -o
  ```

- Để chạy `iotop` trong chế độ batch và ghi ra file:
  ```bash
  iotop -b -n 10 > iotop_output.txt
  ```

- Để theo dõi một tiến trình cụ thể với PID là 1234:
  ```bash
  iotop -p 1234
  ```

## Tips
- Sử dụng tùy chọn `-o` để chỉ xem các tiến trình đang hoạt động, giúp giảm bớt thông tin không cần thiết.
- Chạy `iotop` với quyền root để có thể xem tất cả các tiến trình, bao gồm cả những tiến trình của người dùng khác.
- Nếu bạn muốn ghi lại thông tin trong một khoảng thời gian dài, hãy sử dụng chế độ batch với tùy chọn `-b` và `-n` để chỉ định số lần cập nhật.