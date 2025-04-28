<!--
Meta Description: # Lệnh "stat" trong Perl: Kiểm Tra Thông Tin Tập Tin ## Tóm tắt Lệnh `stat` trong Perl cho phép bạn lấy thông tin chi tiết về một tập tin hoặc một thư...
Meta Keywords: tin, tập, stat, thông, một
-->

# Lệnh "stat" trong Perl: Kiểm Tra Thông Tin Tập Tin

## Tóm tắt
Lệnh `stat` trong Perl cho phép bạn lấy thông tin chi tiết về một tập tin hoặc một thư mục, bao gồm kích thước, thời gian chỉnh sửa, quyền truy cập và nhiều thông tin khác.

## Tài liệu
Lệnh `stat` là một hàm tích hợp trong Perl, được sử dụng để thu thập thông tin về các tập tin. Khi bạn gọi hàm `stat`, nó trả về một danh sách các giá trị chứa thông tin liên quan đến tập tin được chỉ định.

### Cú pháp
```perl
@stats = stat($filename);
```

### Tham số
- `$filename`: Tên tập tin hoặc đường dẫn đến tập tin mà bạn muốn kiểm tra.

### Kết quả
Hàm `stat` trả về một danh sách các giá trị, bao gồm:
1. Device ID (ID thiết bị)
2. Inode number (Số inode)
3. File type (Loại tập tin)
4. Permissions (Quyền truy cập)
5. Number of links (Số liên kết)
6. Owner's user ID (ID người dùng chủ sở hữu)
7. Group's ID (ID nhóm)
8. Size of file (Kích thước tập tin)
9. Last access time (Thời gian truy cập cuối)
10. Modification time (Thời gian chỉnh sửa cuối)
11. Change time (Thời gian thay đổi cuối)
12. Block size (Kích thước khối)
13. Number of blocks (Số khối)

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng hàm `stat`:

```perl
my $filename = 'example.txt';
my @stats = stat($filename);

if (@stats) {
    print "Kích thước tập tin: $stats[7] bytes\n";
    print "Thời gian chỉnh sửa cuối: " . localtime($stats[9]) . "\n";
} else {
    print "Không thể lấy thông tin tập tin: $!\n";
}
```

## Giải thích
Khi sử dụng `stat`, một số điều cần lưu ý:
- Kết quả của `stat` có thể khác nhau tùy thuộc vào hệ điều hành và hệ thống tập tin.
- Nếu tập tin không tồn tại hoặc không thể truy cập, `stat` sẽ trả về `undef` và biến `$!` sẽ chứa thông báo lỗi.
- Hãy chú ý đến quyền truy cập của tập tin; nếu không có quyền truy cập, bạn sẽ không thể lấy thông tin từ tập tin đó.

## Tóm tắt một dòng
Lệnh `stat` trong Perl cho phép lấy thông tin chi tiết về tập tin, bao gồm kích thước, thời gian và quyền truy cập.