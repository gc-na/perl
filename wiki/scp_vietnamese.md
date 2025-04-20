# [Hệ điều hành] C Shell (csh) scp Cách sử dụng: Chuyển tệp an toàn giữa các máy tính

## Tổng quan
Lệnh `scp` (Secure Copy Protocol) được sử dụng để sao chép tệp giữa các máy tính qua mạng một cách an toàn. Nó sử dụng SSH để bảo mật dữ liệu trong quá trình truyền tải.

## Cách sử dụng
Cú pháp cơ bản của lệnh `scp` như sau:
```csh
scp [options] [arguments]
```

## Các tùy chọn thông dụng
- `-r`: Sao chép thư mục và tất cả các tệp con bên trong.
- `-P port`: Chỉ định cổng SSH khác với cổng mặc định (22).
- `-i identity_file`: Sử dụng tệp khóa riêng để xác thực.
- `-v`: Bật chế độ chi tiết để xem thông tin quá trình sao chép.

## Ví dụ thông dụng
Sao chép một tệp từ máy cục bộ đến máy từ xa:
```csh
scp localfile.txt user@remotehost:/path/to/destination/
```

Sao chép một tệp từ máy từ xa về máy cục bộ:
```csh
scp user@remotehost:/path/to/remotefile.txt /local/destination/
```

Sao chép một thư mục từ máy cục bộ sang máy từ xa:
```csh
scp -r localdirectory user@remotehost:/path/to/destination/
```

Sao chép tệp qua cổng SSH không mặc định:
```csh
scp -P 2222 localfile.txt user@remotehost:/path/to/destination/
```

## Mẹo
- Luôn kiểm tra kết nối SSH trước khi sử dụng `scp` để đảm bảo rằng bạn có quyền truy cập vào máy từ xa.
- Sử dụng tùy chọn `-v` để gỡ lỗi nếu gặp vấn đề trong quá trình sao chép.
- Đảm bảo rằng bạn đã thiết lập khóa SSH để tránh việc nhập mật khẩu mỗi lần sao chép tệp.