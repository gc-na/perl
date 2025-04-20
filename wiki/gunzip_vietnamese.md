# [Hệ điều hành] C Shell (csh) gunzip Cách sử dụng: Giải nén tệp tin nén

## Tổng quan
Lệnh `gunzip` được sử dụng để giải nén các tệp tin nén có định dạng `.gz`. Lệnh này là một phần của bộ công cụ gzip, cho phép người dùng khôi phục lại các tệp tin đã bị nén để sử dụng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `gunzip` như sau:
```
gunzip [tùy chọn] [đối số]
```

## Các tùy chọn phổ biến
- `-c`: Giải nén tệp tin và xuất ra đầu ra chuẩn (stdout) mà không xóa tệp gốc.
- `-f`: Buộc giải nén tệp tin, ngay cả khi tệp đã tồn tại.
- `-k`: Giữ lại tệp tin gốc sau khi giải nén.
- `-v`: Hiển thị thông tin chi tiết về quá trình giải nén.

## Ví dụ thường gặp
- Giải nén một tệp tin đơn giản:
  ```bash
  gunzip file.txt.gz
  ```

- Giải nén và giữ lại tệp gốc:
  ```bash
  gunzip -k file.txt.gz
  ```

- Giải nén nhiều tệp tin cùng lúc:
  ```bash
  gunzip file1.gz file2.gz file3.gz
  ```

- Giải nén và xuất ra đầu ra chuẩn:
  ```bash
  gunzip -c file.txt.gz > file.txt
  ```

- Giải nén với thông tin chi tiết:
  ```bash
  gunzip -v file.txt.gz
  ```

## Mẹo
- Luôn kiểm tra dung lượng ổ đĩa trước khi giải nén, vì tệp tin giải nén có thể chiếm nhiều không gian hơn.
- Sử dụng tùy chọn `-k` nếu bạn không muốn mất tệp tin nén gốc.
- Để giải nén tệp tin trong một thư mục khác, bạn có thể sử dụng lệnh `-c` và chuyển hướng đầu ra đến thư mục mong muốn.