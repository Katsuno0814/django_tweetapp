from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
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
