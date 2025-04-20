# [Hệ điều hành] C Shell (csh) sftp Cách sử dụng: Truy cập và truyền tải tệp qua SSH

## Tổng quan
Lệnh `sftp` (SSH File Transfer Protocol) cho phép người dùng truyền tải tệp giữa máy tính cục bộ và máy chủ từ xa một cách an toàn thông qua giao thức SSH. Nó cung cấp một giao diện tương tác để thực hiện các thao tác như tải lên, tải xuống, và quản lý tệp.

## Cách sử dụng
Cú pháp cơ bản của lệnh `sftp` như sau:

```csh
sftp [options] [user@]hostname
```

## Các tùy chọn phổ biến
- `-P port`: Chỉ định cổng kết nối.
- `-i identity_file`: Sử dụng tệp khóa riêng để xác thực.
- `-b batchfile`: Chạy các lệnh từ tệp lệnh.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế khi sử dụng lệnh `sftp`:

1. **Kết nối đến máy chủ SFTP:**
   ```csh
   sftp user@hostname
   ```

2. **Tải tệp từ máy chủ về máy cục bộ:**
   ```csh
   get remote_file.txt
   ```

3. **Tải lên tệp từ máy cục bộ lên máy chủ:**
   ```csh
   put local_file.txt
   ```

4. **Liệt kê các tệp trong thư mục hiện tại trên máy chủ:**
   ```csh
   ls
   ```

5. **Tạo thư mục mới trên máy chủ:**
   ```csh
   mkdir new_directory
   ```

## Mẹo
- **Sử dụng khóa SSH:** Để tăng cường bảo mật, hãy sử dụng khóa SSH thay vì mật khẩu khi kết nối đến máy chủ.
- **Kiểm tra kết nối:** Trước khi thực hiện các thao tác truyền tải tệp, hãy kiểm tra kết nối bằng cách sử dụng lệnh `ls` để đảm bảo bạn đã kết nối thành công.
- **Sử dụng tệp lệnh:** Nếu bạn có nhiều lệnh cần thực hiện, hãy lưu chúng vào một tệp và sử dụng tùy chọn `-b` để chạy chúng tự động.