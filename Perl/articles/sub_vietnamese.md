<!--
Meta Description: # Tìm Hiểu Về Từ Khóa "sub" Trong Perl ## Tóm Tắt Từ khóa `sub` trong Perl được sử dụng để định nghĩa một hàm. Đây là một phần quan trọng trong việc l...
Meta Keywords: hàm, định, nghĩa, perl, sub
-->

# Tìm Hiểu Về Từ Khóa "sub" Trong Perl

## Tóm Tắt
Từ khóa `sub` trong Perl được sử dụng để định nghĩa một hàm. Đây là một phần quan trọng trong việc lập trình với Perl, cho phép bạn tổ chức mã nguồn và tái sử dụng các đoạn mã một cách hiệu quả.

## Tài Liệu
### Mục Đích
`sub` giúp định nghĩa một hàm trong Perl, cho phép bạn nhóm các đoạn mã lại với nhau để thực hiện một chức năng cụ thể. Hàm có thể nhận tham số đầu vào và trả về giá trị.

### Cú Pháp
Cú pháp cơ bản để định nghĩa một hàm là:

```perl
sub tên_hàm {
    # Các câu lệnh
    return giá_trị;  # Không bắt buộc
}
```

### Sử Dụng
- **Định nghĩa**: Bạn có thể định nghĩa một hàm bằng cách sử dụng từ khóa `sub`, theo sau là tên hàm và khối mã.
- **Gọi hàm**: Để sử dụng hàm đã định nghĩa, bạn gọi nó bằng tên hàm.

## Ví Dụ
### Ví dụ 1: Hàm Không Tham Số
```perl
sub say_hello {
    print "Xin chào!\n";
}

say_hello();  # Kết quả: Xin chào!
```

### Ví dụ 2: Hàm Có Tham Số
```perl
sub add {
    my ($a, $b) = @_;
    return $a + $b;
}

my $sum = add(5, 10);  # Kết quả: 15
print "Tổng là: $sum\n";
```

### Ví dụ 3: Hàm Trả Về Giá Trị
```perl
sub multiply {
    my ($x, $y) = @_;
    return $x * $y;
}

my $product = multiply(4, 5);  # Kết quả: 20
print "Tích là: $product\n";
```

## Giải Thích
- **Tham Số và Giá Trị Trả Về**: Khi định nghĩa hàm, bạn có thể nhận nhiều tham số bằng cách sử dụng dấu `@_`. Giá trị trả về không bắt buộc nhưng thường được thực hiện qua từ khóa `return`.
- **Biến Toàn Cục và Biến Cục Bộ**: Biến được định nghĩa bên trong hàm là cục bộ và không thể truy cập từ bên ngoài. Bạn có thể sử dụng biến toàn cục nếu cần.
- **Gọi hàm**: Đảm bảo rằng hàm đã được định nghĩa trước khi gọi.

### Những Cái Bẫy Thường Gặp
- **Không Định Nghĩa Hàm Trước Khi Gọi**: Nếu bạn gọi một hàm trước khi định nghĩa nó, Perl sẽ báo lỗi.
- **Tham Số Không Đúng**: Đảm bảo rằng số lượng tham số khi gọi hàm phải tương ứng với số tham số trong định nghĩa.

## Tóm Tắt Một Câu
Từ khóa `sub` trong Perl cho phép bạn định nghĩa và sử dụng hàm, giúp tổ chức mã nguồn và tái sử dụng các đoạn mã hiệu quả.