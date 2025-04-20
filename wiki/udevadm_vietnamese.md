# [Linux] C Shell (csh) udevadm Sử Dụng: Quản lý thiết bị trong hệ thống

## Tổng Quan
Lệnh `udevadm` được sử dụng để tương tác với hệ thống udev, một trình quản lý thiết bị trong Linux. Nó cho phép người dùng quản lý và theo dõi các thiết bị được kết nối với hệ thống, cũng như cấu hình các quy tắc cho các thiết bị đó.

## Cách Sử Dụng
Cú pháp cơ bản của lệnh `udevadm` như sau:
```
udevadm [options] [arguments]
```

## Các Tùy Chọn Thông Dụng
- `info`: Hiển thị thông tin về một thiết bị cụ thể.
- `trigger`: Kích hoạt các quy tắc udev cho các thiết bị hiện có.
- `settle`: Chờ cho tất cả các sự kiện udev đã hoàn tất.
- `control`: Quản lý hoạt động của udev daemon.

## Ví Dụ Thông Dụng
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `udevadm`:

1. **Hiển thị thông tin về một thiết bị cụ thể:**
   ```bash
   udevadm info --query=all --name=/dev/sda
   ```

2. **Kích hoạt các quy tắc udev cho các thiết bị hiện có:**
   ```bash
   udevadm trigger
   ```

3. **Chờ cho tất cả các sự kiện udev đã hoàn tất:**
   ```bash
   udevadm settle
   ```

4. **Quản lý hoạt động của udev daemon:**
   ```bash
   udevadm control --reload-rules
   ```

## Mẹo
- Luôn sử dụng tùy chọn `--query=all` khi cần thông tin chi tiết về thiết bị.
- Trước khi thay đổi quy tắc udev, hãy sao lưu các tệp cấu hình hiện tại để tránh mất mát dữ liệu.
- Sử dụng `udevadm monitor` để theo dõi các sự kiện thiết bị trong thời gian thực, điều này hữu ích cho việc gỡ lỗi.