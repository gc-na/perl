# [日本] C Shell (csh) rsync 使用法: ファイルの同期と転送

## 概要
`rsync` コマンドは、ファイルやディレクトリを効率的に同期させたり転送したりするためのツールです。ネットワーク越しやローカル間でのデータのバックアップやミラーリングに広く使用されています。

## 使用法
基本的な構文は以下の通りです。

```bash
rsync [オプション] [引数]
```

## 一般的なオプション
- `-a` : アーカイブモード。ファイルの属性を保持しつつ、再帰的にコピーします。
- `-v` : 詳細モード。進行状況を表示します。
- `-z` : 転送中にデータを圧縮します。
- `-r` : ディレクトリを再帰的にコピーします。
- `--delete` : 送信先に存在しないファイルを削除します。

## 一般的な例
以下に、`rsync` コマンドの実用的な例をいくつか示します。

### 1. ローカルディレクトリの同期
```bash
rsync -av /path/to/source/ /path/to/destination/
```

### 2. リモートサーバーへのファイル転送
```bash
rsync -avz /path/to/local/file user@remote_host:/path/to/remote/destination/
```

### 3. リモートサーバーからのファイル取得
```bash
rsync -avz user@remote_host:/path/to/remote/file /path/to/local/destination/
```

### 4. 不要なファイルの削除を含む同期
```bash
rsync -av --delete /path/to/source/ /path/to/destination/
```

## ヒント
- `-n` オプションを使用すると、実際の転送を行わずに何が行われるかを確認できます。
- 大きなファイルを転送する際は、`-z` オプションを使用して転送速度を向上させることができます。
- 定期的なバックアップには、`cron` ジョブを設定して自動化することを検討してください。