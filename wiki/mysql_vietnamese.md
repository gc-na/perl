# [Hệ điều hành] C Shell (csh) mysql Cách sử dụng: Truy cập và quản lý cơ sở dữ liệu MySQL

## Overview
Lệnh `mysql` được sử dụng để truy cập và quản lý cơ sở dữ liệu MySQL từ dòng lệnh. Nó cho phép người dùng thực hiện các truy vấn SQL, quản lý cơ sở dữ liệu và thực hiện các tác vụ khác liên quan đến MySQL.

## Usage
Cú pháp cơ bản của lệnh `mysql` như sau:
```
mysql [options] [arguments]
```

## Common Options
- `-u [username]`: Chỉ định tên người dùng để kết nối với cơ sở dữ liệu.
- `-p`: Yêu cầu nhập mật khẩu cho người dùng đã chỉ định.
- `-h [hostname]`: Chỉ định máy chủ MySQL mà bạn muốn kết nối.
- `-D [database]`: Chỉ định cơ sở dữ liệu mà bạn muốn sử dụng ngay lập tức sau khi kết nối.
- `--execute`: Thực thi một câu lệnh SQL ngay lập tức.

## Common Examples
- Kết nối đến MySQL với tên người dùng và mật khẩu:
  ```bash
  mysql -u root -p
  ```

- Kết nối đến một cơ sở dữ liệu cụ thể:
  ```bash
  mysql -u root -p -D mydatabase
  ```

- Thực thi một câu lệnh SQL từ dòng lệnh:
  ```bash
  mysql -u root -p --execute "SHOW DATABASES;"
  ```

- Xuất dữ liệu từ một bảng:
  ```bash
  mysql -u root -p -D mydatabase --execute "SELECT * FROM mytable;"
  ```

## Tips
- Luôn sử dụng tùy chọn `-p` để bảo mật mật khẩu của bạn.
- Nếu bạn thường xuyên làm việc với một cơ sở dữ liệu cụ thể, hãy sử dụng tùy chọn `-D` để tiết kiệm thời gian.
- Sử dụng lệnh `--execute` để thực hiện các câu lệnh SQL nhanh chóng mà không cần vào giao diện tương tác của MySQL.