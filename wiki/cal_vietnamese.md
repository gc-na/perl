# [Hệ điều hành] C Shell (csh) cal <Sử dụng tương đương>: Hiển thị lịch

## Tổng quan
Lệnh `cal` trong C Shell (csh) được sử dụng để hiển thị lịch tháng hoặc năm. Nó cho phép người dùng xem lịch một cách nhanh chóng và dễ dàng từ dòng lệnh.

## Cú pháp
Cú pháp cơ bản của lệnh `cal` như sau:
```
cal [options] [arguments]
```

## Các tùy chọn phổ biến
- `-1`: Hiển thị lịch của tháng hiện tại.
- `-3`: Hiển thị lịch của tháng trước, tháng hiện tại và tháng sau.
- `-y`: Hiển thị lịch của cả năm.
- `-m`: Hiển thị tháng cụ thể (theo số) trong năm.

## Các ví dụ phổ biến
- Hiển thị lịch của tháng hiện tại:
  ```csh
  cal
  ```

- Hiển thị lịch của tháng 5 năm 2023:
  ```csh
  cal 5 2023
  ```

- Hiển thị lịch của cả năm 2023:
  ```csh
  cal -y 2023
  ```

- Hiển thị lịch của tháng trước, tháng hiện tại và tháng sau:
  ```csh
  cal -3
  ```

## Mẹo
- Sử dụng tùy chọn `-m` để chỉ định tháng cụ thể mà bạn muốn xem.
- Kết hợp `cal` với lệnh `grep` để tìm các ngày cụ thể trong lịch.
- Thường xuyên sử dụng `cal` để lên kế hoạch cho các sự kiện hoặc cuộc họp trong tháng.