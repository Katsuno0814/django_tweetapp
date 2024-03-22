from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import FormView, DeleteView, UpdateView
from .forms import TweetForm
from .models import Tweet
from comments.forms import CommentForm
from comments.models import Comment
from django.shortcuts import get_object_or_404


class IndexView(ListView):
    model = Tweet
    template_name = 'tweets/index.html'
    context_object_name = 'tweets'
    def get_queryset(self):
        # 'created_at' フィールドを使って降順に並び替える
        return Tweet.objects.order_by('-created_at')



class CreateView(FormView):
    template_name = 'tweets/new.html'
    form_class = TweetForm
    success_url = reverse_lazy('tweets:index')

    def form_valid(self, form):
        # form.cleaned_dataを使用して安全にフォームデータを取得
        image = form.cleaned_data['image']
        text = form.cleaned_data['text']

        # Tweetモデルインスタンスを作成して保存
        # form_valid メソッド内で self.request.user を取得し、Tweet の user フィールドにセット
        tweet = Tweet.objects.create(image=image, text=text, user=self.request.user)

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

class ShowView(FormMixin, DetailView):
    model = Tweet
    template_name = 'tweets/show.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(tweet=self.object).order_by('-created_at')
        context['comments'] = comments
        context['form'] = self.get_form()
        for comment in comments:
          print(comment.user.nickname, comment.text)
        return context
