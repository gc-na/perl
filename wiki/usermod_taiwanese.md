# [台灣] C Shell (csh) usermod 使用法: 修改使用者帳號資訊

## Overview
`usermod` 命令用於修改現有使用者帳號的屬性，例如更改使用者的家目錄、使用者名稱或群組等。

## Usage
基本語法如下：
```csh
usermod [options] [arguments]
```

## Common Options
- `-l <new_username>`: 更改使用者名稱。
- `-d <new_home>`: 更改使用者的家目錄。
- `-g <new_group>`: 更改使用者的主要群組。
- `-aG <group>`: 將使用者添加到附加群組中。
- `-s <shell>`: 更改使用者的默認 shell。

## Common Examples
以下是一些常見的使用範例：

1. 更改使用者名稱：
   ```csh
   usermod -l newusername oldusername
   ```

2. 更改使用者的家目錄：
   ```csh
   usermod -d /new/home/directory username
   ```

3. 更改使用者的主要群組：
   ```csh
   usermod -g newgroup username
   ```

4. 將使用者添加到附加群組：
   ```csh
   usermod -aG additionalgroup username
   ```

5. 更改使用者的默認 shell：
   ```csh
   usermod -s /bin/zsh username
   ```

## Tips
- 在執行 `usermod` 命令之前，建議先備份使用者的資料。
- 確保在更改使用者名稱或家目錄後，更新相關的權限和擁有者設定。
- 使用 `usermod` 命令時，通常需要具有管理員權限。