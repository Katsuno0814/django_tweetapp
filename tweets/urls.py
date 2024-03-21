from django.urls import path

from . import views

app_name = "tweets"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("tweets/new/", views.CreateView.as_view(), name="new"),
    path("tweets/<int:pk>/delete/", views.DeleteView.as_view(), name="delete"),
]