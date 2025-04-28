<!--
Meta Description: # Truyền đổi ký tự trong Perl với lệnh tr/// ## Tóm tắt Lệnh `tr///` trong Perl được sử dụng để thay thế hoặc xóa các ký tự trong một chuỗi. Đây là mộ...
Meta Keywords: trong, các, thay, lệnh, thế
-->

# Truyền đổi ký tự trong Perl với lệnh tr///

## Tóm tắt
Lệnh `tr///` trong Perl được sử dụng để thay thế hoặc xóa các ký tự trong một chuỗi. Đây là một công cụ mạnh mẽ cho phép người lập trình dễ dàng thực hiện các thao tác biến đổi ký tự mà không cần phải viết nhiều mã lệnh phức tạp.

## Tài liệu
Lệnh `tr///` là viết tắt của "translate" (dịch). Nó cho phép bạn thay thế các ký tự trong một chuỗi với các ký tự khác hoặc xóa chúng. Cú pháp cơ bản của lệnh này như sau:

```perl
tr/old_characters/new_characters/;
```

Trong đó:
- `old_characters` là danh sách các ký tự bạn muốn thay thế.
- `new_characters` là danh sách các ký tự sẽ thay thế cho các ký tự trong `old_characters`.

Lưu ý rằng số lượng ký tự trong `old_characters` và `new_characters` cần phải khớp nhau. Nếu số lượng ký tự không khớp, Perl sẽ cảnh báo và chỉ thực hiện thay thế cho các ký tự có số lượng phù hợp.

## Ví dụ
### Ví dụ 1: Thay thế ký tự
```perl
my $string = "hello world";
$string =~ tr/h/e/;
print $string;  # Kết quả: "eello world"
```

### Ví dụ 2: Xóa ký tự
```perl
my $string = "hello world";
$string =~ tr/o//d;  # 'd' để chỉ định xóa
print $string;  # Kết quả: "hell wrld"
```

### Ví dụ 3: Thay thế nhiều ký tự
```perl
my $string = "abcde";
$string =~ tr/abc/xyz/;
print $string;  # Kết quả: "xyzde"
```

## Giải thích
Một số điểm cần lưu ý khi sử dụng lệnh `tr///`:
- Lệnh này không hỗ trợ các biểu thức chính quy; nó chỉ làm việc với các ký tự.
- Nếu có bất kỳ ký tự nào trong `old_characters` không có ký tự tương ứng trong `new_characters`, ký tự đó sẽ không bị thay thế.
- Nếu chuỗi đầu vào không chứa ký tự nào trong `old_characters`, chuỗi sẽ không bị thay đổi.

Ngoài ra, lệnh `tr///` hoạt động trực tiếp trên chuỗi gốc và không tạo ra một chuỗi mới, do đó nó có thể tiết kiệm bộ nhớ.

## Tóm tắt một dòng
Lệnh `tr///` trong Perl là công cụ hiệu quả để thay thế hoặc xóa các ký tự trong chuỗi một cách đơn giản và nhanh chóng.