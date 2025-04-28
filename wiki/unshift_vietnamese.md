<!--
Meta Description: # Hàm `unshift` trong Perl: Cách Thêm Phần Tử Vào Đầu Mảng ## Tóm tắt Hàm `unshift` trong Perl cho phép bạn thêm một hoặc nhiều phần tử vào đầu một mả...
Meta Keywords: mảng, unshift, phần, thêm, vào
-->

# Hàm `unshift` trong Perl: Cách Thêm Phần Tử Vào Đầu Mảng

## Tóm tắt
Hàm `unshift` trong Perl cho phép bạn thêm một hoặc nhiều phần tử vào đầu một mảng, mang lại sự linh hoạt trong việc quản lý dữ liệu trong các mảng.

## Tài liệu
Hàm `unshift` được sử dụng để chèn các giá trị vào đầu một mảng. Cú pháp cơ bản của hàm này như sau:

```perl
unshift(@array, $value1, $value2, ...);
```

- **@array**: Tên của mảng mà bạn muốn thêm phần tử vào đầu.
- **$value1, $value2, ...**: Các giá trị bạn muốn thêm vào mảng.

Khi bạn gọi hàm `unshift`, mảng sẽ được cập nhật và trả về số lượng phần tử hiện có trong mảng sau khi thêm các phần tử mới.

### Mục đích
Hàm `unshift` rất hữu ích khi bạn cần quản lý danh sách theo thứ tự mà các phần tử được thêm vào, đặc biệt là khi thứ tự quan trọng trong ứng dụng của bạn.

## Ví dụ
Dưới đây là một số ví dụ đơn giản về cách sử dụng hàm `unshift`:

### Ví dụ 1: Thêm một phần tử vào mảng
```perl
my @array = (2, 3, 4);
unshift(@array, 1);
print "@array";  # Kết quả: 1 2 3 4
```

### Ví dụ 2: Thêm nhiều phần tử vào mảng
```perl
my @array = (3, 4);
unshift(@array, 1, 2);
print "@array";  # Kết quả: 1 2 3 4
```

### Ví dụ 3: Kiểm tra số lượng phần tử trong mảng
```perl
my @array = (1, 2);
my $count = unshift(@array, 0);
print "$count";  # Kết quả: 3
```

## Giải thích
Mặc dù `unshift` rất hữu ích, nhưng có một số điều cần lưu ý:

- **Hiệu suất**: Khi bạn thêm phần tử vào đầu một mảng lớn, hoạt động này có thể tốn thời gian vì tất cả các phần tử hiện có cần phải được di chuyển sang phải để tạo không gian cho các phần tử mới.
- **Tham chiếu đến mảng**: Nếu bạn sử dụng tham chiếu đến mảng, hãy đảm bảo sử dụng dấu `@{}` để truy cập đúng mảng. Ví dụ:
  ```perl
  my $array_ref = [1, 2, 3];
  unshift(@{$array_ref}, 0);
  print "@{$array_ref}";  # Kết quả: 0 1 2 3
  ```

## Tóm tắt một dòng
Hàm `unshift` trong Perl cho phép bạn thêm một hoặc nhiều phần tử vào đầu mảng, giúp quản lý danh sách một cách hiệu quả.