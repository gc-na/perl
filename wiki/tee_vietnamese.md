# [Hệ điều hành] C Shell (csh) tee Cách sử dụng: Ghi và hiển thị đầu ra

## Overview
Lệnh `tee` trong C Shell (csh) được sử dụng để đọc từ đầu vào chuẩn và ghi ra cả đầu ra chuẩn và một hoặc nhiều tệp. Điều này cho phép bạn xem đầu ra của một lệnh trên màn hình trong khi cũng lưu trữ nó vào tệp.

## Usage
Cú pháp cơ bản của lệnh `tee` như sau:
```
tee [options] [arguments]
```

## Common Options
- `-a`: Ghi thêm vào tệp thay vì ghi đè.
- `-i`: Bỏ qua tín hiệu ngắt (interrupt signals).
- `--help`: Hiển thị thông tin trợ giúp về lệnh `tee`.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `tee`:

1. Ghi đầu ra của lệnh `ls` vào tệp `output.txt`:
   ```csh
   ls | tee output.txt
   ```

2. Ghi đầu ra của lệnh `echo` vào tệp `log.txt` và hiển thị trên màn hình:
   ```csh
   echo "Hello, World!" | tee log.txt
   ```

3. Ghi thêm đầu ra của lệnh `df` vào tệp `disk_usage.txt`:
   ```csh
   df | tee -a disk_usage.txt
   ```

4. Sử dụng `tee` để ghi đầu ra của một lệnh phức tạp:
   ```csh
   ps aux | grep httpd | tee httpd_processes.txt
   ```

## Tips
- Sử dụng tùy chọn `-a` khi bạn muốn ghi thêm vào tệp mà không làm mất dữ liệu cũ.
- Kết hợp `tee` với các lệnh khác để theo dõi và ghi lại thông tin trong quá trình thực hiện.
- Kiểm tra nội dung của tệp đã ghi bằng lệnh `cat` để đảm bảo dữ liệu đã được lưu đúng cách.