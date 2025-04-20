# [Hệ điều hành] C Shell (csh) renice: Thay đổi ưu tiên của tiến trình

## Overview
Lệnh `renice` trong C Shell (csh) được sử dụng để thay đổi mức độ ưu tiên của một hoặc nhiều tiến trình đang chạy. Mức độ ưu tiên này ảnh hưởng đến cách thức hệ thống phân bổ tài nguyên cho các tiến trình, với các giá trị thấp hơn cho thấy ưu tiên cao hơn.

## Usage
Cú pháp cơ bản của lệnh `renice` như sau:

```csh
renice [options] [arguments]
```

## Common Options
- `-n`: Chỉ định mức độ ưu tiên mới.
- `-p`: Chỉ định ID tiến trình (PID) mà bạn muốn thay đổi mức độ ưu tiên.
- `-g`: Thay đổi mức độ ưu tiên cho một nhóm tiến trình.
- `-u`: Thay đổi mức độ ưu tiên cho một người dùng cụ thể.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `renice`:

1. Thay đổi mức độ ưu tiên của một tiến trình với PID 1234 thành 10:
   ```csh
   renice -n 10 -p 1234
   ```

2. Thay đổi mức độ ưu tiên cho tất cả các tiến trình của người dùng "user1" thành 5:
   ```csh
   renice -n 5 -u user1
   ```

3. Thay đổi mức độ ưu tiên cho một nhóm tiến trình với GID 5678 thành 15:
   ```csh
   renice -n 15 -g 5678
   ```

4. Kiểm tra mức độ ưu tiên hiện tại của một tiến trình:
   ```csh
   ps -o pid,pri,ni,comm
   ```

## Tips
- Trước khi thay đổi mức độ ưu tiên, hãy kiểm tra mức độ ưu tiên hiện tại của tiến trình để quyết định xem cần thay đổi hay không.
- Sử dụng `renice` với quyền root để có thể thay đổi mức độ ưu tiên cho các tiến trình của người dùng khác.
- Cẩn thận khi tăng mức độ ưu tiên của một tiến trình, vì điều này có thể ảnh hưởng đến hiệu suất của hệ thống.