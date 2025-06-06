<!--
Meta Description: # Perl 的 "package" 使用指南：了解 Perl 的命名空間 ## 簡介 在 Perl 中，`package` 是用來定義命名空間的關鍵字。它能夠幫助開發者組織代碼，避免名稱衝突，並增強模塊的重用性。 ## 文檔 ### 目的 `package` 關鍵字的主要目的是創建一個新的命名空間...
Meta Keywords: package, perl, mynamespace, use, greet
-->

# Perl 的 "package" 使用指南：了解 Perl 的命名空間

## 簡介
在 Perl 中，`package` 是用來定義命名空間的關鍵字。它能夠幫助開發者組織代碼，避免名稱衝突，並增強模塊的重用性。

## 文檔
### 目的
`package` 關鍵字的主要目的是創建一個新的命名空間，這樣同名的變量、子程序和其他符號可以在不同的上下文中共存。

### 用法
在 Perl 中，使用 `package` 關鍵字來定義一個新的命名空間，語法如下：
```perl
package NamespaceName;
```
定義完命名空間後，所有在該命名空間內聲明的變量和子程序都會屬於這個命名空間。要使用這些符號，您需要指定命名空間或使用 `use` 語句。

### 詳細信息
- **定義命名空間**：每個 `package` 的定義都會影響到後續的代碼，直到遇到另一個 `package` 定義或文件結束。
- **符號表**：`package` 會影響符號表，這意味着在不同的命名空間中，即使名稱相同，對應的變量和子程序也會是不同的。
- **模塊化**：使用 `package` 可以將代碼組織得更為模塊化，這有助於提高代碼的可讀性和可維護性。

## 範例
以下是一些基本的 `package` 使用範例：

### 範例 1：創建一個簡單的命名空間
```perl
package MyNamespace;

sub greet {
    return "Hello from MyNamespace!";
}

1;  # 模塊必須返回真值
```

### 範例 2：使用命名空間
```perl
use MyNamespace;

print MyNamespace::greet();  # 輸出 "Hello from MyNamespace!"
```

## 解釋
- **常見陷阱**：初學者經常忽略在子程序前加上命名空間，這會導致找不到該子程序的錯誤。
- **使用 `::`**：在調用命名空間中的子程序或變量時，必須使用 `::` 符號來指定完整的名稱。
- **影響範圍**：在一個 `package` 內部聲明的變量如果沒有使用 `my` 或 `our`，會變為全局變量，這可能會導致意外的名稱衝突。

## 一句總結
`package` 在 Perl 中用於創建命名空間，幫助開發者組織代碼並避免名稱衝突。