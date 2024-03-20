from django.views.generic import ListView
from .models import Tweet

class IndexView(ListView):
    model = Tweet
    template_name = 'tweets/index.html'
    context_object_name = 'tweets'