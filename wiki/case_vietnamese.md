# [Hệ điều hành] C Shell (csh) case <Sử dụng tương đương>: Xử lý điều kiện

## Tổng quan
Lệnh `case` trong C Shell (csh) được sử dụng để thực hiện các phép kiểm tra điều kiện, cho phép thực thi các lệnh khác nhau dựa trên giá trị của một biến. Nó tương tự như cấu trúc `switch` trong các ngôn ngữ lập trình khác.

## Cú pháp
Cú pháp cơ bản của lệnh `case` như sau:
```csh
case [biến] in
    [mẫu1])
        [lệnh1]
        ;;
    [mẫu2])
        [lệnh2]
        ;;
    ...
esac
```

## Các tùy chọn phổ biến
- `in`: Chỉ định các mẫu mà biến sẽ được so sánh.
- `;;`: Kết thúc một khối lệnh cho một mẫu.
- `esac`: Kết thúc lệnh `case`.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `case`:

### Ví dụ 1: Kiểm tra biến
```csh
set fruit = "apple"
case $fruit in
    apple)
        echo "Đây là một quả táo."
        ;;
    banana)
        echo "Đây là một quả chuối."
        ;;
    *)
        echo "Đây không phải là táo hay chuối."
        ;;
esac
```

### Ví dụ 2: Phân loại số
```csh
set number = 3
case $number in
    1)
        echo "Số là một."
        ;;
    2)
        echo "Số là hai."
        ;;
    3)
        echo "Số là ba."
        ;;
    *)
        echo "Số không nằm trong phạm vi từ 1 đến 3."
        ;;
esac
```

### Ví dụ 3: Kiểm tra phần mở rộng tệp
```csh
set file = "document.txt"
case $file in
    *.txt)
        echo "Đây là một tệp văn bản."
        ;;
    *.jpg)
        echo "Đây là một tệp hình ảnh."
        ;;
    *)
        echo "Đây là một loại tệp khác."
        ;;
esac
```

## Mẹo
- Sử dụng dấu `*` trong mẫu để khớp với bất kỳ chuỗi nào, giúp linh hoạt hơn trong việc kiểm tra.
- Đảm bảo rằng mỗi khối lệnh kết thúc bằng `;;` để tránh lỗi cú pháp.
- Sử dụng `esac` để kết thúc lệnh `case`, tương tự như `end` trong một số ngôn ngữ lập trình khác.