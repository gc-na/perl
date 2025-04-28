<!--
Meta Description: # Hàm substr trong Perl: Cách sử dụng và ví dụ ## Tóm tắt Hàm `substr` trong Perl được sử dụng để truy xuất hoặc thay đổi một phần của chuỗi. Hàm này ...
Meta Keywords: chuỗi, phần, substr, thay, một
-->

# Hàm substr trong Perl: Cách sử dụng và ví dụ

## Tóm tắt
Hàm `substr` trong Perl được sử dụng để truy xuất hoặc thay đổi một phần của chuỗi. Hàm này rất hữu ích trong việc xử lý chuỗi, cho phép lập trình viên dễ dàng thao tác với các vị trí cụ thể trong chuỗi.

## Tài liệu
Hàm `substr` có cú pháp cơ bản như sau:

```perl
substr($string, $offset, $length, $replacement);
```

### Mô tả:
- **$string**: Chuỗi gốc mà bạn muốn thao tác.
- **$offset**: Vị trí bắt đầu để lấy hoặc thay thế phần của chuỗi. Lưu ý rằng vị trí bắt đầu tính từ 0.
- **$length**: Số ký tự cần lấy hoặc thay thế. Nếu không cung cấp, hàm sẽ lấy đến hết chuỗi.
- **$replacement**: (Tùy chọn) Chuỗi thay thế cho phần đã chỉ định. Nếu không có, hàm chỉ đơn giản là lấy phần chuỗi.

### Chức năng:
Hàm `substr` có thể được sử dụng để:
- Lấy một phần của chuỗi.
- Thay thế một phần của chuỗi bằng một giá trị khác.

## Ví dụ
### Lấy một phần của chuỗi
```perl
my $string = "Hello, World!";
my $sub = substr($string, 7, 5); # Kết quả: "World"
print $sub;
```

### Thay thế một phần của chuỗi
```perl
my $string = "Hello, World!";
substr($string, 7, 5, "Perl");
print $string; # Kết quả: "Hello, Perl!"
```

### Truy xuất từ vị trí âm
```perl
my $string = "Hello, World!";
my $sub = substr($string, -6, 5); # Kết quả: "World"
print $sub;
```

## Giải thích
- **Vị trí âm**: Bạn có thể sử dụng các chỉ số âm để bắt đầu từ cuối chuỗi. Ví dụ, `-1` tương ứng với ký tự cuối cùng.
- **Không có độ dài**: Nếu tham số `$length` không được cung cấp, `substr` sẽ trả về phần chuỗi từ vị trí `$offset` đến hết chuỗi.
- **Thay thế không cố định**: Khi bạn thay thế một phần của chuỗi, độ dài của chuỗi gốc có thể thay đổi, vì vậy hãy cẩn thận với các phép toán khác liên quan đến độ dài chuỗi.

## Tóm tắt một dòng
Hàm `substr` trong Perl cho phép bạn lấy hoặc thay thế một phần của chuỗi một cách linh hoạt và dễ dàng.