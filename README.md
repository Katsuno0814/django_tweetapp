
```
pictweet % python manage.py shell
```
(InteractiveConsole)

```
>>> from tweets.models import Tweet
>>> from django.utils import timezone
>>> t = Tweet(name= 'takashi' text= "Nice to meet you!")
>>> t.save()
```



レコードに保存をさせたい場合
Django のモデルには create というクラスメソッドがデフォルトで用意されていないため、AttributeError が発生します。
```
 Tweet.create(name= 'sato', text= "Hello world!")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Tweet' has no attribute 'create'
```

このエラーは Tweet クラスに create という属性やメソッドが存在しないことを示しています。しかし、Djangoは .objects.create() というメソッドチェーンを使用して新しいレコードをデータベースに追加する機能を提供しています。

オブジェクトを作成してデータベースに保存するには、以下のコードを使用します：
Tweet.objects.create(name='sato', text="Hello world!")
で作成ができる



ビューファイル
railsのようなapplication.html.erbのファイルやyeildの機能

↓↓↓↓↓↓↓↓
Djangoにおいて、Railsのapplication.html.erbと同様の、全てのテンプレートで共通のレイアウトや要素をデフォルトで読み込んで使用する方法は、ベーステンプレート (Base Template) を使用することで実現できます。

ベーステンプレートの作成
全ページ共通のHTML構造が定義されたベーステンプレートを作成します。例えば、base.htmlという名前のファイルをテンプレートディレクトリに作成し、以下のような基本的なHTML構造を定義します：

```
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
ここで、{% block %}タグは、子テンプレートでオーバーライド（上書き）可能な部分を定義しています。例えば、{% block content %}の中身は各ページ固有のHTMLで上書きされます。

子テンプレートの作成
次に、このベーステンプレートを継承し使用する子テンプレートを作成します。{% extends %}タグを使ってベーステンプレートを指定し、必要なブロックをオーバーライドします：


```
<!-- some_page.html -->
{% extends "base.html" %}

{% block title %}Some Page - My Site{% endblock title %}

{% block content %}
    <!-- このページ独自のコンテンツ -->
    <h1>Some Page</h1>
    <p>This is some specific content for this page.</p>
{% endblock content %}
```
このテンプレートでは、ベーステンプレートのcontentブロックを特定のページ用のコンテンツで上書きしています。

Djangoにおけるyieldメソッドの代替
Railsのyieldメソッドは、ビューの内容（例えば、application.html.erb内の特定の場所で）を動的に描画する役割を持ちます。Djangoでは、これに相当する機能を{% block %}タグが担っており、上記のようにベーステンプレートでブロックを定義し、それらを子テンプレートでオーバーライドすることで、柔軟なテンプレート構造を実現しています。

この方法により、DjangoでもRailsのapplication.html.erbに似た、全ページ共通のレイアウトとページ固有のコンテンツを組み合せた動的なページ生成が可能になります。



Djangoでは
setting.pyで以下のようにプロジェクト直下のtemplatesフォルダを参照するようにする
```
 TEMPLATES = [
    {
        # その他の設定...
        'DIRS': [BASE_DIR / 'templates'],
        # その他の設定...
    },
]
```



cssの読み込み方法
アプリケーション直下にstaticディレクトリを作成し、その中にcssフォルダ/style.cssとする。
base.htmlの記述に
```
    <link rel="stylesheet" href="{% static '/css/style.css' %}">
```

setting.pyにの追加
```
import os

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
```