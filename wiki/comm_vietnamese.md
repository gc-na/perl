# [Hệ điều hành] C Shell (csh) comm lệnh: So sánh hai tệp tin

## Tổng quan
Lệnh `comm` trong C Shell (csh) được sử dụng để so sánh hai tệp tin đã được sắp xếp và hiển thị các dòng khác nhau giữa chúng. Lệnh này rất hữu ích khi bạn muốn tìm ra sự khác biệt giữa hai tệp hoặc xác định các dòng chung.

## Cách sử dụng
Cú pháp cơ bản của lệnh `comm` như sau:

```csh
comm [options] [arguments]
```

## Các tùy chọn phổ biến
- `-1`: Không hiển thị các dòng chỉ có trong tệp đầu tiên.
- `-2`: Không hiển thị các dòng chỉ có trong tệp thứ hai.
- `-3`: Không hiển thị các dòng chung giữa hai tệp.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `comm`:

1. So sánh hai tệp tin và hiển thị tất cả các dòng khác nhau:
   ```csh
   comm file1.txt file2.txt
   ```

2. Chỉ hiển thị các dòng có trong tệp thứ hai:
   ```csh
   comm -13 file1.txt file2.txt
   ```

3. Chỉ hiển thị các dòng có trong tệp đầu tiên:
   ```csh
   comm -23 file1.txt file2.txt
   ```

4. Hiển thị các dòng chung giữa hai tệp:
   ```csh
   comm -12 file1.txt file2.txt
   ```

## Mẹo
- Đảm bảo rằng cả hai tệp tin được so sánh đều đã được sắp xếp trước khi sử dụng lệnh `comm`, nếu không, kết quả có thể không chính xác.
- Bạn có thể sử dụng lệnh `sort` để sắp xếp tệp tin trước khi so sánh:
  ```csh
  sort file1.txt > sorted_file1.txt
  sort file2.txt > sorted_file2.txt
  comm sorted_file1.txt sorted_file2.txt
  ```
- Sử dụng các tùy chọn kết hợp để tùy chỉnh đầu ra theo nhu cầu của bạn, giúp dễ dàng phân tích sự khác biệt giữa các tệp tin.