<!--
Meta Description: # Tính căn bậc hai trong Perl với hàm sqrt ## Tóm tắt Hàm `sqrt` trong Perl dùng để tính căn bậc hai của một số. Đây là một trong những hàm toán học c...
Meta Keywords: căn, bậc, hai, của, hàm
-->

# Tính căn bậc hai trong Perl với hàm sqrt

## Tóm tắt
Hàm `sqrt` trong Perl dùng để tính căn bậc hai của một số. Đây là một trong những hàm toán học cơ bản được sử dụng rộng rãi trong lập trình để xử lý các phép toán số học.

## Tài liệu
Hàm `sqrt` là một hàm trong Perl được sử dụng để tính căn bậc hai của một số không âm. Cú pháp của hàm này rất đơn giản:

```perl
my $sqrt_value = sqrt($number);
```

### Mục đích
Hàm `sqrt` giúp lập trình viên dễ dàng lấy căn bậc hai của một giá trị số học, phục vụ cho nhiều mục đích khác nhau trong tính toán và phân tích dữ liệu.

### Cách sử dụng
- **Tham số đầu vào**: Hàm nhận một tham số, đó là số mà bạn muốn tính căn bậc hai. Tham số này phải là một số không âm.
- **Giá trị trả về**: Hàm trả về căn bậc hai của số đó. Nếu tham số là âm, hàm sẽ trả về `NaN` (Not a Number).

## Ví dụ
Dưới đây là một số ví dụ về cách sử dụng hàm `sqrt` trong Perl:

### Ví dụ 1: Tính căn bậc hai của một số dương
```perl
my $number = 16;
my $sqrt_value = sqrt($number);
print "Căn bậc hai của $number là: $sqrt_value\n"; # Kết quả: Căn bậc hai của 16 là: 4
```

### Ví dụ 2: Tính căn bậc hai của số 0
```perl
my $number = 0;
my $sqrt_value = sqrt($number);
print "Căn bậc hai của $number là: $sqrt_value\n"; # Kết quả: Căn bậc hai của 0 là: 0
```

### Ví dụ 3: Căn bậc hai của số âm
```perl
my $number = -9;
my $sqrt_value = sqrt($number);
print "Căn bậc hai của $number là: $sqrt_value\n"; # Kết quả: Căn bậc hai của -9 là: NaN
```

## Giải thích
Khi sử dụng hàm `sqrt`, có một số điều cần lưu ý:
- Chỉ số không âm mới được phép tính căn bậc hai. Nếu bạn cố gắng tính căn bậc hai của một số âm, hàm sẽ trả về `NaN`.
- Hãy đảm bảo rằng bạn kiểm tra giá trị đầu vào trước khi gọi hàm `sqrt`, để tránh gặp lỗi không mong muốn trong quá trình thực thi chương trình.

## Tóm tắt trong một câu
Hàm `sqrt` trong Perl cho phép tính toán căn bậc hai của một số không âm, rất hữu ích trong các phép toán số học cơ bản.