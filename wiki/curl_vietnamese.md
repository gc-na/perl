# [Hệ điều hành] C Shell (csh) curl Cách sử dụng: Lấy dữ liệu từ một URL

## Tổng quan
Lệnh `curl` là một công cụ dòng lệnh mạnh mẽ được sử dụng để truyền tải dữ liệu từ hoặc đến một máy chủ thông qua các giao thức như HTTP, HTTPS, FTP, và nhiều hơn nữa. Nó cho phép người dùng thực hiện các yêu cầu mạng và nhận dữ liệu từ các URL.

## Cách sử dụng
Cú pháp cơ bản của lệnh curl như sau:
```
curl [options] [arguments]
```

## Các tùy chọn phổ biến
- `-O`: Tải tệp và lưu với tên gốc.
- `-o [file]`: Tải tệp và lưu với tên chỉ định.
- `-I`: Chỉ lấy tiêu đề HTTP.
- `-d [data]`: Gửi dữ liệu trong yêu cầu POST.
- `-H [header]`: Thêm một tiêu đề tùy chỉnh vào yêu cầu.

## Ví dụ phổ biến
- Tải một tệp từ một URL và lưu với tên gốc:
  ```bash
  curl -O http://example.com/file.zip
  ```

- Tải một tệp và lưu với tên chỉ định:
  ```bash
  curl -o myfile.zip http://example.com/file.zip
  ```

- Lấy tiêu đề HTTP của một trang web:
  ```bash
  curl -I http://example.com
  ```

- Gửi dữ liệu trong yêu cầu POST:
  ```bash
  curl -d "name=John&age=30" http://example.com/api
  ```

- Thêm một tiêu đề tùy chỉnh vào yêu cầu:
  ```bash
  curl -H "Authorization: Bearer token" http://example.com/protected
  ```

## Mẹo
- Sử dụng `-L` để tự động theo dõi các chuyển hướng (redirects).
- Kiểm tra thông tin chi tiết về yêu cầu và phản hồi bằng cách sử dụng tùy chọn `-v` (verbose).
- Để lưu lịch sử của các yêu cầu, bạn có thể sử dụng `-o` để ghi vào tệp và xem lại sau này.