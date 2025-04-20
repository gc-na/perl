# [Hệ điều hành] C Shell (csh) cp <Sao chép tệp tin>: Lệnh sao chép tệp tin và thư mục

## Overview
Lệnh `cp` trong C Shell (csh) được sử dụng để sao chép tệp tin và thư mục từ vị trí này sang vị trí khác. Đây là một trong những lệnh cơ bản và quan trọng trong việc quản lý tệp tin trên hệ thống Unix/Linux.

## Usage
Cú pháp cơ bản của lệnh `cp` như sau:
```csh
cp [options] [arguments]
```

## Common Options
- `-i`: Yêu cầu xác nhận trước khi ghi đè lên tệp tin đã tồn tại.
- `-r`: Sao chép thư mục và tất cả các tệp tin bên trong nó (recursive).
- `-u`: Chỉ sao chép tệp tin nếu tệp nguồn mới hơn tệp đích hoặc nếu tệp đích không tồn tại.
- `-v`: Hiển thị thông tin chi tiết về các tệp tin đang được sao chép.

## Common Examples
- Sao chép một tệp tin:
```csh
cp file1.txt file2.txt
```

- Sao chép một thư mục cùng với tất cả các tệp tin bên trong:
```csh
cp -r myfolder/ myfolder_backup/
```

- Sao chép tệp tin và yêu cầu xác nhận nếu tệp đích đã tồn tại:
```csh
cp -i file1.txt file2.txt
```

- Sao chép tệp tin và hiển thị quá trình sao chép:
```csh
cp -v file1.txt file2.txt
```

## Tips
- Luôn sử dụng tùy chọn `-i` khi sao chép tệp tin quan trọng để tránh ghi đè không mong muốn.
- Khi sao chép thư mục lớn, hãy sử dụng tùy chọn `-r` để đảm bảo tất cả các tệp tin con được sao chép.
- Kiểm tra quyền truy cập của tệp tin trước khi sao chép để đảm bảo bạn có quyền thực hiện thao tác này.