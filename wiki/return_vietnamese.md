<!--
Meta Description: # Lệnh "return" trong Perl: Cách sử dụng và ý nghĩa ## Tóm tắt Lệnh `return` trong Perl được sử dụng để trả về giá trị từ một hàm, giúp kết thúc thực ...
Meta Keywords: hàm, return, trả, giá, trị
-->

# Lệnh "return" trong Perl: Cách sử dụng và ý nghĩa

## Tóm tắt
Lệnh `return` trong Perl được sử dụng để trả về giá trị từ một hàm, giúp kết thúc thực thi hàm và gửi kết quả về nơi gọi hàm. 

## Tài liệu
### Mục đích
Lệnh `return` cho phép lập trình viên định nghĩa giá trị mà hàm sẽ trả về sau khi hoàn thành thực hiện. Đây là một phần quan trọng trong việc xây dựng các hàm có thể tái sử dụng và trả về kết quả cho các thao tác khác trong chương trình.

### Cách sử dụng
- **Cú pháp cơ bản**: 
  ```perl
  sub ten_ham {
      # logic ở đây
      return $giatri; # trả về giá trị
  }
  ```

- **Trả về nhiều giá trị**:
  Một hàm có thể trả về nhiều giá trị bằng cách sử dụng một danh sách:
  ```perl
  sub tra_ve_hai_giatri {
      return ($giatri1, $giatri2);
  }
  ```

- **Hàm không có lệnh return**: Nếu không sử dụng lệnh `return`, hàm sẽ trả về giá trị cuối cùng được tính toán hoặc `undef` nếu không có giá trị nào được tính toán.

### Chi tiết
- Khi `return` được gọi, hàm sẽ ngay lập tức dừng lại và trả về giá trị cho nơi gọi.
- Nếu không có giá trị nào được chỉ định trong lệnh `return`, hàm sẽ trả về giá trị `undef`.
- Lệnh `return` có thể được sử dụng ở bất kỳ vị trí nào trong hàm, nhưng một khi nó được thực thi, hàm sẽ không tiếp tục chạy mã phía sau.
- Việc sử dụng `return` không chỉ giúp lấy giá trị ra ngoài hàm mà còn có thể giúp kiểm soát luồng thực thi.

## Ví dụ
### Ví dụ đơn giản
```perl
sub tinh_tong {
    my ($a, $b) = @_;
    return $a + $b; # trả về tổng của hai tham số
}

my $result = tinh_tong(5, 10);
print "Tổng là: $result\n"; # Kết quả: Tổng là: 15
```

### Ví dụ trả về nhiều giá trị
```perl
sub tra_ve_hai_giatri {
    my ($a, $b) = @_;
    return ($a + $b, $a * $b); # trả về tổng và tích
}

my ($tong, $tich) = tra_ve_hai_giatri(5, 10);
print "Tổng: $tong, Tích: $tich\n"; # Kết quả: Tổng: 15, Tích: 50
```

## Giải thích
- **Lỗi phổ biến**: Một số lập trình viên mới có thể quên sử dụng lệnh `return`, dẫn đến việc hàm không trả về giá trị như mong muốn. Điều này có thể gây nhầm lẫn khi kiểm tra giá trị trả về.
- **Kiểm soát luồng**: Sử dụng `return` để kiểm soát luồng thực thi trong hàm. Nếu có điều kiện mà bạn muốn dừng hàm sớm, bạn có thể sử dụng `return` để kết thúc hàm ngay lập tức.
- **Return trong vòng lặp**: Nếu sử dụng `return` trong vòng lặp, hàm sẽ kết thúc ngay lập tức và không tiếp tục lặp lại.

## Tóm tắt một câu
Lệnh `return` trong Perl được sử dụng để trả về giá trị từ một hàm, giúp kết thúc thực thi hàm và gửi kết quả về nơi gọi hàm.