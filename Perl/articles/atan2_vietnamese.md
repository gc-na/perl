<!--
Meta Description: # Hàm atan2 trong Perl: Tính toán góc từ tọa độ Cartesian ## Tóm tắt Hàm `atan2` trong Perl được sử dụng để tính toán góc (độ) giữa trục x và trục y t...
Meta Keywords: góc, atan2, hàm, trong, tính
-->

# Hàm atan2 trong Perl: Tính toán góc từ tọa độ Cartesian

## Tóm tắt
Hàm `atan2` trong Perl được sử dụng để tính toán góc (độ) giữa trục x và trục y trong hệ tọa độ Cartesian, dựa trên các giá trị của hai tọa độ. Hàm này rất hữu ích trong đồ họa máy tính và các ứng dụng toán học liên quan đến hình học.

## Tài liệu
Hàm `atan2` nhận hai tham số đầu vào: tọa độ y và tọa độ x, và trả về giá trị góc tính bằng radian. Công thức tính được xác định như sau:

```perl
atan2(Y, X)
```

### Mục đích
Hàm `atan2` giúp xác định góc giữa điểm (x, y) và trục x dương. Giá trị trả về nằm trong khoảng từ -π đến π (-180 độ đến 180 độ). Việc sử dụng `atan2` giúp xử lý các trường hợp mà hàm `atan` không thể giải quyết do không xác định được dấu của x và y.

### Cách sử dụng
Để sử dụng hàm `atan2`, bạn chỉ cần gọi nó với hai tham số là tọa độ y và x. Dưới đây là cú pháp cơ bản:

```perl
my $goc = atan2($y, $x);
```

## Ví dụ
### Ví dụ 1: Tính góc cho điểm trong phần tư I
```perl
use strict;
use warnings;

my $y = 1;
my $x = 1;
my $goc = atan2($y, $x);
print "Góc là: $goc radians\n"; # Kết quả: Góc là: 0.7853981633974483 radians
```

### Ví dụ 2: Tính góc cho điểm trong phần tư II
```perl
use strict;
use warnings;

my $y = 1;
my $x = -1;
my $goc = atan2($y, $x);
print "Góc là: $goc radians\n"; # Kết quả: Góc là: 2.356194490192345 radians
```

### Ví dụ 3: Tính góc cho điểm trong phần tư III
```perl
use strict;
use warnings;

my $y = -1;
my $x = -1;
my $goc = atan2($y, $x);
print "Góc là: $goc radians\n"; # Kết quả: Góc là: -3.9269908169872414 radians
```

## Giải thích
Khi sử dụng hàm `atan2`, có một số điều cần lưu ý:
- Đảm bảo bạn cung cấp đúng thứ tự tham số: y trước x.
- Kết quả trả về là giá trị góc tính bằng radian. Nếu cần chuyển đổi sang độ, bạn có thể nhân với 180/π.
- Hàm `atan2` có thể xử lý trường hợp khi x = 0, điều mà hàm `atan` không thể làm. Khi x = 0, hàm sẽ trả về π/2 hoặc -π/2 tùy thuộc vào giá trị của y.
- Luôn kiểm tra các giá trị đầu vào để tránh lỗi không mong muốn.

## Tóm tắt một dòng
Hàm `atan2` trong Perl tính toán góc giữa trục x và y từ hai tọa độ, và là công cụ quan trọng trong các ứng dụng hình học và đồ họa.