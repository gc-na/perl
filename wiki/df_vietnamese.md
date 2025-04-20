# [Hệ điều hành] C Shell (csh) df Cách sử dụng: Kiểm tra dung lượng đĩa

## Overview
Lệnh `df` trong C Shell (csh) được sử dụng để hiển thị thông tin về dung lượng đĩa của các hệ thống tập tin. Nó cho phép người dùng biết được dung lượng đã sử dụng, dung lượng còn trống và tổng dung lượng của các phân vùng đĩa.

## Usage
Cú pháp cơ bản của lệnh `df` như sau:
```
df [options] [arguments]
```

## Common Options
- `-h`: Hiển thị dung lượng theo định dạng dễ đọc (kilo, mega, giga).
- `-T`: Hiển thị loại hệ thống tập tin.
- `-a`: Hiển thị tất cả các hệ thống tập tin, bao gồm cả những hệ thống không được gắn kết.
- `-i`: Hiển thị thông tin về số lượng inode thay vì dung lượng đĩa.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `df`:

1. Hiển thị thông tin dung lượng đĩa cơ bản:
   ```csh
   df
   ```

2. Hiển thị dung lượng đĩa theo định dạng dễ đọc:
   ```csh
   df -h
   ```

3. Hiển thị loại hệ thống tập tin:
   ```csh
   df -T
   ```

4. Hiển thị thông tin cho tất cả các hệ thống tập tin:
   ```csh
   df -a
   ```

5. Hiển thị thông tin về số lượng inode:
   ```csh
   df -i
   ```

## Tips
- Sử dụng tùy chọn `-h` để dễ dàng đọc và hiểu dung lượng đĩa.
- Kết hợp `df` với lệnh `grep` để tìm kiếm thông tin về một phân vùng cụ thể.
- Thường xuyên kiểm tra dung lượng đĩa để đảm bảo rằng hệ thống của bạn không bị đầy, điều này có thể gây ra sự cố cho các ứng dụng và dịch vụ đang chạy.