from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('tweets:index')  # 登録完了後にリダイレクトするURL
    template_name = 'users/sign_up.html'
