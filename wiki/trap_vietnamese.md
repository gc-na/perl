# [Hệ điều hành] C Shell (csh) trap Cách sử dụng: Quản lý tín hiệu trong shell

## Tổng quan
Lệnh `trap` trong C Shell (csh) được sử dụng để xử lý các tín hiệu và sự kiện trong quá trình thực thi của một script. Nó cho phép người dùng xác định các hành động cụ thể sẽ được thực hiện khi nhận được một tín hiệu nhất định, giúp quản lý và kiểm soát quá trình chạy của script.

## Cách sử dụng
Cú pháp cơ bản của lệnh `trap` như sau:

```csh
trap [hành động] [tín hiệu]
```

## Các tùy chọn phổ biến
- `hành động`: Hành động mà bạn muốn thực hiện khi nhận được tín hiệu. Có thể là một lệnh hoặc một tập hợp các lệnh.
- `tín hiệu`: Tín hiệu mà bạn muốn theo dõi, có thể là tên tín hiệu (như `INT`, `TERM`) hoặc số tín hiệu.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `trap`:

1. **Bắt tín hiệu ngắt (CTRL+C)**:
   ```csh
   trap 'echo "Script bị ngắt"; exit' INT
   ```

2. **Dọn dẹp trước khi thoát**:
   ```csh
   trap 'rm -f temp_file; echo "Đã xóa file tạm"; exit' EXIT
   ```

3. **Bắt tín hiệu thoát**:
   ```csh
   trap 'echo "Đang thoát"; exit' TERM
   ```

4. **Thực hiện nhiều lệnh khi nhận tín hiệu**:
   ```csh
   trap 'echo "Đang dừng"; kill -9 $$' HUP
   ```

## Mẹo
- **Sử dụng `EXIT`**: Đặt một lệnh dọn dẹp với tín hiệu `EXIT` để đảm bảo rằng các tài nguyên được giải phóng ngay cả khi script kết thúc bất ngờ.
- **Kiểm tra tín hiệu**: Sử dụng lệnh `trap -l` để liệt kê tất cả các tín hiệu có sẵn mà bạn có thể theo dõi.
- **Đặt nhiều tín hiệu**: Bạn có thể theo dõi nhiều tín hiệu bằng cách chỉ định chúng trong cùng một lệnh `trap`, giúp quản lý tốt hơn các tình huống khác nhau.