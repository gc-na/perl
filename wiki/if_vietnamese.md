# [Hệ điều hành Unix] C Shell (csh) if: Kiểm tra điều kiện

## Overview
Lệnh `if` trong C Shell (csh) được sử dụng để kiểm tra một điều kiện và thực hiện các lệnh khác nhau dựa trên kết quả của điều kiện đó. Đây là một công cụ quan trọng trong lập trình shell để thực hiện các quyết định logic.

## Usage
Cú pháp cơ bản của lệnh `if` như sau:
```csh
if ( điều kiện ) then
    lệnh1
else
    lệnh2
endif
```

## Common Options
- `then`: Bắt đầu khối lệnh sẽ được thực hiện nếu điều kiện đúng.
- `else`: Bắt đầu khối lệnh sẽ được thực hiện nếu điều kiện sai.
- `endif`: Kết thúc khối lệnh `if`.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `if`:

### Ví dụ 1: Kiểm tra một biến
```csh
set var = 10
if ( $var > 5 ) then
    echo "Biến lớn hơn 5"
else
    echo "Biến không lớn hơn 5"
endif
```

### Ví dụ 2: Kiểm tra sự tồn tại của một tệp
```csh
if ( -e "file.txt" ) then
    echo "Tệp tồn tại"
else
    echo "Tệp không tồn tại"
endif
```

### Ví dụ 3: Kiểm tra một điều kiện phức tạp
```csh
set num = 15
if ( $num < 10 ) then
    echo "Số nhỏ hơn 10"
else if ( $num == 15 ) then
    echo "Số bằng 15"
else
    echo "Số lớn hơn 10 và không bằng 15"
endif
```

## Tips
- Luôn đảm bảo rằng các điều kiện được đặt trong dấu ngoặc đơn để tránh lỗi cú pháp.
- Sử dụng `else if` để kiểm tra nhiều điều kiện mà không cần lồng nhiều lệnh `if`.
- Kiểm tra kỹ các biến và điều kiện trước khi thực hiện lệnh để tránh lỗi không mong muốn.