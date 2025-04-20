# [Hệ điều hành Linux] C Shell (csh) mkswap: Tạo không gian hoán đổi

## Overview
Lệnh `mkswap` được sử dụng để tạo một vùng không gian hoán đổi (swap space) trên một thiết bị lưu trữ. Không gian hoán đổi cho phép hệ điều hành sử dụng không gian trên đĩa để mở rộng bộ nhớ ảo, giúp cải thiện hiệu suất khi bộ nhớ RAM không đủ.

## Usage
Cú pháp cơ bản của lệnh `mkswap` như sau:
```
mkswap [options] [arguments]
```

## Common Options
- `-f`: Bỏ qua kiểm tra lỗi trên thiết bị.
- `-L label`: Gán nhãn cho vùng hoán đổi.
- `-p priority`: Thiết lập độ ưu tiên cho vùng hoán đổi.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `mkswap`:

1. Tạo một tệp hoán đổi có kích thước 1GB:
   ```bash
   dd if=/dev/zero of=/swapfile bs=1M count=1024
   mkswap /swapfile
   ```

2. Tạo một vùng hoán đổi trên một phân vùng cụ thể:
   ```bash
   mkswap /dev/sda5
   ```

3. Gán nhãn cho vùng hoán đổi:
   ```bash
   mkswap -L my_swap /dev/sda5
   ```

4. Thiết lập độ ưu tiên cho vùng hoán đổi:
   ```bash
   mkswap -p 10 /dev/sda5
   ```

## Tips
- Đảm bảo rằng không gian hoán đổi đủ lớn để đáp ứng nhu cầu của hệ thống, thường là từ 1 đến 2 lần kích thước RAM.
- Sau khi tạo vùng hoán đổi, hãy sử dụng lệnh `swapon` để kích hoạt nó.
- Kiểm tra trạng thái của không gian hoán đổi bằng lệnh `swapon --show` để xác nhận rằng nó đã được kích hoạt thành công.