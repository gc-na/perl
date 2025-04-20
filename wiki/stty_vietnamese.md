# [Hệ điều hành] C Shell (csh) stty: Thiết lập và điều chỉnh các thuộc tính của terminal

## Overview
Lệnh `stty` trong C Shell (csh) được sử dụng để thiết lập và điều chỉnh các thuộc tính của terminal. Nó cho phép người dùng thay đổi các thiết lập như chế độ nhập liệu, các ký tự điều khiển và nhiều tùy chọn khác liên quan đến cách mà terminal hoạt động.

## Usage
Cú pháp cơ bản của lệnh `stty` như sau:
```csh
stty [options] [arguments]
```

## Common Options
Dưới đây là một số tùy chọn phổ biến của lệnh `stty` cùng với giải thích ngắn gọn:

- `-a`: Hiển thị tất cả các thiết lập hiện tại của terminal.
- `-g`: Xuất các thiết lập hiện tại dưới dạng một chuỗi có thể sử dụng để khôi phục.
- `erase <char>`: Thiết lập ký tự xóa (thường là Backspace).
- `kill <char>`: Thiết lập ký tự để xóa dòng (thường là Ctrl + U).
- `intr <char>`: Thiết lập ký tự để ngắt (thường là Ctrl + C).

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `stty`:

1. Hiển thị tất cả các thiết lập hiện tại:
   ```csh
   stty -a
   ```

2. Thiết lập ký tự xóa là Backspace:
   ```csh
   stty erase ^H
   ```

3. Thiết lập ký tự ngắt là Ctrl + C:
   ```csh
   stty intr ^C
   ```

4. Xuất các thiết lập hiện tại để khôi phục sau này:
   ```csh
   stty -g > settings.txt
   ```

5. Khôi phục các thiết lập từ tệp:
   ```csh
   stty `cat settings.txt`
   ```

## Tips
- Khi thay đổi các thiết lập của terminal, hãy cẩn thận để tránh làm mất khả năng sử dụng terminal.
- Sử dụng tùy chọn `-a` để kiểm tra các thiết lập hiện tại trước khi thực hiện thay đổi.
- Lưu các thiết lập quan trọng vào tệp để có thể khôi phục dễ dàng sau này.