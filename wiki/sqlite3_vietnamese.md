# [Hệ điều hành] C Shell (csh) sqlite3 Cách sử dụng: Truy cập và quản lý cơ sở dữ liệu SQLite

## Tổng quan
Lệnh `sqlite3` cho phép người dùng truy cập và quản lý cơ sở dữ liệu SQLite. Đây là một công cụ mạnh mẽ để thực hiện các truy vấn SQL, tạo bảng, và thao tác với dữ liệu trong cơ sở dữ liệu.

## Cách sử dụng
Cú pháp cơ bản của lệnh `sqlite3` như sau:
```
sqlite3 [tùy chọn] [đối số]
```

## Tùy chọn phổ biến
- `-help`: Hiển thị thông tin trợ giúp về lệnh.
- `-version`: Hiển thị phiên bản của SQLite.
- `-init <file>`: Chạy các lệnh SQL từ tệp chỉ định khi khởi động.
- `-batch`: Chạy ở chế độ không tương tác, thích hợp cho các tập lệnh tự động.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `sqlite3`:

1. **Tạo một cơ sở dữ liệu mới**:
   ```bash
   sqlite3 mydatabase.db
   ```

2. **Chạy một lệnh SQL để tạo bảng**:
   ```bash
   sqlite3 mydatabase.db "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);"
   ```

3. **Chèn dữ liệu vào bảng**:
   ```bash
   sqlite3 mydatabase.db "INSERT INTO users (name) VALUES ('Nguyễn Văn A');"
   ```

4. **Truy vấn dữ liệu từ bảng**:
   ```bash
   sqlite3 mydatabase.db "SELECT * FROM users;"
   ```

5. **Xuất kết quả truy vấn ra tệp**:
   ```bash
   sqlite3 mydatabase.db "SELECT * FROM users;" > output.txt
   ```

## Mẹo
- Sử dụng tùy chọn `-init` để tự động chạy các lệnh SQL khi khởi động, giúp tiết kiệm thời gian.
- Luôn kiểm tra phiên bản của SQLite để đảm bảo bạn đang sử dụng các tính năng mới nhất.
- Khi làm việc với cơ sở dữ liệu lớn, hãy cân nhắc sử dụng chế độ `-batch` để tăng tốc độ thực thi.