# [Hệ điều hành Unix] C Shell (csh) foreach: Lặp qua danh sách

## Overview
Lệnh `foreach` trong C Shell (csh) cho phép người dùng lặp qua một danh sách các giá trị và thực hiện một tập hợp các lệnh cho mỗi giá trị trong danh sách đó. Đây là một công cụ hữu ích để tự động hóa các tác vụ lặp lại trong môi trường dòng lệnh.

## Usage
Cú pháp cơ bản của lệnh `foreach` như sau:

```
foreach [biến] (danh sách)
    lệnh
end
```

## Common Options
Lệnh `foreach` không có nhiều tùy chọn phức tạp, nhưng dưới đây là một số điểm cần lưu ý:
- **biến**: Tên biến sẽ nhận giá trị từ danh sách trong mỗi lần lặp.
- **danh sách**: Danh sách các giá trị mà bạn muốn lặp qua.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `foreach`:

1. **Lặp qua các số từ 1 đến 5**:
   ```csh
   foreach i (1 2 3 4 5)
       echo "Số hiện tại là: $i"
   end
   ```

2. **Lặp qua các tên tệp**:
   ```csh
   foreach file (*.txt)
       echo "Đang xử lý tệp: $file"
   end
   ```

3. **Lặp qua các thư mục**:
   ```csh
   foreach dir (dir1 dir2 dir3)
       cd $dir
       echo "Đang ở trong thư mục: $dir"
       cd ..
   end
   ```

## Tips
- Hãy chắc chắn rằng danh sách bạn cung cấp cho `foreach` không chứa các ký tự đặc biệt có thể gây nhầm lẫn.
- Sử dụng `echo` để kiểm tra giá trị của biến trong quá trình lặp để đảm bảo rằng lệnh đang hoạt động như mong đợi.
- Bạn có thể kết hợp `foreach` với các lệnh khác để tạo ra các kịch bản phức tạp hơn, giúp tự động hóa nhiều tác vụ.