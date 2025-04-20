# [Hệ điều hành] C Shell (csh) parted Cách sử dụng: Quản lý phân vùng đĩa

## Tổng quan
Lệnh `parted` trong C Shell (csh) được sử dụng để quản lý các phân vùng trên đĩa cứng. Nó cho phép người dùng tạo, xóa, thay đổi kích thước và quản lý các phân vùng một cách dễ dàng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `parted` như sau:

```csh
parted [options] [arguments]
```

## Các tùy chọn phổ biến
- `-l` : Liệt kê tất cả các thiết bị lưu trữ và phân vùng.
- `mklabel` : Tạo một nhãn phân vùng mới cho đĩa.
- `mkpart` : Tạo một phân vùng mới.
- `rm` : Xóa một phân vùng.
- `resizepart` : Thay đổi kích thước của một phân vùng.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `parted`:

1. **Liệt kê các phân vùng:**
   ```csh
   parted -l
   ```

2. **Tạo nhãn phân vùng mới:**
   ```csh
   parted /dev/sda mklabel gpt
   ```

3. **Tạo một phân vùng mới:**
   ```csh
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

4. **Xóa một phân vùng:**
   ```csh
   parted /dev/sda rm 1
   ```

5. **Thay đổi kích thước của một phân vùng:**
   ```csh
   parted /dev/sda resizepart 1 200MiB
   ```

## Mẹo
- Trước khi thực hiện bất kỳ thay đổi nào, hãy sao lưu dữ liệu quan trọng để tránh mất mát.
- Sử dụng lệnh `print` trong `parted` để xem thông tin chi tiết về các phân vùng trước khi thực hiện thay đổi.
- Hãy cẩn thận khi xóa hoặc thay đổi kích thước phân vùng, vì điều này có thể ảnh hưởng đến dữ liệu trên đĩa.