# github-actions-template-python
template project for python with github actions

# 前提条件

- poetry環境構築
- act環境構築
- dockerデーモンの起動

## poetry環境構築

https://qiita.com/ksato9700/items/b893cf1db83605898d8a
https://cocoatomo.github.io/poetry-ja/basic-usage/

## act環境構築

https://gauravgahlot.in/blog/run-github-actions-locally-docker-nektos-act/
https://gauravgahlot.in/blog/run-github-actions-locally-docker-nektos-act/

## dockerデーモンの起動

sudo service docker start

# テンプレートでのテスト

1. git clone
2. poetry install
3. poetry run pytest
4. act
