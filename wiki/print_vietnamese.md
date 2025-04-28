<!--
Meta Description: # Lệnh print trong Perl: Cách sử dụng và ví dụ ## Tóm tắt Lệnh `print` trong Perl là một trong những lệnh cơ bản nhất được sử dụng để in ra dữ liệu ra...
Meta Keywords: file, print, perl, lệnh, ghi
-->

# Lệnh print trong Perl: Cách sử dụng và ví dụ

## Tóm tắt
Lệnh `print` trong Perl là một trong những lệnh cơ bản nhất được sử dụng để in ra dữ liệu ra màn hình hoặc ghi vào file. Đây là một công cụ mạnh mẽ giúp các lập trình viên hiển thị thông tin, kết quả tính toán, hoặc thông báo cho người dùng.

## Tài liệu
Lệnh `print` trong Perl được sử dụng để xuất dữ liệu ra stdout (màn hình) hoặc tới một file. Cú pháp cơ bản của lệnh là:

```perl
print LIST;
```

Trong đó `LIST` có thể là một hoặc nhiều giá trị, có thể là chuỗi, số, hoặc biến. 

### Mục đích
Mục đích của lệnh `print` là để hiển thị thông tin cho người dùng hoặc ghi lại thông tin trong file. Nó có thể được sử dụng trong nhiều ngữ cảnh khác nhau, từ in ra các giá trị đơn giản đến các định dạng phức tạp.

### Cách sử dụng
Lệnh `print` có thể được sử dụng như sau:

- In một chuỗi:
  ```perl
  print "Xin chào, thế giới!\n";
  ```
  
- In giá trị của biến:
  ```perl
  my $ten = "Nguyen Van A";
  print "Tên của tôi là $ten\n";
  ```

- In nhiều giá trị:
  ```perl
  my $x = 10;
  my $y = 20;
  print "Giá trị của x là $x và y là $y\n";
  ```

- In ra file:
  ```perl
  open(my $fh, '>', 'output.txt') or die "Không thể mở file: $!";
  print $fh "Nội dung được ghi vào file\n";
  close($fh);
  ```

## Ví dụ
Dưới đây là một số ví dụ minh họa cho lệnh `print`:

1. **In chuỗi đơn giản**:
   ```perl
   print "Chào mừng đến với Perl!\n";
   ```

2. **In biến**:
   ```perl
   my $tuoi = 25;
   print "Tôi $tuoi tuổi.\n";
   ```

3. **In ra danh sách**:
   ```perl
   my @mang = ("apple", "banana", "cherry");
   print "Các loại trái cây: @mang\n";
   ```

4. **Ghi vào file**:
   ```perl
   open(my $file, '>', 'example.txt') or die "Không thể mở file: $!";
   print $file "Đây là một ví dụ ghi vào file.\n";
   close($file);
   ```

## Giải thích
Khi sử dụng lệnh `print`, có một số điểm cần lưu ý:

- **Ký tự xuống dòng**: Để in ra một dòng mới, bạn cần thêm ký tự `\n` vào cuối chuỗi.
- **Biến trong chuỗi**: Để in giá trị của biến trong chuỗi, sử dụng dấu `$` trước tên biến.
- **Ghi file**: Đảm bảo đã mở file trước khi sử dụng lệnh `print` để ghi dữ liệu.

### Những cạm bẫy thường gặp
- **Quên dấu chấm phẩy**: Mỗi lệnh trong Perl cần có dấu chấm phẩy ở cuối.
- **Chưa mở file**: Nếu bạn không mở file trước khi ghi, chương trình sẽ báo lỗi.
- **Không có quyền ghi**: Nếu file đã tồn tại và không có quyền ghi, bạn sẽ không thể ghi vào file.

## Tóm tắt một dòng
Lệnh `print` trong Perl cho phép bạn xuất dữ liệu ra màn hình hoặc ghi vào file một cách dễ dàng và linh hoạt.