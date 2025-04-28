<!--
Meta Description: # Tìm Hiểu Về Hàm readline Trong Perl: Hướng Dẫn Chi Tiết ## Tóm Tắt Hàm `readline` trong Perl được sử dụng để đọc một hoặc nhiều dòng dữ liệu từ một ...
Meta Keywords: đọc, hàm, một, file, readline
-->

# Tìm Hiểu Về Hàm readline Trong Perl: Hướng Dẫn Chi Tiết

## Tóm Tắt
Hàm `readline` trong Perl được sử dụng để đọc một hoặc nhiều dòng dữ liệu từ một filehandle hoặc một file. Hàm này rất hữu ích trong việc xử lý dữ liệu văn bản và quản lý input từ người dùng.

## Tài Liệu
Hàm `readline` là một công cụ mạnh mẽ trong Perl cho phép lập trình viên dễ dàng đọc dữ liệu từ các nguồn khác nhau. Cú pháp cơ bản của hàm này như sau:

```perl
@lines = readline(FILEHANDLE);
```

### Mục đích
Mục đích chính của hàm `readline` là thu thập dữ liệu từ filehandle. Bạn có thể sử dụng hàm này để đọc toàn bộ nội dung của file hoặc chỉ một vài dòng tùy thuộc vào cách thức bạn gọi hàm.

### Cách sử dụng
- **Đọc từ filehandle**: Nếu bạn đã mở một filehandle, bạn có thể sử dụng `readline` để đọc nội dung của file.
- **Đọc từ một file cụ thể**: Bạn có thể chỉ định tên file để đọc trực tiếp từ file.

### Chi tiết
1. **Trả về**: Hàm `readline` trả về một danh sách các dòng đã đọc từ filehandle.
2. **Chấm dứt**: Khi không còn dữ liệu, hàm sẽ trả về `undef`.
3. **Đọc từng dòng**: Bạn có thể đọc từng dòng một bằng cách sử dụng vòng lặp `while`.

## Ví Dụ
Dưới đây là một số ví dụ minh họa việc sử dụng hàm `readline` trong Perl:

### Ví dụ 1: Đọc toàn bộ nội dung của file
```perl
open(my $fh, '<', 'file.txt') or die "Không thể mở file: $!";
my @lines = readline($fh);
close($fh);
print @lines;
```

### Ví dụ 2: Đọc từng dòng trong file
```perl
open(my $fh, '<', 'file.txt') or die "Không thể mở file: $!";
while (my $line = readline($fh)) {
    print $line;
}
close($fh);
```

### Ví dụ 3: Đọc từ STDIN
```perl
print "Nhập dữ liệu (Ctrl+D để kết thúc):\n";
while (my $line = readline(*STDIN)) {
    print "Bạn đã nhập: $line";
}
```

## Giải Thích
Khi sử dụng hàm `readline`, có một số điều bạn cần lưu ý:
- **Filehandle chưa mở**: Nếu bạn thử đọc từ một filehandle chưa được mở, chương trình sẽ gặp lỗi.
- **Xử lý dữ liệu rỗng**: Nếu file đã đọc hết, bạn nên kiểm tra giá trị trả về để tránh lỗi.
- **Dấu phân cách**: Hàm này tự động loại bỏ ký tự newline ở cuối mỗi dòng, nhưng nếu bạn cần giữ lại, bạn có thể sử dụng phương thức khác.

## Tóm Tắt Một Dòng
Hàm `readline` trong Perl cho phép bạn đọc dữ liệu từ filehandle hoặc file một cách dễ dàng và hiệu quả.