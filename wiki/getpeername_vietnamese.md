<!--
Meta Description: # Hàm getpeername trong Perl: Cách sử dụng và ví dụ ## Tóm tắt Hàm `getpeername` trong Perl được sử dụng để lấy địa chỉ của đối tác kết nối (peer) tro...
Meta Keywords: socket, hàm, dụng, địa, chỉ
-->

# Hàm getpeername trong Perl: Cách sử dụng và ví dụ

## Tóm tắt
Hàm `getpeername` trong Perl được sử dụng để lấy địa chỉ của đối tác kết nối (peer) trong một phiên làm việc mạng, thường được áp dụng trong các ứng dụng sử dụng socket.

## Tài liệu
### Mục đích
Hàm `getpeername` cho phép bạn xác định địa chỉ IP và cổng của máy chủ mà một socket đã kết nối đến. Điều này rất hữu ích trong các ứng dụng mạng để nhận diện và xử lý các kết nối từ bên ngoài.

### Cú pháp
```perl
use Socket;
my $peer_addr = getpeername(SOCKET);
```

### Tham số
- `SOCKET`: Đây là socket đã được tạo và kết nối đến một địa chỉ khác.

### Trả về
Hàm trả về địa chỉ của đối tác kết nối dưới dạng một chuỗi nhị phân. Để chuyển đổi địa chỉ này thành dạng có thể đọc được (như địa chỉ IP và cổng), bạn cần sử dụng hàm `getnameinfo` hoặc `unpack`.

## Ví dụ
### Ví dụ 1: Lấy địa chỉ của đối tác kết nối
```perl
use IO::Socket;
use Socket;

my $sock = IO::Socket::INET->new(
    Proto    => 'tcp',
    LocalPort => 5000,
    Listen    => 5,
    Reuse     => 1
) or die "Không thể tạo socket: $!";

while (my $client = $sock->accept()) {
    my $peer_addr = getpeername($client);
    my ($port, $ip) = unpack_sockaddr_in($peer_addr);
    print "Kết nối từ: " . inet_ntoa($ip) . ":" . $port . "\n";
}
```

### Ví dụ 2: Sử dụng với hàm `getnameinfo`
```perl
use IO::Socket;
use Socket;

my $sock = IO::Socket::INET->new(
    Proto    => 'tcp',
    LocalPort => 5001,
    Listen    => 5,
    Reuse     => 1
) or die "Không thể tạo socket: $!";

while (my $client = $sock->accept()) {
    my $peer_addr = getpeername($client);
    my ($port, $ip) = unpack_sockaddr_in($peer_addr);
    
    my $peer_name = getnameinfo($peer_addr);
    print "Kết nối từ: $peer_name\n";
}
```

## Giải thích
### Những điều cần lưu ý
- Đảm bảo rằng socket đã được kết nối trước khi gọi hàm `getpeername`, nếu không hàm sẽ trả về `undef`.
- Trong một số trường hợp, địa chỉ IP có thể không có sẵn, hãy xử lý các trường hợp ngoại lệ này.
- Sử dụng các hàm `inet_ntoa` và `unpack_sockaddr_in` để chuyển đổi địa chỉ và cổng từ định dạng nhị phân sang định dạng đọc được.

## Tóm tắt một dòng
Hàm `getpeername` trong Perl cho phép bạn lấy địa chỉ IP và cổng của đối tác kết nối trong một ứng dụng mạng.