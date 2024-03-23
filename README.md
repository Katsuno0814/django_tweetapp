# 基本的なコマンドをメモ程度に残しました。

# Djangoプロジェクトのはじめ方

## Djangoのインストールとプロジェクトの作成

公式のチュートリアル：
[https://docs.djangoproject.com/ja/5.0/intro/tutorial01/](https://docs.djangoproject.com/ja/5.0/intro/tutorial01/)

1. **プロジェクトを作成**

    ```bash
    django-admin startproject プロジェクトアプリ名
    ```

2. **開発サーバを起動**

    ```bash
    python manage.py runserver
    ```

3. **新しいアプリケーションを作成**

    ```bash
    python manage.py startapp アプリ名(機能名)
    ```

## データベースのマイグレーション

1. **マイグレーションファイルの作成**

    ```bash
    python manage.py makemigrations
    ```

2. **マイグレーションの適用**

    ```bash
    python manage.py migrate
    ```

## Django Extensionsの導入

```bash
pip3 install django-extensions
```

`settings.py`に追加：

```python
INSTALLED_APPS = [
    'django_extensions',
    # 他のインストールされたアプリケーション
]
```

使用例：

```bash
python manage.py show_urls
```

## モデルの操作

1. **Djangoシェルを起動**

    ```bash
    python manage.py shell
    ```

2. **モデルからオブジェクトを作成して保存**

    ```python
    >>> from tweets.models import Tweet
    >>> from django.utils import timezone
    >>> t = Tweet(name='takashi', text="Nice to meet you!")
    >>> t.save()
    ```

3. **オブジェクトの作成と保存を一度に行う**

    ```python
    >>> Tweet.objects.create(name='sato', text="Hello world!")
    ```

## テンプレート

### ベーステンプレートの作成

`base.html`を作成して、すべてのページの共通レイアウトを定義します。

```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock title %}</title>
    {% block extra_head %}{% endblock extra_head %}
</head>
<body>
    <header>
        <!-- 全ページ共通のヘッダーコンテンツ -->
    </header>

    <main>
        {% block content %}{% endblock content %}
    </main>

    <footer>
        <!-- 全ページ共通のフッターコンテンツ -->
    </footer>

    {% block extra_js %}{% endblock extra_js %}
</body>
</html>
```

### 子テンプレートの作成

`{% extends "base.html" %}`を使用して、ベーステンプレートを拡張します。

```html
<!-- some_page.html -->
{% extends "base.html" %}

{% block title %}Some Page - My Site{% endblock title %}

{% block content %}
    <!-- このページ独自のコンテンツ -->
{% endblock content %}
```
