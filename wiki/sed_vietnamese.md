# [Hệ điều hành Unix] C Shell (csh) sed Cách sử dụng: Chỉnh sửa văn bản

## Tổng quan
Lệnh `sed` (stream editor) là một công cụ mạnh mẽ trong C Shell dùng để chỉnh sửa văn bản trong dòng. Nó cho phép người dùng thực hiện các thao tác như thay thế, xóa hoặc chèn văn bản một cách tự động trong các tệp hoặc đầu vào từ dòng lệnh.

## Cách sử dụng
Cú pháp cơ bản của lệnh `sed` như sau:
```bash
sed [options] [arguments]
```

## Các tùy chọn phổ biến
- `-e`: Cho phép thực hiện nhiều lệnh `sed` trong một lần gọi.
- `-i`: Chỉnh sửa tệp trực tiếp mà không cần tạo tệp tạm.
- `-n`: Ngăn không in ra đầu ra mặc định, chỉ in ra những dòng được chỉ định.
- `s`: Thay thế một chuỗi văn bản bằng một chuỗi khác.

## Ví dụ phổ biến
- **Thay thế một chuỗi văn bản trong tệp**:
```bash
sed 's/old_text/new_text/' filename.txt
```

- **Thay thế tất cả các chuỗi trong tệp**:
```bash
sed 's/old_text/new_text/g' filename.txt
```

- **Chỉnh sửa tệp trực tiếp**:
```bash
sed -i 's/old_text/new_text/g' filename.txt
```

- **In ra các dòng chứa một chuỗi cụ thể**:
```bash
sed -n '/pattern/p' filename.txt
```

- **Xóa các dòng chứa một chuỗi cụ thể**:
```bash
sed '/pattern/d' filename.txt
```

## Mẹo
- Hãy luôn sao lưu tệp trước khi sử dụng tùy chọn `-i` để tránh mất dữ liệu.
- Sử dụng tùy chọn `-n` để chỉ in ra những dòng bạn quan tâm, giúp đầu ra gọn gàng hơn.
- Thực hành với các tệp nhỏ trước khi áp dụng trên các tệp lớn để làm quen với cú pháp và hành vi của `sed`.