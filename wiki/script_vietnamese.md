# [Hệ điều hành] C Shell (csh) script: Ghi lại phiên làm việc

## Overview
Lệnh `script` trong C Shell (csh) được sử dụng để ghi lại một phiên làm việc trong terminal. Khi bạn chạy lệnh này, tất cả các đầu ra trên màn hình sẽ được lưu vào một tệp, cho phép bạn xem lại hoặc chia sẻ phiên làm việc của mình sau này.

## Usage
Cú pháp cơ bản của lệnh `script` như sau:
```
script [options] [arguments]
```

## Common Options
- `-a`: Thêm đầu ra vào tệp đã tồn tại thay vì ghi đè.
- `-f`: Ghi lại đầu ra ngay lập tức, không chờ đến khi phiên làm việc kết thúc.
- `-q`: Chạy ở chế độ im lặng, không hiển thị thông báo bắt đầu và kết thúc.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `script`:

1. Ghi lại một phiên làm việc vào tệp `session.log`:
   ```csh
   script session.log
   ```

2. Ghi lại phiên làm việc và thêm vào tệp đã tồn tại:
   ```csh
   script -a session.log
   ```

3. Ghi lại phiên làm việc ngay lập tức:
   ```csh
   script -f session.log
   ```

4. Chạy lệnh trong chế độ im lặng:
   ```csh
   script -q session.log
   ```

## Tips
- Hãy chắc chắn kiểm tra tệp ghi lại sau khi kết thúc phiên làm việc để đảm bảo mọi thông tin cần thiết đã được lưu.
- Sử dụng tùy chọn `-f` nếu bạn muốn theo dõi ngay lập tức các đầu ra trong thời gian thực.
- Đặt tên tệp ghi lại theo ngày hoặc nội dung để dễ dàng tìm kiếm sau này.