# [Hệ điều hành Unix] C Shell (csh) chmod: Thay đổi quyền truy cập tệp

## Overview
Lệnh `chmod` trong C Shell (csh) được sử dụng để thay đổi quyền truy cập của các tệp và thư mục. Quyền truy cập này xác định ai có thể đọc, ghi hoặc thực thi tệp.

## Usage
Cú pháp cơ bản của lệnh `chmod` như sau:
```csh
chmod [options] [arguments]
```

## Common Options
- `u`: đại diện cho người sở hữu tệp (user).
- `g`: đại diện cho nhóm người dùng (group).
- `o`: đại diện cho những người khác (others).
- `a`: đại diện cho tất cả (all).
- `+`: thêm quyền.
- `-`: xóa quyền.
- `=`: thiết lập quyền cụ thể.

## Common Examples
- **Thêm quyền ghi cho người sở hữu tệp:**
```csh
chmod u+w filename.txt
```

- **Xóa quyền thực thi cho nhóm:**
```csh
chmod g-x script.sh
```

- **Thiết lập quyền đọc cho tất cả mọi người:**
```csh
chmod a+r document.pdf
```

- **Thêm quyền đọc và ghi cho nhóm và xóa quyền ghi cho người khác:**
```csh
chmod g+rw,o-w file.txt
```

## Tips
- Luôn kiểm tra quyền truy cập hiện tại của tệp trước khi thay đổi bằng lệnh `ls -l`.
- Sử dụng các quyền cụ thể thay vì quyền rộng để bảo mật tốt hơn.
- Hãy cẩn thận khi sử dụng quyền `777`, vì điều này cho phép tất cả mọi người có thể đọc, ghi và thực thi tệp.