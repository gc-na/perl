# [Hệ điều hành] C Shell (csh) basename <Sử dụng tương đương>: Lấy tên tệp từ đường dẫn

## Overview
Lệnh `basename` trong C Shell (csh) được sử dụng để lấy tên tệp từ một đường dẫn đầy đủ. Nó loại bỏ tất cả các phần của đường dẫn, chỉ để lại tên tệp cuối cùng.

## Usage
Cú pháp cơ bản của lệnh `basename` như sau:
```
basename [options] [arguments]
```

## Common Options
- `-a`: Xử lý nhiều tệp và trả về tên tệp cho từng tệp.
- `-s`: Loại bỏ phần mở rộng được chỉ định từ tên tệp.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `basename`:

1. Lấy tên tệp từ đường dẫn:
   ```csh
   basename /home/user/document.txt
   ```
   Kết quả: `document.txt`

2. Lấy tên tệp từ đường dẫn và loại bỏ phần mở rộng:
   ```csh
   basename /home/user/document.txt .txt
   ```
   Kết quả: `document`

3. Xử lý nhiều tệp:
   ```csh
   basename -a /home/user/file1.txt /home/user/file2.txt
   ```
   Kết quả:
   ```
   file1.txt
   file2.txt
   ```

4. Loại bỏ phần mở rộng từ nhiều tệp:
   ```csh
   basename -s .txt /home/user/file1.txt /home/user/file2.txt
   ```
   Kết quả:
   ```
   file1
   file2
   ```

## Tips
- Sử dụng `basename` khi bạn chỉ cần tên tệp mà không cần biết đường dẫn đầy đủ.
- Kết hợp `basename` với các lệnh khác trong shell để xử lý tệp hiệu quả hơn.
- Hãy chú ý đến phần mở rộng khi sử dụng tùy chọn `-s` để đảm bảo bạn loại bỏ chính xác phần mở rộng mong muốn.