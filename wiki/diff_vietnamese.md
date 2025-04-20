# [Hệ điều hành] C Shell (csh) diff Cách sử dụng: So sánh sự khác biệt giữa các tệp

## Overview
Lệnh `diff` trong C Shell (csh) được sử dụng để so sánh nội dung của hai tệp và hiển thị sự khác biệt giữa chúng. Lệnh này rất hữu ích cho lập trình viên và người dùng khi cần theo dõi các thay đổi trong mã nguồn hoặc tài liệu.

## Usage
Cú pháp cơ bản của lệnh `diff` như sau:
```csh
diff [options] [arguments]
```

## Common Options
- `-u`: Hiển thị sự khác biệt theo định dạng "unified", giúp dễ đọc hơn.
- `-c`: Hiển thị sự khác biệt theo định dạng "context", bao gồm một số dòng ngữ cảnh xung quanh sự khác biệt.
- `-i`: Bỏ qua sự khác biệt về chữ hoa chữ thường.
- `-w`: Bỏ qua sự khác biệt về khoảng trắng.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `diff`:

1. So sánh hai tệp:
   ```csh
   diff file1.txt file2.txt
   ```

2. Hiển thị sự khác biệt theo định dạng unified:
   ```csh
   diff -u file1.txt file2.txt
   ```

3. So sánh hai tệp và bỏ qua sự khác biệt về chữ hoa chữ thường:
   ```csh
   diff -i file1.txt file2.txt
   ```

4. So sánh hai tệp và hiển thị ngữ cảnh:
   ```csh
   diff -c file1.txt file2.txt
   ```

## Tips
- Sử dụng tùy chọn `-u` để có được kết quả dễ đọc hơn, đặc biệt khi làm việc với mã nguồn.
- Kiểm tra sự khác biệt giữa các phiên bản tệp trước khi thực hiện các thay đổi lớn.
- Kết hợp `diff` với các công cụ khác như `patch` để tự động áp dụng các thay đổi.