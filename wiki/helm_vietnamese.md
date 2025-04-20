# [Hệ điều hành] C Shell (csh) helm <Sử dụng tương đương>: Quản lý các gói ứng dụng Kubernetes

## Tổng quan
Lệnh `helm` là một công cụ quản lý gói cho Kubernetes, giúp người dùng dễ dàng cài đặt, nâng cấp và quản lý các ứng dụng trên nền tảng Kubernetes thông qua các biểu đồ (charts).

## Cách sử dụng
Cú pháp cơ bản của lệnh `helm` như sau:
```shell
helm [options] [arguments]
```

## Các tùy chọn phổ biến
- `install`: Cài đặt một biểu đồ mới.
- `upgrade`: Nâng cấp một biểu đồ đã cài đặt.
- `uninstall`: Gỡ bỏ một biểu đồ đã cài đặt.
- `list`: Liệt kê các biểu đồ đã cài đặt.
- `repo`: Quản lý các kho biểu đồ.

## Ví dụ phổ biến
- Cài đặt một biểu đồ:
```shell
helm install my-release my-chart
```
- Nâng cấp một biểu đồ:
```shell
helm upgrade my-release my-chart
```
- Gỡ bỏ một biểu đồ:
```shell
helm uninstall my-release
```
- Liệt kê các biểu đồ đã cài đặt:
```shell
helm list
```
- Thêm một kho biểu đồ mới:
```shell
helm repo add my-repo https://example.com/charts
```

## Mẹo
- Luôn kiểm tra phiên bản của biểu đồ trước khi nâng cấp để đảm bảo tính tương thích.
- Sử dụng các nhãn (labels) để quản lý các biểu đồ một cách hiệu quả hơn.
- Đọc tài liệu của biểu đồ để hiểu rõ các tùy chọn cấu hình có sẵn.