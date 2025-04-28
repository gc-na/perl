<!--
Meta Description: # Hàm getsockname trong Perl: Cách sử dụng và ví dụ ## Tóm tắt Hàm `getsockname` trong Perl được sử dụng để lấy địa chỉ của socket hiện tại, cho phép ...
Meta Keywords: socket, địa, chỉ, một, getsockname
-->

# Hàm getsockname trong Perl: Cách sử dụng và ví dụ

## Tóm tắt
Hàm `getsockname` trong Perl được sử dụng để lấy địa chỉ của socket hiện tại, cho phép người lập trình xác định địa chỉ IP và cổng mà socket đang sử dụng.

## Tài liệu
Hàm `getsockname` là một phần của mô-đun `Socket` trong Perl, cho phép người dùng truy xuất thông tin địa chỉ của một socket đã được tạo ra. Hàm này rất hữu ích trong các ứng dụng mạng khi bạn cần biết thông tin chi tiết về socket đang hoạt động.

### Cú pháp
```perl
getsockname SOCKET
```

- **SOCKET**: Là biến đại diện cho socket mà bạn muốn lấy địa chỉ. Biến này phải là một socket đã được tạo ra bằng cách sử dụng `socket()`.

### Mô tả
Khi bạn gọi hàm `getsockname`, nó sẽ trả về địa chỉ IP và cổng mà socket đang sử dụng. Thông tin này được trả về dưới dạng một biến, thường là một tham số được sử dụng cùng với các hàm khác như `unpack` để trích xuất thông tin cụ thể từ địa chỉ.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng `getsockname` trong Perl:

```perl
use strict;
use warnings;
use IO::Socket;

# Tạo một socket
my $socket = IO::Socket::INET->new(
    Proto => 'udp',
    LocalPort => 0, # Cho hệ thống tự động chọn cổng
) or die "Không thể tạo socket: $!";

# Lấy địa chỉ của socket
my $sock_addr = getsockname($socket);
my ($port, $ip) = sockaddr_in($sock_addr);

print "Địa chỉ IP: " . inet_ntoa($ip) . "\n";
print "Cổng: " . $port . "\n";
```

## Giải thích
Khi sử dụng `getsockname`, có một số điều cần lưu ý:

- **Socket chưa kết nối**: Nếu socket chưa được liên kết với một địa chỉ (ví dụ, chưa gọi `bind`), hàm `getsockname` có thể không hoạt động như mong đợi.
- **Kiểm tra lỗi**: Luôn kiểm tra lỗi khi tạo socket và khi gọi các hàm liên quan để đảm bảo rằng chương trình của bạn không gặp phải vấn đề không mong muốn.
- **Chạy trên nền tảng khác nhau**: Các chi tiết về địa chỉ mạng có thể khác nhau trên các nền tảng khác nhau. Do đó, cần chú ý khi làm việc trên các hệ điều hành khác nhau để đảm bảo tính tương thích.

## Tóm tắt một câu
Hàm `getsockname` trong Perl cho phép lấy địa chỉ IP và cổng của một socket đã được tạo ra, rất hữu ích trong các ứng dụng mạng.