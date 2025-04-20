# [Hệ điều hành] C Shell (csh) expr Cách sử dụng: Tính toán và xử lý chuỗi

## Overview
Lệnh `expr` trong C Shell (csh) được sử dụng để thực hiện các phép toán số học, so sánh và xử lý chuỗi. Đây là một công cụ hữu ích cho việc tính toán và xử lý dữ liệu trong các kịch bản shell.

## Usage
Cú pháp cơ bản của lệnh `expr` như sau:
```
expr [options] [arguments]
```

## Common Options
- `+` : Phép cộng.
- `-` : Phép trừ.
- `*` : Phép nhân (cần phải được escape hoặc đặt trong dấu nháy đơn).
- `/` : Phép chia.
- `%` : Phép chia lấy dư.
- `=` : So sánh bằng.
- `!=` : So sánh khác.
- `<` : So sánh nhỏ hơn.
- `>` : So sánh lớn hơn.
- `length` : Trả về độ dài của chuỗi.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `expr`:

### Ví dụ 1: Phép cộng
```csh
expr 5 + 3
```
Kết quả: `8`

### Ví dụ 2: Phép trừ
```csh
expr 10 - 4
```
Kết quả: `6`

### Ví dụ 3: Phép nhân
```csh
expr 7 \* 6
```
Kết quả: `42`

### Ví dụ 4: Phép chia
```csh
expr 20 / 4
```
Kết quả: `5`

### Ví dụ 5: So sánh
```csh
expr 5 = 5
```
Kết quả: `1` (đúng)

### Ví dụ 6: Độ dài chuỗi
```csh
expr length "Hello World"
```
Kết quả: `11`

## Tips
- Luôn sử dụng dấu escape (`\`) cho phép nhân (`*`) để tránh nhầm lẫn với ký tự wildcard trong shell.
- Khi làm việc với chuỗi, hãy chắc chắn rằng chuỗi được đặt trong dấu nháy để tránh lỗi cú pháp.
- Sử dụng `expr` trong các kịch bản shell để tự động hóa các phép toán và so sánh, giúp tiết kiệm thời gian và công sức.