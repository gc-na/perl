# [Hệ điều hành] C Shell (csh) lsblk Cách sử dụng: [liệt kê thiết bị lưu trữ]

## Tổng quan
Lệnh `lsblk` được sử dụng để liệt kê các thiết bị lưu trữ trên hệ thống, bao gồm cả ổ đĩa cứng, ổ USB và phân vùng. Lệnh này cung cấp thông tin về cấu trúc và trạng thái của các thiết bị lưu trữ, giúp người dùng dễ dàng quản lý và theo dõi.

## Cách sử dụng
Cú pháp cơ bản của lệnh `lsblk` như sau:
```
lsblk [tùy chọn] [tham số]
```

## Tùy chọn phổ biến
- `-a` hoặc `--all`: Hiển thị tất cả các thiết bị, bao gồm cả những thiết bị không có phân vùng.
- `-f` hoặc `--fs`: Hiển thị thông tin về hệ thống tệp của các thiết bị.
- `-l` hoặc `--list`: Hiển thị danh sách các thiết bị theo dạng hàng.
- `-o` hoặc `--output`: Chỉ định các cột thông tin cụ thể để hiển thị.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `lsblk`:

1. Liệt kê tất cả các thiết bị lưu trữ:
   ```bash
   lsblk
   ```

2. Hiển thị thông tin chi tiết về hệ thống tệp:
   ```bash
   lsblk -f
   ```

3. Hiển thị danh sách các thiết bị theo dạng hàng:
   ```bash
   lsblk -l
   ```

4. Chỉ định cột thông tin cụ thể để hiển thị:
   ```bash
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
   ```

## Mẹo
- Sử dụng tùy chọn `-f` để nhanh chóng kiểm tra hệ thống tệp của các thiết bị, điều này rất hữu ích khi bạn cần xác định loại hệ thống tệp đang sử dụng.
- Kết hợp `lsblk` với các lệnh khác như `grep` để lọc kết quả theo nhu cầu cụ thể của bạn.
- Thường xuyên kiểm tra danh sách thiết bị lưu trữ để đảm bảo rằng bạn có thể quản lý và sử dụng chúng một cách hiệu quả.