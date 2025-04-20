# [Hệ điều hành] C Shell (csh) md5sum: [tính toán giá trị băm MD5]

## Tổng quan
Lệnh `md5sum` được sử dụng để tính toán và kiểm tra giá trị băm MD5 của một tệp tin. Giá trị băm MD5 là một chuỗi ký tự đại diện cho nội dung của tệp, giúp xác định tính toàn vẹn của tệp tin khi truyền tải hoặc lưu trữ.

## Cách sử dụng
Cú pháp cơ bản của lệnh `md5sum` như sau:
```
md5sum [tùy chọn] [đối số]
```

## Các tùy chọn phổ biến
- `-b`: Tính toán giá trị băm cho tệp nhị phân.
- `-c`: Kiểm tra giá trị băm từ một tệp tin chứa các giá trị băm đã được tính toán trước đó.
- `-t`: Tính toán giá trị băm cho tệp tin văn bản.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `md5sum`:

1. Tính toán giá trị băm MD5 cho một tệp tin:
   ```bash
   md5sum ten_tap_tin.txt
   ```

2. Tính toán giá trị băm cho nhiều tệp tin:
   ```bash
   md5sum tap_tin1.txt tap_tin2.txt
   ```

3. Kiểm tra giá trị băm từ một tệp tin:
   ```bash
   md5sum -c danh_sach_bam.md5
   ```

4. Tính toán giá trị băm cho tệp nhị phân:
   ```bash
   md5sum -b ten_tap_nhi_phan.bin
   ```

## Mẹo
- Luôn kiểm tra giá trị băm của tệp tin tải xuống để đảm bảo tính toàn vẹn.
- Sử dụng tệp tin chứa giá trị băm để dễ dàng kiểm tra nhiều tệp tin cùng một lúc.
- Kết hợp `md5sum` với các lệnh khác trong shell để tự động hóa quy trình kiểm tra tính toàn vẹn của tệp tin.