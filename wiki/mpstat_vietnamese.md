# [Hệ điều hành] C Shell (csh) mpstat Cách sử dụng: Theo dõi hiệu suất CPU

## Overview
Lệnh `mpstat` được sử dụng để theo dõi và báo cáo hiệu suất của các CPU trong hệ thống. Nó cung cấp thông tin chi tiết về mức sử dụng CPU, giúp người dùng phân tích và tối ưu hóa hiệu suất hệ thống.

## Usage
Cú pháp cơ bản của lệnh `mpstat` như sau:
```
mpstat [options] [arguments]
```

## Common Options
- `-P ALL`: Hiển thị thông tin cho tất cả các CPU.
- `-u`: Hiển thị thông tin về mức sử dụng CPU.
- `-w`: Hiển thị thông tin về mức sử dụng bộ nhớ.
- `-h`: Hiển thị thông tin theo định dạng dễ đọc hơn.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `mpstat`:

1. Hiển thị thông tin sử dụng CPU cho tất cả các CPU:
   ```bash
   mpstat -P ALL
   ```

2. Hiển thị thông tin sử dụng CPU với định dạng dễ đọc:
   ```bash
   mpstat -u -h
   ```

3. Theo dõi hiệu suất CPU mỗi 5 giây:
   ```bash
   mpstat 5
   ```

4. Hiển thị thông tin sử dụng CPU cho CPU 0:
   ```bash
   mpstat -P 0
   ```

## Tips
- Sử dụng tùy chọn `-P ALL` để có cái nhìn tổng quan về tất cả các CPU trong hệ thống.
- Kết hợp `mpstat` với các lệnh khác như `grep` để lọc thông tin cần thiết.
- Theo dõi hiệu suất CPU trong thời gian thực bằng cách sử dụng tùy chọn thời gian, giúp phát hiện các vấn đề kịp thời.