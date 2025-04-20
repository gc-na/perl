# [Hệ điều hành Unix] C Shell (csh) wc Cách sử dụng: Đếm số dòng, từ và ký tự trong tệp

## Tổng quan
Lệnh `wc` (word count) trong C Shell được sử dụng để đếm số dòng, số từ và số ký tự trong một tệp. Đây là một công cụ hữu ích để phân tích nội dung tệp văn bản.

## Cách sử dụng
Cú pháp cơ bản của lệnh `wc` như sau:
```
wc [tùy chọn] [đối số]
```

## Tùy chọn phổ biến
- `-l`: Đếm số dòng trong tệp.
- `-w`: Đếm số từ trong tệp.
- `-c`: Đếm số ký tự trong tệp.
- `-m`: Đếm số ký tự (bao gồm cả ký tự đặc biệt).
- `-L`: Hiển thị chiều dài của dòng dài nhất.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `wc`:

1. Đếm số dòng trong một tệp:
   ```bash
   wc -l ten_tap.txt
   ```

2. Đếm số từ trong một tệp:
   ```bash
   wc -w ten_tap.txt
   ```

3. Đếm số ký tự trong một tệp:
   ```bash
   wc -c ten_tap.txt
   ```

4. Đếm số dòng, số từ và số ký tự cùng một lúc:
   ```bash
   wc ten_tap.txt
   ```

5. Đếm chiều dài của dòng dài nhất trong một tệp:
   ```bash
   wc -L ten_tap.txt
   ```

## Mẹo
- Bạn có thể kết hợp nhiều tùy chọn trong một lệnh, ví dụ: `wc -lw ten_tap.txt` để đếm cả số dòng và số từ.
- Sử dụng lệnh `cat` kết hợp với `wc` để đếm nội dung từ nhiều tệp:
  ```bash
  cat tap1.txt tap2.txt | wc
  ```
- Để dễ dàng xử lý kết quả, bạn có thể chuyển hướng đầu ra của lệnh `wc` vào một tệp khác:
  ```bash
  wc ten_tap.txt > ket_qua.txt
  ```