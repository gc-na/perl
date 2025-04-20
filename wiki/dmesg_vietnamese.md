# [Hệ điều hành] C Shell (csh) dmesg Cách sử dụng: Xem thông tin log hệ thống

## Tổng quan
Lệnh `dmesg` được sử dụng để hiển thị thông tin log của kernel, giúp người dùng theo dõi các sự kiện và thông báo từ hệ thống trong quá trình khởi động và hoạt động. Đây là một công cụ hữu ích để chẩn đoán và xử lý sự cố.

## Cách sử dụng
Cú pháp cơ bản của lệnh `dmesg` như sau:
```
dmesg [tùy chọn] [đối số]
```

## Các tùy chọn phổ biến
- `-c`: Xóa thông tin log sau khi hiển thị.
- `-n <mức độ>`: Thiết lập mức độ thông báo mà bạn muốn hiển thị.
- `-T`: Hiển thị thời gian theo định dạng dễ đọc.
- `-f <loại>`: Chỉ hiển thị thông tin log của một loại cụ thể.

## Ví dụ thường gặp
- Hiển thị toàn bộ thông tin log của kernel:
  ```bash
  dmesg
  ```

- Hiển thị thông tin log với thời gian dễ đọc:
  ```bash
  dmesg -T
  ```

- Xóa log sau khi hiển thị:
  ```bash
  dmesg -c
  ```

- Chỉ hiển thị thông tin log với mức độ cảnh báo:
  ```bash
  dmesg -n 1
  ```

## Mẹo
- Sử dụng `dmesg | less` để cuộn qua thông tin log dài một cách dễ dàng.
- Kết hợp `dmesg` với `grep` để tìm kiếm thông tin cụ thể:
  ```bash
  dmesg | grep error
  ```
- Theo dõi log theo thời gian thực bằng cách sử dụng lệnh:
  ```bash
  dmesg --follow
  ```