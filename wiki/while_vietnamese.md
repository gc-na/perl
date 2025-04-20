# [Hệ điều hành] C Shell (csh) while: Lặp lại một khối lệnh

## Overview
Lệnh `while` trong C Shell (csh) được sử dụng để thực hiện một khối lệnh nhiều lần miễn là điều kiện được chỉ định là đúng. Đây là một công cụ hữu ích để tự động hóa các tác vụ lặp đi lặp lại trong kịch bản.

## Usage
Cú pháp cơ bản của lệnh `while` như sau:

```csh
while ( điều kiện )
    # các lệnh cần thực hiện
end
```

## Common Options
Lệnh `while` không có nhiều tùy chọn, nhưng điều kiện bên trong dấu ngoặc có thể sử dụng nhiều biểu thức khác nhau, bao gồm:
- `-eq`: Kiểm tra xem hai giá trị có bằng nhau không.
- `-ne`: Kiểm tra xem hai giá trị có khác nhau không.
- `-lt`: Kiểm tra xem giá trị bên trái có nhỏ hơn giá trị bên phải không.
- `-gt`: Kiểm tra xem giá trị bên trái có lớn hơn giá trị bên phải không.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `while`:

### Ví dụ 1: Đếm từ 1 đến 5
```csh
set count = 1
while ( $count <= 5 )
    echo "Đếm: $count"
    @ count++
end
```

### Ví dụ 2: Lặp cho đến khi người dùng nhập 'exit'
```csh
set input = ""
while ( "$input" != "exit" )
    echo "Nhập một lệnh (hoặc 'exit' để thoát):"
    set input = $< 
end
```

### Ví dụ 3: Tính tổng các số từ 1 đến n
```csh
set n = 10
set sum = 0
set count = 1
while ( $count <= $n )
    @ sum += $count
    @ count++
end
echo "Tổng từ 1 đến $n là: $sum"
```

## Tips
- Đảm bảo rằng điều kiện trong lệnh `while` sẽ trở thành sai tại một thời điểm nào đó để tránh vòng lặp vô hạn.
- Sử dụng lệnh `@` để thực hiện các phép toán số học trong C Shell.
- Kiểm tra kỹ các biến trước khi sử dụng để đảm bảo chúng có giá trị mong muốn.