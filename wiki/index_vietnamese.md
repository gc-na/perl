<!--
Meta Description: # Tìm hiểu về Hàm `index` trong Perl: Cách Tìm Kiếm Chuỗi Nhanh Chóng ## Tóm tắt Hàm `index` trong Perl được sử dụng để tìm vị trí của một chuỗi con t...
Meta Keywords: chuỗi, tìm, trí, của, trong
-->

# Tìm hiểu về Hàm `index` trong Perl: Cách Tìm Kiếm Chuỗi Nhanh Chóng

## Tóm tắt
Hàm `index` trong Perl được sử dụng để tìm vị trí của một chuỗi con trong một chuỗi lớn hơn, trả về chỉ số bắt đầu của chuỗi con nếu tìm thấy, hoặc -1 nếu không tìm thấy.

## Tài liệu
Hàm `index` trong Perl có mục đích tìm kiếm vị trí của một chuỗi con trong một chuỗi lớn hơn. Cú pháp của hàm là:

```perl
index($string, $substring, $position);
```

- **$string**: Chuỗi lớn hơn mà bạn muốn tìm kiếm.
- **$substring**: Chuỗi con mà bạn muốn tìm kiếm trong chuỗi lớn.
- **$position** (tùy chọn): Vị trí bắt đầu tìm kiếm trong chuỗi lớn (mặc định là 0).

Hàm sẽ trả về chỉ số của vị trí đầu tiên mà chuỗi con được tìm thấy trong chuỗi lớn. Nếu chuỗi con không tồn tại, hàm sẽ trả về -1.

## Ví dụ
### Ví dụ 1: Tìm kiếm một chuỗi con
```perl
my $string = "Xin chào, thế giới!";
my $substring = "thế";
my $position = index($string, $substring);
print "Vị trí của '$substring' trong chuỗi là: $position\n";  # Kết quả: Vị trí của 'thế' trong chuỗi là: 8
```

### Ví dụ 2: Tìm kiếm từ vị trí cụ thể
```perl
my $string = "Xin chào, thế giới!";
my $substring = "chào";
my $position = index($string, $substring, 5);
print "Vị trí của '$substring' bắt đầu từ vị trí 5 là: $position\n";  # Kết quả: Vị trí của 'chào' bắt đầu từ vị trí 5 là: 4
```

## Giải thích
Khi sử dụng hàm `index`, có một số điểm cần lưu ý:

- **Chỉ số bắt đầu**: Chỉ số trả về bắt đầu từ 0. Do đó, vị trí đầu tiên của chuỗi sẽ luôn là 0.
- **Không phân biệt chữ hoa chữ thường**: Hàm `index` phân biệt chữ hoa và chữ thường, điều này có thể dẫn đến việc không tìm thấy chuỗi con nếu bạn không chú ý đến trường hợp chữ.
- **Chuỗi con rỗng**: Nếu chuỗi con là một chuỗi rỗng, hàm sẽ trả về chỉ số 0, vì một chuỗi rỗng được coi là xuất hiện tại mọi vị trí của chuỗi lớn.

## Tóm tắt ngắn gọn
Hàm `index` trong Perl giúp tìm kiếm vị trí của chuỗi con trong chuỗi lớn và trả về chỉ số của vị trí đó hoặc -1 nếu không tìm thấy.