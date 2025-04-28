<!--
Meta Description: # Lệnh system trong Perl: Cách Thực Thi Lệnh Hệ Thống ## Tóm tắt Lệnh `system` trong Perl cho phép bạn thực thi các lệnh hệ thống bên ngoài từ mã Perl...
Meta Keywords: lệnh, thực, thi, các, system
-->

# Lệnh system trong Perl: Cách Thực Thi Lệnh Hệ Thống

## Tóm tắt
Lệnh `system` trong Perl cho phép bạn thực thi các lệnh hệ thống bên ngoài từ mã Perl, trả về kết quả thực thi và mã thoát của lệnh đó.

## Tài liệu
### Mục đích
Lệnh `system` được sử dụng để chạy các lệnh hệ thống từ chương trình Perl. Bạn có thể gọi các chương trình khác, thực hiện các tác vụ bên ngoài, và nhận mã thoát để kiểm tra xem lệnh đó có thực thi thành công hay không.

### Cú pháp
```perl
system(Lệnh);
```
- **Lệnh**: Một chuỗi hoặc danh sách các tham số lệnh hệ thống cần thực thi.

### Chi tiết
Khi bạn gọi `system`, Perl sẽ tạo một quá trình con để chạy lệnh mà bạn đã chỉ định. Lệnh có thể là bất kỳ lệnh nào mà bạn có thể chạy trong terminal hoặc command prompt. Mã thoát của lệnh được trả về, với mã 0 cho thành công và các mã khác cho lỗi.

## Ví dụ
### Ví dụ 1: Thực thi lệnh đơn giản
```perl
my $result = system("ls -l");
if ($result == 0) {
    print "Lệnh thực thi thành công.\n";
} else {
    print "Lệnh thất bại với mã thoát: $result\n";
}
```

### Ví dụ 2: Thực thi lệnh với tham số
```perl
my $filename = "test.txt";
my $result = system("cat", $filename);
if ($result == 0) {
    print "Đã hiển thị nội dung của $filename.\n";
} else {
    print "Không thể đọc tệp: $filename với mã thoát: $result\n";
}
```

## Giải thích
- **Mã thoát**: Mã trả về từ lệnh có thể được kiểm tra để xác định xem lệnh có thành công hay không. Mã thoát 0 thường chỉ ra thành công, trong khi các mã khác chỉ ra lỗi.
- **Quá trình con**: Lệnh `system` tạo ra một quá trình con, điều này có thể ảnh hưởng đến hiệu suất nếu bạn thực thi nhiều lệnh liên tiếp.
- **Tránh sử dụng lệnh không an toàn**: Hãy cẩn thận khi thực thi các lệnh từ đầu vào không đáng tin cậy để tránh các tấn công tiêm mã.

## Tóm tắt một dòng
Lệnh `system` trong Perl cho phép bạn thực thi các lệnh hệ thống bên ngoài và trả về mã thoát để kiểm tra kết quả thực thi.