# [Hệ điều hành] C Shell (csh) strace Cách sử dụng: Theo dõi các cuộc gọi hệ thống

## Tổng quan
Lệnh `strace` được sử dụng để theo dõi và ghi lại các cuộc gọi hệ thống mà một chương trình thực hiện trong quá trình chạy. Điều này rất hữu ích để gỡ lỗi và phân tích hành vi của các ứng dụng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `strace` như sau:
```csh
strace [options] [arguments]
```

## Các tùy chọn phổ biến
- `-c`: Tóm tắt thống kê các cuộc gọi hệ thống.
- `-f`: Theo dõi các cuộc gọi hệ thống của các tiến trình con.
- `-o <file>`: Ghi đầu ra vào tệp thay vì hiển thị trên màn hình.
- `-e <expression>`: Chỉ theo dõi các cuộc gọi hệ thống cụ thể theo biểu thức đã cho.

## Ví dụ phổ biến
1. Theo dõi một chương trình đơn giản:
   ```csh
   strace ls
   ```

2. Ghi lại đầu ra vào một tệp:
   ```csh
   strace -o output.txt ls
   ```

3. Tóm tắt các cuộc gọi hệ thống:
   ```csh
   strace -c ls
   ```

4. Theo dõi các cuộc gọi hệ thống của tiến trình con:
   ```csh
   strace -f ./my_program
   ```

5. Chỉ theo dõi các cuộc gọi hệ thống liên quan đến tệp:
   ```csh
   strace -e trace=file ls
   ```

## Mẹo
- Sử dụng tùy chọn `-o` để lưu lại đầu ra cho việc phân tích sau này.
- Kết hợp với `-c` để có cái nhìn tổng quan về hiệu suất của các cuộc gọi hệ thống.
- Đọc tài liệu hướng dẫn bằng cách sử dụng `man strace` để tìm hiểu thêm về các tùy chọn và cách sử dụng.