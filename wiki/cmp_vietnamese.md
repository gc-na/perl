# [Hệ điều hành] C Shell (csh) cmp <So sánh hai tệp>: So sánh nội dung của hai tệp

## Overview
Lệnh `cmp` trong C Shell (csh) được sử dụng để so sánh nội dung của hai tệp. Nếu hai tệp giống nhau, lệnh sẽ không xuất ra gì; nếu khác nhau, lệnh sẽ chỉ ra vị trí đầu tiên mà chúng khác nhau.

## Usage
Cú pháp cơ bản của lệnh `cmp` như sau:
```
cmp [options] [arguments]
```

## Common Options
- `-l`: Hiển thị vị trí và giá trị byte khác nhau.
- `-s`: Không xuất ra thông tin, chỉ trả về mã thoát.
- `-i <n>`: Bỏ qua n byte đầu tiên trong mỗi tệp.
- `-n <n>`: So sánh chỉ n byte đầu tiên của tệp.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `cmp`:

1. So sánh hai tệp:
   ```bash
   cmp file1.txt file2.txt
   ```

2. So sánh và hiển thị vị trí byte khác nhau:
   ```bash
   cmp -l file1.txt file2.txt
   ```

3. So sánh mà không xuất ra thông tin:
   ```bash
   cmp -s file1.txt file2.txt
   ```

4. So sánh chỉ n byte đầu tiên của hai tệp:
   ```bash
   cmp -n 10 file1.txt file2.txt
   ```

## Tips
- Sử dụng tùy chọn `-s` nếu bạn chỉ cần biết liệu hai tệp có khác nhau hay không mà không cần thông tin chi tiết.
- Khi so sánh các tệp lớn, hãy cân nhắc sử dụng tùy chọn `-n` để chỉ so sánh một phần của tệp nhằm tiết kiệm thời gian.
- Đảm bảo rằng bạn có quyền truy cập vào cả hai tệp trước khi thực hiện lệnh `cmp`.