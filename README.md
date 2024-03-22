
Django のプロジェクト (project) を構成するコードを自動生成します。プロジェクトとは、データベースの設定や Django 固有のオプション、アプリケーション固有の設定などといった、個々の Django インスタンスの設定を集めたものです。

```
django-admin startproject プロジェクトアプリ名

python manage.py runserver

python manage.py startapp アプリ名(機能名)

```

マイグレーションファイル
```
python manage.py makemigrations
python manage.py migrate

```

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



新規投稿

Djangoでのフォームのカスタマイズ
ModelFormを使うことで、モデルに基づいたフォームをカスタマイズして作成することができます。このフォームクラスは、モデルから直接フォームフィールドを生成し、さらにその表示や振る舞いを調整するために使われます。

以下はTweetモデルに対するカスタムフォームを作成する例です。forms.pyファイルをプロジェクトに追加（または編集）して、下記のように記載します。


コピーする
from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['name', 'image', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nickname'}),
            'text': forms.Textarea(attrs={'placeholder': 'Text', 'rows': 4}),
        }
        labels = {
            'name': 'ニックネーム',
            'image': '画像URL',
            'text': 'テキスト',
        }
このフォームクラスでは、Metaサブクラスを通してどのモデルが対象であるか、そしてどのフィールドがフォームに含まれるべきかをDjangoに伝えます。さらに、widgets属性を用いて特定のフィールド（この場合はnameとtext）のHTML表示をカスタマイズしています。


DjangoでRESTfulにする
Djangoでは、CreateViewは新しいオブジェクトを作成するためのフォームを表示（getリクエスト）し、提供されたデータを使用してオブジェクトを保存（postリクエスト）します。つまり、CreateViewはRailsのnewアクション（フォームを表示）とcreateアクション（データを保存）の両方の機能を内包しています。

しかし、よりRESTfulな設計を望む場合、たとえば、フォーム表示とデータの保存を明確に分けたい場合は、フレームワークに依存せずにビュー関数やクラスベースビューを使ってこれらのアクションを別々に定義することができます。


コピーする
from django.views.generic.edit import FormView
from .forms import TweetForm

class TweetNewView(FormView):
    template_name = 'tweet_new.html'
    form_class = TweetForm
    success_url = '/tweet/success/'

    def form_valid(self, form):
        # ここでフォームのデータを保存するロジックを書く
        return super().form_valid(form)



CreateView はDjangoにおいて汎用的なクラスベースビューの一つであり、それを直接使うのではなく、あなた自身のモデルに対応したビューを定義して使用するべきです。例えば、Tweetモデルがあるとして、そのモデル用のクリエイトビューを定義する場合は、次のように書きます：


コピーする
from django.views.generic.edit import CreateView
from .models import Tweet

class TweetCreateView(CreateView):
    model = Tweet
    fields = ['name', 'image', 'text']  # あなたがフォームで使用したいフィールド
    template_name = 'tweet_form.html'   # フォームのテンプレート
    success_url = reverse_lazy('home')  # 投稿後にリダイレクトするURL

reverse_lazy関数に正しいURLパターンの名前を引数として渡す必要があります。たとえば、フォームの送信後にユーザーをホームページにリダイレクトしたい場合は、次のように書きます。（ここではホームページのURLの名前がhomeだと仮定しています）


コピーする
class CreateView(FormView):
    # ...
    success_url = reverse_lazy('home')



 tweet.rbを編集しバリデーションを設けましょう
app/models/tweet.rb

class Tweet < ApplicationRecord
  validates :text, presence: true
end
このバリデーションの設定により、空のツイートは登録できなくなりました

これをできるか確認。


汎用ビューを使用して楽に実装できるようにする。
django.views.generic.list.ListView
一覧表示を表示させるためのView
django.views.generic.detail.DetailView
詳細を表示するためのView
django.views.generic.edit.FormView
フォームを利用するためのView
django.views.generic.edit.CreateView
モデルオブジェクトを登録するためのView
django.views.generic.edit.UpdateView
モデルオブジェクトを更新するためのView
django.views.generic.edit.DeleteView
モデルオブジェクトを削除するためのView


ユーザーの登録には
AbstractBaseUser と BaseUserManager の使用してユーザーモデルの作成を行う。

以下をsetting.pyへ
AUTH_USER_MODEL = 'users.CustomUser'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ログインの処理はfrom django.contrib.auth.views import LoginViewで楽に実装


```
# urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # 既存のパス
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    # 他のURLconfパス...
]

```


エラー
users/urls.pyにはログアウトのurlpathは書かない、ルートディレクトリで行うようにしているため
```
サーバーは'logout'という名前のURLパターンを見つけることができずに500の内部サーバーエラーを返しています。エラーはdjango.urls.exceptions.NoReverseMatchとして示されており、これは{% url 'logout' %}タグまたはreverse('logout')関数をテンプレートまたはビューで使っているものの、Djangoがこの名前のURLパターンを識別できないことを意味します。

この問題を解決するには、logoutという名前のURLルートをurls.pyに正しく定義する必要があります。これは通常、ログアウト機能を提供するためにdjango.contrib.auth.views.LogoutViewを使って行われます。あなたのプロジェクトまたはアプリケーションのurls.pyファイルをチェックして、logoutURLパターンが正しく設定されていることを確認してください。

urls.pyの例
以下は、ログアウト機能をurls.pyに追加する簡単な例です：

from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # 他のURLパターン
    path('logout/', LogoutView.as_view(), name='logout'),
]

```