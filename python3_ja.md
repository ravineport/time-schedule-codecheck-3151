# CLIアプリケーション作成方法 (Python3)

codecheckチャレンジの解答をCLIアプリケーションとして作成する方法を教えるよ。

## 必須条件

- Python3（詳しいバージョンについては[ドキュ](https://code-check.github.io/docs/ja/reference_users/#serverside-language-and-tool-versions)を見てね。)
- 標準ライブラリの[`argparse`](https://docs.python.org/3.5/library/argparse.html)モジュール

## 引数の取得
[app.py](app/app.py)では`main`という関数が定義されてる。  
この関数を編集することでCLIアプリケーションが作成できるぞ。  

``` python
def main(args, options):
  for arg in args:
    # 以下の行を自分のコードと置換してね。
    result = arg
```

コマンドライン引数は`args`に配列として渡される。  

オプション形式の引数を使用する場合は[cli.py](cli.py)内で`argparse`の`parser.add_argument`でオプション引数を追加できるよ。

## 結果の出力
`stdout`への出力は標準の`print()`メソッドを使用してね。

``` python
  print(result)
```

## 外部ライブラリの追加方法
外部ライブラリを使用する場合は以下の手順で実施してね。

- [requirements.txt](requirements.txt)にライブラリ名とバージョンを記述
- [codecheck.yml](codecheck.yml)に以下の内容を追加：

``` yaml
build:
  - pip3 install -r requirements.txt
```
