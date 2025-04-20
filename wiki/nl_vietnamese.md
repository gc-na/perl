# [Hệ điều hành] C Shell (csh) nl <Sử dụng tương đương>: Đánh số dòng trong tệp

## Tổng quan
Lệnh `nl` trong C Shell (csh) được sử dụng để đánh số các dòng trong một tệp văn bản. Nó giúp người dùng dễ dàng theo dõi và tham chiếu đến các dòng cụ thể trong tệp.

## Cú pháp
Cú pháp cơ bản của lệnh `nl` như sau:
```
nl [tùy chọn] [đối số]
```

## Tùy chọn thông dụng
- `-b`: Chỉ định cách đánh số dòng (ví dụ: `-b a` để đánh số tất cả các dòng).
- `-f`: Chỉ định số dòng bắt đầu cho mỗi tệp mới.
- `-h`: Bỏ qua các dòng tiêu đề.
- `-n`: Chỉ định kiểu đánh số (ví dụ: `-n ln` để đánh số theo kiểu lề trái).

## Ví dụ thông dụng
Dưới đây là một số ví dụ về cách sử dụng lệnh `nl`:

1. Đánh số tất cả các dòng trong một tệp:
   ```bash
   nl ten_tap.txt
   ```

2. Đánh số chỉ các dòng không trống:
   ```bash
   nl -b t ten_tap.txt
   ```

3. Đánh số các dòng trong một tệp và lưu kết quả vào một tệp mới:
   ```bash
   nl ten_tap.txt > ten_tap_moi.txt
   ```

4. Đánh số các dòng với kiểu lề phải:
   ```bash
   nl -n rn ten_tap.txt
   ```

## Mẹo
- Sử dụng tùy chọn `-b` để kiểm soát cách đánh số dòng, giúp bạn tùy chỉnh theo nhu cầu cụ thể.
- Kết hợp lệnh `nl` với các lệnh khác như `grep` hoặc `sort` để xử lý tệp hiệu quả hơn.
- Kiểm tra tài liệu hướng dẫn bằng lệnh `man nl` để tìm hiểu thêm về các tùy chọn và cách sử dụng.