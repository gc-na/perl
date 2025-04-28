<!--
Meta Description: # Perl 中的 "sub" 函數：創建和使用子程序的完整指南 ## 簡介 在 Perl 程式設計中，`sub` 是用來定義子程序（Subroutine）的一個關鍵字。子程序是一段可重用的代碼，能夠執行特定的任務，並且可以在程式中的多個地方調用。 ## 文檔 ### 目的 `sub` 的主要目的是...
Meta Keywords: perl, sub, return, print, square
-->

# Perl 中的 "sub" 函數：創建和使用子程序的完整指南

## 簡介
在 Perl 程式設計中，`sub` 是用來定義子程序（Subroutine）的一個關鍵字。子程序是一段可重用的代碼，能夠執行特定的任務，並且可以在程式中的多個地方調用。

## 文檔
### 目的
`sub` 的主要目的是促進代碼的模組化和重用。透過使用子程序，程式員可以將複雜的邏輯分解為較小的、易於管理的部分。

### 用法
在 Perl 中，創建子程序的語法如下：

```perl
sub subroutine_name {
    # 子程序的代碼
}
```

要調用子程序，只需使用其名稱：

```perl
subroutine_name();
```

### 詳情
- **參數傳遞**：子程序可以接受參數，這些參數通常通過 `@_` 數組來訪問。
  
  ```perl
  sub greet {
      my ($name) = @_;
      print "Hello, $name!\n";
  }
  
  greet("Alice");
  ```

- **返回值**：子程序可以返回值，使用 `return` 語句。

  ```perl
  sub add {
      my ($a, $b) = @_;
      return $a + $b;
  }
  
  my $result = add(2, 3);
  ```

- **作用域**：子程序的變量作用域通常是局部的，除非使用 `our` 或 `global`。

## 示例
以下是一些基本的子程序使用示例：

1. **簡單的子程序定義與調用**：

    ```perl
    sub say_hello {
        print "Hello, World!\n";
    }

    say_hello();
    ```

2. **帶參數的子程序**：

    ```perl
    sub square {
        my ($num) = @_;
        return $num * $num;
    }

    my $sq = square(4);
    print "Square: $sq\n";  # 輸出 Square: 16
    ```

3. **帶返回值的子程序**：

    ```perl
    sub multiply {
        my ($x, $y) = @_;
        return $x * $y;
    }

    my $product = multiply(5, 6);
    print "Product: $product\n";  # 輸出 Product: 30
    ```

## 解釋
在使用 `sub` 定義子程序時，常見的問題包括：

- **作用域問題**：確保理解變量的作用域，尤其是在使用全局變量時，避免意外修改。
- **參數未正確傳遞**：檢查在調用子程序時是否傳遞了正確數量的參數。
- **返回值的使用**：注意在子程序中使用 `return` 返回值，並在調用時正確處理。

## 一句總結
`sub` 是 Perl 中定義和使用子程序的關鍵字，能夠促進代碼的重用和模組化。