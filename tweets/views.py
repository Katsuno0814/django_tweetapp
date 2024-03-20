from django.http import HttpResponseRedirect
from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = "tweets/index.html"
