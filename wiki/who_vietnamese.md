# [Hệ điều hành] C Shell (csh) who: Xem danh sách người dùng đang đăng nhập

## Overview
Lệnh `who` trong C Shell (csh) được sử dụng để hiển thị danh sách những người dùng đang đăng nhập vào hệ thống. Nó cung cấp thông tin về tên người dùng, thời gian đăng nhập, và thiết bị mà họ đang sử dụng.

## Usage
Cú pháp cơ bản của lệnh `who` như sau:
```
who [options] [arguments]
```

## Common Options
- `-b`: Hiển thị thời gian khởi động của hệ thống.
- `-q`: Chỉ hiển thị danh sách tên người dùng và số lượng người dùng đang đăng nhập.
- `-H`: Hiển thị tiêu đề cho các cột thông tin.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `who`:

1. Hiển thị danh sách người dùng đang đăng nhập:
   ```csh
   who
   ```

2. Hiển thị thời gian khởi động của hệ thống:
   ```csh
   who -b
   ```

3. Hiển thị danh sách tên người dùng và số lượng người dùng:
   ```csh
   who -q
   ```

4. Hiển thị danh sách người dùng với tiêu đề:
   ```csh
   who -H
   ```

## Tips
- Sử dụng lệnh `who` thường xuyên để theo dõi ai đang sử dụng hệ thống của bạn.
- Kết hợp với các lệnh khác như `grep` để lọc thông tin cụ thể về người dùng.
- Nếu bạn cần thông tin chi tiết hơn, hãy xem xét sử dụng lệnh `w`, lệnh này cung cấp thêm thông tin về hoạt động của người dùng.