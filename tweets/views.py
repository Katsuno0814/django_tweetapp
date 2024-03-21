from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, DeleteView, UpdateView
from .forms import TweetForm
from .models import Tweet

class IndexView(ListView):
    model = Tweet
    template_name = 'tweets/index.html'
    context_object_name = 'tweets'


class CreateView(FormView):
    template_name = 'tweets/new.html'
    form_class = TweetForm
    success_url = reverse_lazy('tweets:index')

    def form_valid(self, form):
        # form.cleaned_dataを使用して安全にフォームデータを取得
        name = form.cleaned_data['name']
        image = form.cleaned_data['image']
        text = form.cleaned_data['text']

        # Tweetモデルインスタンスを作成して保存
        Tweet.objects.create(name=name, image=image, text=text)

        # 親クラスのform_validを呼び出してリダイレクト処理を行う
        return super().form_valid(form)

class DeleteView(DeleteView):
  model = Tweet
  template_name = 'tweets/tweet_confirm_delete.html'  # 削除確認ページのテンプレート
  success_url = reverse_lazy('tweets:index')  # 削除成功後のリダイレクト先URL


class UpdateView(UpdateView):
    model = Tweet
    form_class = TweetForm
    template_name = 'tweets/edit.html'  # テンプレート名を指定
    success_url = reverse_lazy('tweets:index')  # 更新後のリダイレクト先URL

class ShowView(DetailView):
  model = Tweet
  template_name = 'tweets/show.html'