<!--
Meta Description: # Perl 中的 readdir 函數：從資料夾讀取檔案名稱 ## Synopsis `readdir` 是 Perl 提供的一個函數，用來從指定的資料夾讀取檔案名稱，並以列表的形式返回。 ## Documentation `readdir` 函數的主要用途是從已經打開的資料夾句柄中讀取檔案名稱。...
Meta Keywords: readdir, dir, opendir, perl, directory
-->

# Perl 中的 readdir 函數：從資料夾讀取檔案名稱

## Synopsis
`readdir` 是 Perl 提供的一個函數，用來從指定的資料夾讀取檔案名稱，並以列表的形式返回。

## Documentation
`readdir` 函數的主要用途是從已經打開的資料夾句柄中讀取檔案名稱。這個函數非常適合用於檔案管理和資料夾內容遍歷。

### 用法
```perl
opendir(my $dir, $directory) or die "無法打開資料夾: $!";
my @files = readdir($dir);
closedir($dir);
```
在這段程式碼中，`opendir` 函數用來打開指定的資料夾，而 `readdir` 函數則會讀取該資料夾中的所有檔案名稱。最後，`closedir` 函數用來關閉資料夾句柄。

### 詳細說明
- **引數**：`readdir` 函數接收一個資料夾句柄作為參數。
- **返回值**：返回資料夾中所有檔案和子資料夾的名稱（不包括 `.` 和 `..`）。
- **錯誤處理**：若資料夾未能正確打開，`opendir` 將會返回錯誤，並且可以使用 `die` 函數來顯示錯誤信息。

## Examples
### 基本範例
以下是使用 `readdir` 的一個簡單例子：
```perl
use strict;
use warnings;

my $directory = 'your_directory_path';
opendir(my $dir, $directory) or die "無法打開資料夾: $!";
my @files = readdir($dir);
closedir($dir);

print "資料夾中的檔案:\n";
print "$_\n" for @files;
```

### 過濾檔案
如果只想要特定類型的檔案，可以加上條件過濾：
```perl
use strict;
use warnings;

my $directory = 'your_directory_path';
opendir(my $dir, $directory) or die "無法打開資料夾: $!";
my @files = grep { /\.txt$/ } readdir($dir);
closedir($dir);

print "資料夾中的文本檔案:\n";
print "$_\n" for @files;
```

## Explanation
- **常見陷阱**：如果未能正確打開資料夾，`readdir` 將無法執行，這會導致程式錯誤。確保使用 `opendir` 前，資料夾的路徑是正確的。
- **不返回隱藏檔案**：`readdir` 會返回所有檔案，但需注意，如果資料夾中有隱藏檔案（以 `.` 開頭），這些檔案會被包含在返回列表中。

## One Line Summary
`readdir` 函數用於從已打開的資料夾讀取檔案名稱，並返回檔案列表。