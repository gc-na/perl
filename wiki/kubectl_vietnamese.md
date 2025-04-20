# [Hệ điều hành] C Shell (csh) kubectl Sử dụng: Quản lý Kubernetes

## Tổng quan
Lệnh `kubectl` là công cụ dòng lệnh chính để quản lý các cụm Kubernetes. Nó cho phép người dùng triển khai ứng dụng, kiểm tra và quản lý trạng thái của các tài nguyên trong cụm Kubernetes.

## Cú pháp
Cú pháp cơ bản của lệnh `kubectl` như sau:
```
kubectl [options] [arguments]
```

## Tùy chọn phổ biến
- `get`: Lấy thông tin về các tài nguyên trong cụm.
- `apply`: Áp dụng các thay đổi từ một tệp cấu hình.
- `delete`: Xóa một tài nguyên cụ thể.
- `describe`: Hiển thị thông tin chi tiết về một tài nguyên.
- `logs`: Lấy nhật ký của một pod.

## Ví dụ phổ biến
- Lấy danh sách tất cả các pod trong cụm:
  ```bash
  kubectl get pods
  ```

- Áp dụng một tệp cấu hình YAML:
  ```bash
  kubectl apply -f deployment.yaml
  ```

- Xóa một pod cụ thể:
  ```bash
  kubectl delete pod <tên-pod>
  ```

- Hiển thị thông tin chi tiết về một dịch vụ:
  ```bash
  kubectl describe service <tên-dịch-vụ>
  ```

- Lấy nhật ký của một pod:
  ```bash
  kubectl logs <tên-pod>
  ```

## Mẹo
- Sử dụng `kubectl get all` để lấy thông tin về tất cả các tài nguyên trong không gian tên hiện tại.
- Thêm `-n <tên-không-gian-tên>` để chỉ định không gian tên cụ thể khi thực hiện các lệnh.
- Sử dụng `--help` với bất kỳ lệnh nào để xem hướng dẫn và các tùy chọn có sẵn.