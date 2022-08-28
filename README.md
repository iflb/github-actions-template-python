# 概要

GitHub Actionでのテストフレームワーク及びpip化を実行する場合の問題を解決するためのテンプレート提供

- テストエラー発生によってリポジトリを汚すことを避ける →　actを使用
- パッケージ管理、実行環境、テスト環境の統一 →　poetry + pytestを使用
- テスト用サービス（RDBMSやRedis、Ducts）の起動方法の統一　→ Dockerコンテナを使用

act+Dockerを使用することで、GitHub Actionsとローカルの実行を同じworkflowで実行可能となる

参考：

- https://dev.classmethod.jp/articles/act-for-github-actions-local-execution-tool/
- https://myenigma.hatenablog.com/entry/2021/01/31/212743
- https://qiita.com/sk217/items/43c994640f4843a18dbe

## 内容

- ${ROOT}/.github/workflows/以下: GitHubActions用workflowファイル
- ${ROOT}/github_actions_template_python/__init__.py: テスト対象のファイル
- ${ROOT}/tests/__init__.py: pytest用テストファイル

## 本パッケージの基本的な使い方

- workflowファイルの雛形としての使用（coしたファイルをコピーして使用）
- パッケージ構成の参考（poetry newで作った構成と同じ）

# 環境構築

下記環境を事前に構築する必要があります。

- pyenv環境構築
- poetry環境構築
- act環境構築
- dockerデーモンの起動

## poetry環境構築

- https://qiita.com/ksato9700/items/b893cf1db83605898d8a
- https://cocoatomo.github.io/poetry-ja/basic-usage/

## act環境構築

- https://gauravgahlot.in/blog/run-github-actions-locally-docker-nektos-act/
- https://github.com/nektos/act/blob/master/README.md

## dockerデーモンの起動

sudo service docker start

# テンプレートでのテスト

1. git clone
2. poetry install
3. poetry run pytest
4. act

## act w/ Redisコンテナ

1. docker start redis
2. act -j container-job
