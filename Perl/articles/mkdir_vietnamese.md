<!--
Meta Description: # Hướng dẫn sử dụng lệnh mkdir trong Perl ## Tóm tắt Lệnh `mkdir` trong Perl được sử dụng để tạo thư mục mới trong hệ thống file của máy tính, giúp qu...
Meta Keywords: mục, thư, tạo, lệnh, mkdir
-->

# Hướng dẫn sử dụng lệnh mkdir trong Perl

## Tóm tắt
Lệnh `mkdir` trong Perl được sử dụng để tạo thư mục mới trong hệ thống file của máy tính, giúp quản lý và tổ chức các tệp tin một cách hiệu quả.

## Tài liệu
Lệnh `mkdir` trong Perl là một hàm quan trọng trong việc quản lý hệ thống file. Mục đích chính của lệnh này là tạo ra một thư mục mới với tên xác định. Cú pháp cơ bản của lệnh `mkdir` như sau:

```perl
mkdir(DIRNAME, MODE);
```

- **DIRNAME**: Tên thư mục mà bạn muốn tạo. Đây là một chuỗi ký tự và có thể bao gồm đường dẫn đầy đủ hoặc chỉ tên thư mục.
- **MODE**: (Tùy chọn) Đây là quyền truy cập cho thư mục mới, được chỉ định dưới dạng một số octal (ví dụ: 0755). Nếu không chỉ định, quyền truy cập mặc định sẽ được áp dụng.

### Sử dụng
Để sử dụng lệnh `mkdir`, bạn cần đảm bảo rằng bạn có quyền tạo thư mục trong vị trí mà bạn đang làm việc. Nếu thư mục đã tồn tại, lệnh sẽ không tạo thư mục mới và có thể trả về thông báo lỗi.

## Ví dụ
Dưới đây là một vài ví dụ đơn giản về cách sử dụng lệnh `mkdir` trong Perl:

### Ví dụ 1: Tạo một thư mục đơn giản
```perl
use strict;
use warnings;

my $dir_name = 'thumuc_moi';
mkdir $dir_name or die "Không thể tạo thư mục '$dir_name': $!";
print "Thư mục '$dir_name' đã được tạo thành công.\n";
```

### Ví dụ 2: Tạo thư mục với quyền truy cập
```perl
use strict;
use warnings;

my $dir_name = 'thumuc_bao_mat';
my $mode = 0755; # Quyền truy cập

mkdir $dir_name, $mode or die "Không thể tạo thư mục '$dir_name': $!";
print "Thư mục '$dir_name' với quyền $mode đã được tạo thành công.\n";
```

## Giải thích
Khi sử dụng lệnh `mkdir`, có một số vấn đề phổ biến mà bạn có thể gặp phải:

- **Thư mục đã tồn tại**: Nếu thư mục bạn cố gắng tạo đã tồn tại, lệnh sẽ không thành công và trả về một thông báo lỗi.
- **Quyền truy cập**: Bạn cần có quyền ghi trong thư mục cha để có thể tạo thư mục mới. Nếu không, lệnh sẽ thất bại.
- **Đường dẫn không hợp lệ**: Đảm bảo rằng đường dẫn bạn cung cấp cho `mkdir` là hợp lệ và không chứa ký tự đặc biệt không được phép.

## Tóm tắt một dòng
Lệnh `mkdir` trong Perl cho phép bạn tạo thư mục mới trong hệ thống file, giúp tổ chức và quản lý tệp tin một cách hiệu quả.