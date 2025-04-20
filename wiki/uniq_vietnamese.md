# [Hệ điều hành] C Shell (csh) uniq Cách sử dụng: Loại bỏ các dòng trùng lặp trong tệp

## Overview
Lệnh `uniq` trong C Shell (csh) được sử dụng để loại bỏ các dòng trùng lặp liên tiếp trong một tệp hoặc từ đầu ra của một lệnh. Điều này rất hữu ích khi bạn muốn làm sạch dữ liệu hoặc chỉ cần giữ lại các dòng duy nhất.

## Usage
Cú pháp cơ bản của lệnh `uniq` như sau:
```
uniq [options] [arguments]
```

## Common Options
- `-c`: Đếm số lần xuất hiện của mỗi dòng.
- `-d`: Chỉ hiển thị các dòng trùng lặp.
- `-u`: Chỉ hiển thị các dòng duy nhất.
- `-i`: Bỏ qua sự khác biệt giữa chữ hoa và chữ thường.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `uniq`:

1. **Loại bỏ các dòng trùng lặp trong một tệp:**
   ```bash
   uniq input.txt output.txt
   ```

2. **Đếm số lần xuất hiện của mỗi dòng:**
   ```bash
   uniq -c input.txt
   ```

3. **Chỉ hiển thị các dòng trùng lặp:**
   ```bash
   uniq -d input.txt
   ```

4. **Chỉ hiển thị các dòng duy nhất:**
   ```bash
   uniq -u input.txt
   ```

5. **Bỏ qua sự khác biệt giữa chữ hoa và chữ thường:**
   ```bash
   uniq -i input.txt output.txt
   ```

## Tips
- Để sử dụng `uniq` hiệu quả, hãy chắc chắn rằng đầu vào đã được sắp xếp. Bạn có thể sử dụng lệnh `sort` trước khi sử dụng `uniq` để đảm bảo điều này.
- Kết hợp `uniq` với các lệnh khác trong pipeline để xử lý dữ liệu một cách linh hoạt.
- Sử dụng tùy chọn `-c` để có cái nhìn tổng quan về số lượng các dòng trùng lặp, điều này có thể hữu ích trong phân tích dữ liệu.