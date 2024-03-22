from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from tweets.models import Tweet
User = get_user_model()


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('tweets:index')  # 登録完了後にリダイレクトするURL
    template_name = 'users/sign_up.html'

class UserPageView(ListView):
    model = Tweet
    template_name = 'users/mypage.html'  # テンプレート名を適切に設定
    context_object_name = 'tweets'  # テンプレートに渡すコンテキスト変数名

    def get_queryset(self):
        print("これがキーワード↓↓↓↓↓↓↓↓↓")
        print(self.kwargs)
        # URLからユーザーIDを取得（'user_id'はurls.pyで設定したパラメータ名に合わせてください）
        user_id = self.kwargs.get('pk')
        # そのIDに対応するユーザーを取得（存在しなければ404エラー）
        self.user = get_object_or_404(User, pk=user_id)
        # そのユーザーに関連するツイートを取得
        return Tweet.objects.filter(user=self.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        # ビューに渡す追加のコンテキスト変数を定義
        context = super().get_context_data(**kwargs)
        context['profile_user'] = self.user  # プロフィールページの所有者
        return context
from tweets.models import Tweet


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('tweets:index')  # 登録完了後にリダイレクトするURL
    template_name = 'users/sign_up.html'

class UserPageView(ListView):
    model = Tweet
    template_name = 'users/mypage.html'  # テンプレート名を適切に設定
    context_object_name = 'tweets'  # テンプレートに渡すコンテキスト変数名

    def get_queryset(self):
        print("これがキーワード↓↓↓↓↓↓↓↓↓")
        print(self.kwargs)
        # URLからユーザーIDを取得（'user_id'はurls.pyで設定したパラメータ名に合わせてください）
        user_id = self.kwargs.get('pk')
        # そのIDに対応するユーザーを取得（存在しなければ404エラー）
        self.user = get_object_or_404(User, pk=user_id)
        # そのユーザーに関連するツイートを取得
        return Tweet.objects.filter(user=self.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
         # 親クラスのメソッドを呼び出して、コンテキストを初期化
        context = super().get_context_data(**kwargs)
        # プロフィールページの所有者をコンテキストに追加
        context['profile_user'] = self.user

        # ここでcontextとself.userの値をプリント
        print("これがcontextの内容です↓↓↓↓↓↓↓↓↓")
        print(context)
        print("これがself.userの内容です↓↓↓↓↓↓↓↓↓")
        print(self.user)

        return context