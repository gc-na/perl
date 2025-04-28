<!--
Meta Description: # Perl 的 gmtime 函數：全方位指南 ## 簡介 `gmtime` 是 Perl 中的一個內建函數，用於獲取格林威治標準時間（GMT）的時間結構，提供將 Unix 時間戳轉換為可讀的時間格式的功能。 ## 文檔 ### 目的 `gmtime` 函數的主要目的是將一個 Unix 時間戳（即...
Meta Keywords: gmtime, gmt, current_gmt, perl, unix
-->

# Perl 的 gmtime 函數：全方位指南

## 簡介
`gmtime` 是 Perl 中的一個內建函數，用於獲取格林威治標準時間（GMT）的時間結構，提供將 Unix 時間戳轉換為可讀的時間格式的功能。

## 文檔
### 目的
`gmtime` 函數的主要目的是將一個 Unix 時間戳（即從1970年1月1日00:00:00 UTC開始的秒數）轉換為 GMT 時間結構，並返回一個包含年、月、日、時、分、秒等信息的列表。

### 使用方法
```perl
my @time = gmtime($epoch_time);
```
- `$epoch_time`：可選參數。如果不提供，`gmtime` 會使用當前時間。
- 返回值：一個包含時間信息的列表，順序為：秒、分鐘、小時、日、月、年（從1900年開始）。

### 詳細說明
- 當使用 `gmtime` 時，返回的年份是從1900年開始計算的。因此，若要獲取當前年份，需加上1900。
- 月的範圍是從0（1月）到11（12月）。
- 函數返回的時間信息是基於 UTC（協調世界時），而不是本地時間。

## 範例
以下是一些使用 `gmtime` 的基本範例：

### 範例 1：獲取當前 GMT 時間
```perl
my @current_gmt = gmtime();
print "Current GMT: $current_gmt[5]+1900-$current_gmt[4]+1-$current_gmt[3] $current_gmt[2]:$current_gmt[1]:$current_gmt[0]\n";
```

### 範例 2：轉換特定 Unix 時間戳
```perl
my $timestamp = 1633072800; # 2021-10-01 00:00:00 UTC
my @gmt = gmtime($timestamp);
print "GMT Time: $gmt[5]+1900-$gmt[4]+1-$gmt[3] $gmt[2]:$gmt[1]:$gmt[0]\n";
```

## 解釋
- **常見陷阱**：使用 `gmtime` 時，初學者常常忽略了年份需加1900，導致年份顯示錯誤。
- **注意事項**：`gmtime` 返回的時間是 UTC 時間，若需要本地時間，應使用 `localtime` 函數。

## 一句總結
`gmtime` 是 Perl 中用於將 Unix 時間戳轉換為格林威治標準時間格式的重要函數。