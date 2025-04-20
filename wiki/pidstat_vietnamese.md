# [Hệ điều hành] C Shell (csh) pidstat: Theo dõi thông tin sử dụng CPU và bộ nhớ của tiến trình

## Tổng quan
Lệnh `pidstat` được sử dụng để theo dõi và hiển thị thông tin về việc sử dụng CPU và bộ nhớ của các tiến trình đang chạy trên hệ thống. Nó cung cấp cái nhìn sâu sắc về hiệu suất của từng tiến trình, giúp người dùng xác định các vấn đề tiềm ẩn trong việc sử dụng tài nguyên.

## Cú pháp
Cú pháp cơ bản của lệnh `pidstat` như sau:
```
pidstat [options] [arguments]
```

## Các tùy chọn phổ biến
- `-p <pid>`: Theo dõi một tiến trình cụ thể theo ID tiến trình (PID).
- `-r`: Hiển thị thông tin sử dụng bộ nhớ.
- `-u`: Hiển thị thông tin sử dụng CPU.
- `-h`: Hiển thị thông tin theo định dạng dễ đọc hơn.
- `-t`: Theo dõi tất cả các luồng của tiến trình.

## Ví dụ thông dụng
Dưới đây là một số ví dụ về cách sử dụng lệnh `pidstat`:

1. Theo dõi thông tin sử dụng CPU của tất cả các tiến trình:
   ```bash
   pidstat
   ```

2. Theo dõi một tiến trình cụ thể với PID 1234:
   ```bash
   pidstat -p 1234
   ```

3. Hiển thị thông tin sử dụng bộ nhớ:
   ```bash
   pidstat -r
   ```

4. Theo dõi tất cả các luồng của một tiến trình:
   ```bash
   pidstat -t -p 1234
   ```

5. Hiển thị thông tin dễ đọc hơn:
   ```bash
   pidstat -h
   ```

## Mẹo
- Sử dụng `pidstat` kết hợp với các lệnh khác như `grep` để lọc thông tin theo nhu cầu.
- Thực hiện lệnh `pidstat` định kỳ bằng cách sử dụng `watch` để theo dõi sự thay đổi theo thời gian.
- Kiểm tra tài liệu hướng dẫn bằng cách sử dụng `man pidstat` để tìm hiểu thêm về các tùy chọn và cách sử dụng.