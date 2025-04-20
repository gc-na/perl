# [Hệ điều hành] C Shell (csh) mkdir Cách sử dụng: Tạo thư mục mới

## Tổng quan
Lệnh `mkdir` trong C Shell (csh) được sử dụng để tạo thư mục mới trong hệ thống tệp. Đây là một lệnh cơ bản nhưng rất quan trọng trong quản lý tệp và thư mục.

## Cách sử dụng
Cú pháp cơ bản của lệnh `mkdir` như sau:

```
mkdir [tùy chọn] [đối số]
```

## Tùy chọn phổ biến
- `-p`: Tạo các thư mục cha nếu chúng chưa tồn tại.
- `-m`: Đặt quyền truy cập cho thư mục mới được tạo.
- `-v`: Hiển thị thông báo chi tiết về các thư mục đã được tạo.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `mkdir`:

1. Tạo một thư mục đơn giản:
   ```csh
   mkdir thu_muc_moi
   ```

2. Tạo nhiều thư mục cùng lúc:
   ```csh
   mkdir thu_muc1 thu_muc2 thu_muc3
   ```

3. Tạo thư mục cha nếu chưa tồn tại:
   ```csh
   mkdir -p duong/dan/thu_muc
   ```

4. Tạo thư mục với quyền truy cập cụ thể:
   ```csh
   mkdir -m 755 thu_muc_bao_mat
   ```

5. Hiển thị thông báo khi tạo thư mục:
   ```csh
   mkdir -v thu_muc_thong_bao
   ```

## Mẹo
- Luôn kiểm tra xem thư mục đã tồn tại hay chưa trước khi tạo để tránh lỗi.
- Sử dụng tùy chọn `-p` để tạo các thư mục lồng nhau một cách dễ dàng.
- Đặt quyền truy cập ngay khi tạo thư mục để đảm bảo tính bảo mật ngay từ đầu.