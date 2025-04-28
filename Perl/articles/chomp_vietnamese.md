<!--
Meta Description: # Chomp trong Perl: Cách sử dụng và ví dụ ## Tóm tắt `chomp` là một hàm trong ngôn ngữ lập trình Perl, dùng để loại bỏ ký tự xuống dòng (newline) ở cu...
Meta Keywords: chomp, dòng, loại, xuống, perl
-->

# Chomp trong Perl: Cách sử dụng và ví dụ

## Tóm tắt
`chomp` là một hàm trong ngôn ngữ lập trình Perl, dùng để loại bỏ ký tự xuống dòng (newline) ở cuối chuỗi. Hàm này rất hữu ích khi làm việc với dữ liệu đầu vào từ người dùng hoặc từ các tệp tin.

## Tài liệu
Hàm `chomp` có tác dụng chính là loại bỏ ký tự xuống dòng ở cuối chuỗi. Ký tự này thường là `\n` (newline) trên hệ điều hành Unix/Linux và có thể là `\r\n` (carriage return + newline) trên Windows.

### Cú pháp
```perl
chomp($string);
```
- `$string`: là biến chuỗi mà bạn muốn loại bỏ ký tự xuống dòng.

### Mục đích
- Đảm bảo rằng dữ liệu đầu vào không có ký tự không cần thiết ở cuối, giúp tránh lỗi trong quá trình xử lý dữ liệu.
- Làm sạch dữ liệu khi đọc từ tệp hoặc đầu vào từ người dùng.

### Sử dụng
Hàm `chomp` có thể được sử dụng với các biến scalars, mảng hoặc thậm chí là các tham số của hàm. Khi sử dụng với mảng, `chomp` sẽ loại bỏ ký tự xuống dòng cho tất cả các phần tử trong mảng.

## Ví dụ
### Ví dụ cơ bản
```perl
my $string = "Hello, World!\n";
chomp($string);
print $string;  # Xuất ra: Hello, World!
```

### Ví dụ với mảng
```perl
my @lines = ("First line\n", "Second line\n", "Third line\n");
chomp(@lines);
print join(", ", @lines);  # Xuất ra: First line, Second line, Third line
```

### Ví dụ với đầu vào từ người dùng
```perl
print "Nhập tên của bạn: ";
my $name = <STDIN>;
chomp($name);
print "Xin chào, $name!\n";
```

## Giải thích
- **Những cạm bẫy thường gặp**: Một số lập trình viên mới có thể không nhận ra rằng `chomp` chỉ loại bỏ ký tự xuống dòng ở cuối chuỗi. Nếu chuỗi không kết thúc bằng ký tự xuống dòng, nó sẽ không thay đổi.
- **Đặc điểm:** `chomp` chỉ hoạt động với ký tự xuống dòng, không loại bỏ bất kỳ ký tự nào khác. Để loại bỏ các ký tự khác, bạn có thể sử dụng regex hoặc hàm `s///`.
- **Hành vi khi không có tham số**: Nếu không có tham số nào được đưa vào, `chomp` sẽ loại bỏ ký tự xuống dòng của biến `$_` (biến mặc định trong Perl).

## Tóm tắt một dòng
Hàm `chomp` trong Perl dùng để loại bỏ ký tự xuống dòng ở cuối chuỗi, giúp làm sạch dữ liệu đầu vào.