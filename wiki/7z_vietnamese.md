# [Hệ điều hành] C Shell (csh) 7z Cách sử dụng: Nén và giải nén tệp

## Tổng quan
Lệnh `7z` là một công cụ mạnh mẽ để nén và giải nén các tệp và thư mục. Nó hỗ trợ nhiều định dạng nén khác nhau và cung cấp khả năng nén với tỷ lệ cao.

## Cách sử dụng
Cú pháp cơ bản của lệnh `7z` như sau:
```
7z [options] [arguments]
```

## Các tùy chọn phổ biến
- `a`: Thêm tệp vào một tệp nén mới.
- `x`: Giải nén tệp nén.
- `l`: Liệt kê nội dung của tệp nén.
- `d`: Xóa tệp trong tệp nén.
- `t`: Kiểm tra tính toàn vẹn của tệp nén.

## Ví dụ phổ biến
- Nén một thư mục:
  ```bash
  7z a archive.7z /path/to/directory
  ```
- Giải nén một tệp nén:
  ```bash
  7z x archive.7z
  ```
- Liệt kê nội dung của tệp nén:
  ```bash
  7z l archive.7z
  ```
- Xóa một tệp trong tệp nén:
  ```bash
  7z d archive.7z file.txt
  ```
- Kiểm tra tính toàn vẹn của tệp nén:
  ```bash
  7z t archive.7z
  ```

## Mẹo
- Luôn kiểm tra tính toàn vẹn của tệp nén sau khi giải nén để đảm bảo không có lỗi.
- Sử dụng tùy chọn `-p` để bảo vệ tệp nén bằng mật khẩu.
- Thực hiện nén với mức độ nén cao hơn bằng cách sử dụng tùy chọn `-mx=9`.