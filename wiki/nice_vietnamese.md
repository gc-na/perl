# [Hệ điều hành] C Shell (csh) nice: Thay đổi độ ưu tiên của tiến trình

## Overview
Lệnh `nice` trong C Shell (csh) được sử dụng để thay đổi độ ưu tiên của một tiến trình khi nó được thực thi. Điều này cho phép người dùng điều chỉnh mức độ tài nguyên hệ thống mà tiến trình đó sẽ sử dụng, từ đó giúp quản lý hiệu suất của hệ thống tốt hơn.

## Usage
Cú pháp cơ bản của lệnh `nice` như sau:
```
nice [options] [arguments]
```

## Common Options
- `-n <value>`: Chỉ định giá trị độ ưu tiên mới cho tiến trình. Giá trị này có thể từ -20 (ưu tiên cao nhất) đến 19 (ưu tiên thấp nhất).
- `-h`: Hiển thị thông tin trợ giúp về cách sử dụng lệnh.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `nice`:

1. **Chạy một tiến trình với độ ưu tiên thấp hơn:**
   ```csh
   nice -n 10 ./my_script.sh
   ```

2. **Chạy một tiến trình với độ ưu tiên cao hơn:**
   ```csh
   nice -n -5 ./my_heavy_task
   ```

3. **Kiểm tra độ ưu tiên của một tiến trình đang chạy:**
   ```csh
   ps -o pid,ni,cmd
   ```

4. **Chạy một lệnh với độ ưu tiên mặc định:**
   ```csh
   nice ./my_program
   ```

## Tips
- Sử dụng giá trị độ ưu tiên hợp lý để tránh làm ảnh hưởng đến các tiến trình quan trọng khác trong hệ thống.
- Kiểm tra độ ưu tiên của tiến trình bằng lệnh `ps` để đảm bảo rằng bạn đã thiết lập đúng.
- Lưu ý rằng chỉ người dùng có quyền cao hơn mới có thể tăng độ ưu tiên của tiến trình (giá trị âm).