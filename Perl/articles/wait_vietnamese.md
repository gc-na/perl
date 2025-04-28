<!--
Meta Description: # Lệnh wait trong Perl: Chờ đợi tiến trình ## Tóm tắt Lệnh `wait` trong Perl được sử dụng để chờ đợi cho một hoặc nhiều tiến trình con hoàn tất. Nó ch...
Meta Keywords: trình, tiến, con, wait, thoát
-->

# Lệnh wait trong Perl: Chờ đợi tiến trình

## Tóm tắt
Lệnh `wait` trong Perl được sử dụng để chờ đợi cho một hoặc nhiều tiến trình con hoàn tất. Nó cho phép chương trình chính kiểm soát và thu thập thông tin về trạng thái của tiến trình con sau khi chúng đã kết thúc.

## Tài liệu
Lệnh `wait` trong Perl là một phần của hệ thống quản lý tiến trình. Khi một tiến trình con được tạo ra bằng cách sử dụng lệnh `fork`, tiến trình cha có thể sử dụng `wait` để tạm dừng thực thi cho đến khi tiến trình con hoàn tất. Điều này giúp đảm bảo rằng tiến trình cha có thể thu thập thông tin về trạng thái kết thúc của tiến trình con, chẳng hạn như mã thoát.

### Cách sử dụng
Để sử dụng `wait`, bạn chỉ cần gọi nó mà không cần tham số. Cú pháp cơ bản như sau:

```perl
wait;
```

Nếu bạn muốn thu thập mã thoát của tiến trình con, bạn có thể sử dụng biến `$?`, trong đó chứa mã thoát của tiến trình con cuối cùng đã kết thúc.

### Chi tiết
- `wait` sẽ chặn tiến trình cha cho đến khi một trong các tiến trình con của nó kết thúc.
- Nếu không có tiến trình con nào còn hoạt động, `wait` sẽ trả ngay lập tức với giá trị -1.
- Mã thoát của tiến trình con có thể được truy cập thông qua biến `$?`. Để lấy mã thoát thực tế, bạn có thể sử dụng phép toán bitwise để xử lý giá trị trong `$?`.

## Ví dụ
### Ví dụ cơ bản
```perl
my $pid = fork();

if ($pid == 0) {
    # Đây là tiến trình con
    print "Tiến trình con đang chạy...\n";
    exit(0); # Kết thúc với mã thoát 0
} else {
    # Đây là tiến trình cha
    wait(); # Chờ cho tiến trình con hoàn tất
    print "Tiến trình con đã hoàn tất.\n";
}
```

### Ví dụ với mã thoát
```perl
my $pid = fork();

if ($pid == 0) {
    # Tiến trình con
    exit(42); # Kết thúc với mã thoát 42
} else {
    # Tiến trình cha
    wait(); # Chờ cho tiến trình con hoàn tất
    my $exit_status = $? >> 8; # Lấy mã thoát
    print "Tiến trình con đã kết thúc với mã thoát: $exit_status\n";
}
```

## Giải thích
- **Cạm bẫy phổ biến**: Một cạm bẫy thường gặp là không kiểm tra biến `$pid` để xác định xem chương trình đang ở trong tiến trình cha hay con. Điều này có thể dẫn đến lỗi khi cố gắng thực hiện các hành động sai vị trí.
- **Giá trị trả về của wait**: Nếu không còn tiến trình con nào để chờ đợi, `wait` sẽ trả về -1 và giá trị của `$?` sẽ không thay đổi. Điều này có thể dẫn đến sự nhầm lẫn nếu không được kiểm tra đúng cách.
- **Nên sử dụng trong môi trường không đồng bộ**: Trong các ứng dụng có nhiều tiến trình, việc sử dụng `wait` là cần thiết để đảm bảo các tiến trình con được quản lý đúng cách.

## Tóm tắt một câu
Lệnh `wait` trong Perl cho phép tiến trình cha chờ đợi và thu thập mã thoát của tiến trình con khi chúng hoàn tất.