# [Hệ điều hành] C Shell (csh) fdisk Cách sử dụng: Quản lý phân vùng ổ đĩa

## Tổng quan
Lệnh `fdisk` được sử dụng để quản lý phân vùng trên ổ đĩa cứng. Nó cho phép người dùng tạo, xóa, thay đổi kích thước và kiểm tra các phân vùng, giúp tối ưu hóa việc sử dụng không gian lưu trữ.

## Cách sử dụng
Cú pháp cơ bản của lệnh `fdisk` như sau:
```bash
fdisk [options] [arguments]
```

## Các tùy chọn phổ biến
- `-l`: Liệt kê tất cả các phân vùng trên các ổ đĩa.
- `-u`: Sử dụng đơn vị là số sector thay vì megabyte.
- `-n`: Tạo một phân vùng mới.
- `-d`: Xóa một phân vùng.
- `-p`: In ra bảng phân vùng hiện tại.

## Ví dụ phổ biến
- **Liệt kê các phân vùng**:
```bash
fdisk -l
```

- **Tạo một phân vùng mới**:
```bash
fdisk /dev/sda
```
Sau đó, bạn sẽ được hướng dẫn để nhập các thông tin cần thiết cho phân vùng mới.

- **Xóa một phân vùng**:
```bash
fdisk /dev/sda
```
Chọn phân vùng cần xóa và làm theo hướng dẫn.

- **In ra bảng phân vùng**:
```bash
fdisk -p /dev/sda
```

## Mẹo
- Trước khi thực hiện bất kỳ thay đổi nào với `fdisk`, hãy sao lưu dữ liệu quan trọng để tránh mất mát.
- Sử dụng lệnh `man fdisk` để xem tài liệu hướng dẫn chi tiết về các tùy chọn và cách sử dụng.
- Hãy cẩn thận khi xóa hoặc thay đổi phân vùng, vì các thao tác này có thể làm mất dữ liệu.