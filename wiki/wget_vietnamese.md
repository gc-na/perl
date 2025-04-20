# [Hệ điều hành] C Shell (csh) wget Cách sử dụng: Tải xuống tệp từ Internet

## Tổng quan
Lệnh `wget` là một công cụ mạnh mẽ dùng để tải xuống tệp từ Internet. Nó hỗ trợ nhiều giao thức như HTTP, HTTPS và FTP, cho phép người dùng dễ dàng tải về các tệp mà không cần phải mở trình duyệt.

## Cách sử dụng
Cú pháp cơ bản của lệnh `wget` như sau:

```bash
wget [tùy chọn] [đối số]
```

## Tùy chọn phổ biến
- `-O [tên_tệp]`: Chỉ định tên tệp để lưu.
- `-c`: Tiếp tục tải xuống từ nơi đã dừng lại.
- `-q`: Chạy ở chế độ im lặng, không hiển thị thông tin tải xuống.
- `--limit-rate=[tốc_độ]`: Giới hạn tốc độ tải xuống.
- `-r`: Tải xuống các tệp từ một trang web một cách đệ quy.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `wget`:

1. Tải xuống một tệp đơn giản:
   ```bash
   wget http://example.com/file.zip
   ```

2. Tải xuống và lưu với tên khác:
   ```bash
   wget -O newfile.zip http://example.com/file.zip
   ```

3. Tiếp tục tải xuống một tệp đã dừng:
   ```bash
   wget -c http://example.com/file.zip
   ```

4. Tải xuống một trang web và tất cả các tệp liên quan:
   ```bash
   wget -r http://example.com
   ```

5. Giới hạn tốc độ tải xuống:
   ```bash
   wget --limit-rate=200k http://example.com/file.zip
   ```

## Mẹo
- Sử dụng tùy chọn `-q` để tải xuống mà không làm phiền bạn với thông tin không cần thiết.
- Nếu bạn cần tải xuống nhiều tệp, hãy xem xét việc sử dụng một tệp danh sách và lệnh `-i` để chỉ định tệp đó.
- Kiểm tra các tùy chọn khác nhau của `wget` bằng cách sử dụng `man wget` để tìm hiểu thêm về các tính năng nâng cao.