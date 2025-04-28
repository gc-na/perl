<!--
Meta Description: # Đổi Tên Tệp Trong Perl: Hướng Dẫn Sử Dụng Lệnh "rename" ## Tóm Tắt Lệnh `rename` trong Perl được sử dụng để đổi tên các tệp trong hệ thống tệp. Lệnh...
Meta Keywords: đổi, tệp, tên, rename, txt
-->

# Đổi Tên Tệp Trong Perl: Hướng Dẫn Sử Dụng Lệnh "rename"

## Tóm Tắt
Lệnh `rename` trong Perl được sử dụng để đổi tên các tệp trong hệ thống tệp. Lệnh này cho phép người dùng thay đổi tên tệp một cách linh hoạt và hiệu quả thông qua việc sử dụng biểu thức chính quy.

## Tài Liệu
Lệnh `rename` trong Perl thực hiện nhiệm vụ đổi tên tệp. Cú pháp cơ bản của lệnh này là:

```perl
rename (OLDNAME, NEWNAME);
```

### Mục Đích
Lệnh `rename` được sử dụng để thay đổi tên một hoặc nhiều tệp trong thư mục hiện tại hoặc đường dẫn được chỉ định. Nó hỗ trợ thao tác trên nhiều tệp cùng một lúc thông qua việc sử dụng các mẫu.

### Cách Sử Dụng
Để sử dụng lệnh `rename`, bạn cần có quyền truy cập vào tệp mà bạn muốn đổi tên. Bạn có thể chỉ định tên cũ và tên mới của tệp, hoặc sử dụng biểu thức chính quy để thay đổi theo mẫu.

Cú pháp đầy đủ:

```perl
rename 's/old_pattern/new_pattern/' @files;
```

Trong đó:
- `old_pattern`: Mẫu cũ mà bạn muốn thay đổi.
- `new_pattern`: Mẫu mới mà bạn muốn áp dụng.
- `@files`: Danh sách các tệp mà bạn muốn đổi tên.

## Ví Dụ
### Ví Dụ 1: Đổi tên một tệp đơn giản
```perl
rename 'file1.txt', 'file2.txt';
```
Ví dụ này sẽ đổi tên tệp `file1.txt` thành `file2.txt`.

### Ví Dụ 2: Đổi tên nhiều tệp theo mẫu
```perl
rename 's/.txt/.bak/', glob("*.txt");
```
Ví dụ này sẽ đổi tất cả các tệp có đuôi `.txt` thành `.bak`.

### Ví Dụ 3: Thay đổi tên tệp với mẫu phức tạp
```perl
rename 's/^old/new/', 'old_file1.txt', 'old_file2.txt';
```
Ví dụ này sẽ đổi tên `old_file1.txt` thành `new_file1.txt` và `old_file2.txt` thành `new_file2.txt`.

## Giải Thích
Khi sử dụng lệnh `rename`, bạn cần lưu ý một số điều sau:
- Nếu tệp mới đã tồn tại, lệnh sẽ không thực hiện đổi tên và sẽ không có thông báo lỗi.
- Biểu thức chính quy được sử dụng trong lệnh `rename` rất mạnh mẽ, nhưng cũng có thể gây ra lỗi nếu không được viết chính xác.
- Hãy chắc chắn rằng bạn có quyền truy cập vào các tệp mà bạn muốn đổi tên.

## Tóm Tắt Một Dòng
Lệnh `rename` trong Perl cho phép người dùng đổi tên tệp một cách linh hoạt và hiệu quả thông qua việc sử dụng biểu thức chính quy.