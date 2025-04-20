# [Hệ điều hành] C Shell (csh) dirname Cách sử dụng: Lấy tên thư mục từ đường dẫn

## Overview
Lệnh `dirname` trong C Shell được sử dụng để trích xuất tên thư mục từ một đường dẫn đầy đủ. Nó giúp người dùng dễ dàng lấy phần thư mục của một đường dẫn mà không cần phải xử lý thủ công.

## Usage
Cú pháp cơ bản của lệnh `dirname` như sau:

```
dirname [options] [arguments]
```

## Common Options
- `-z`: Xuất kết quả dưới dạng chuỗi rỗng nếu đường dẫn không hợp lệ.
- `--help`: Hiển thị thông tin trợ giúp về cách sử dụng lệnh.
- `--version`: Hiển thị phiên bản của lệnh `dirname`.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `dirname`:

1. Lấy tên thư mục từ một đường dẫn đầy đủ:
   ```csh
   dirname /home/user/documents/file.txt
   ```
   Kết quả sẽ là:
   ```
   /home/user/documents
   ```

2. Lấy tên thư mục từ một đường dẫn khác:
   ```csh
   dirname /usr/local/bin/script.sh
   ```
   Kết quả sẽ là:
   ```
   /usr/local/bin
   ```

3. Sử dụng với đường dẫn không có tên tệp:
   ```csh
   dirname /var/log/
   ```
   Kết quả sẽ là:
   ```
   /var/log
   ```

## Tips
- Sử dụng `dirname` trong các kịch bản shell để tự động hóa việc xử lý đường dẫn.
- Kết hợp lệnh `dirname` với các lệnh khác như `basename` để có được cả tên thư mục và tên tệp từ một đường dẫn.
- Đảm bảo rằng đường dẫn bạn cung cấp là hợp lệ để tránh kết quả không mong muốn.