<!--
Meta Description: # Perl 的 "rename" 命令：檔案重命名的最佳工具 ## 概要 在 Perl 中，`rename` 命令是一個用於改變檔案名稱的函數。它提供了一種簡單有效的方法來批量重命名檔案，特別適合需要處理大量檔案的情況。 ## 文檔 `rename` 函數的主要目的在於更改檔案名稱。此函數的基本語...
Meta Keywords: rename, new_file, perl, txt, use
-->

# Perl 的 "rename" 命令：檔案重命名的最佳工具

## 概要
在 Perl 中，`rename` 命令是一個用於改變檔案名稱的函數。它提供了一種簡單有效的方法來批量重命名檔案，特別適合需要處理大量檔案的情況。

## 文檔
`rename` 函數的主要目的在於更改檔案名稱。此函數的基本語法如下：

```perl
rename( $oldname, $newname )
```

### 參數：
- `$oldname`：原始檔案名稱（可以是相對路徑或絕對路徑）。
- `$newname`：新的檔案名稱。

### 使用方法：
1. 確保檔案存在於指定路徑。
2. 呼叫 `rename` 函數並傳入舊檔案名稱和新檔案名稱。
3. 檢查返回值以確認重命名是否成功。

### 返回值：
`rename` 函數會在成功時返回真（true），失敗時返回假（false），並可能設置 `$!` 變數以指示錯誤原因。

## 示例
這裡是一些基本的使用示例：

### 示例 1：單個檔案重命名
```perl
use strict;
use warnings;

my $old_file = 'old_name.txt';
my $new_file = 'new_name.txt';

if (rename($old_file, $new_file)) {
    print "檔案已成功重命名為 $new_file\n";
} else {
    warn "重命名失敗: $!";
}
```

### 示例 2：批量重命名
```perl
use strict;
use warnings;

foreach my $file (glob("*.txt")) {
    my $new_file = $file;
    $new_file =~ s/\.txt$/_backup.txt/; # 在檔案名後添加 "_backup"
    
    if (rename($file, $new_file)) {
        print "檔案 $file 已重命名為 $new_file\n";
    } else {
        warn "重命名失敗: $!";
    }
}
```

## 解釋
使用 `rename` 函數時，使用者需要注意以下幾點：
- **檔案路徑**：確保提供的檔案路徑正確，否則會導致重命名失敗。
- **權限問題**：如果沒有足夠的權限來修改檔案，`rename` 會失敗。
- **覆蓋檔案**：如果新的檔案名稱已經存在，`rename` 會覆蓋該檔案，這可能導致資料丟失，因此在執行之前務必確認。

## 一句話總結
Perl 的 `rename` 命令是一個強大的工具，可用於簡單而有效的檔案重命名，適合批量操作和個別檔案的處理。