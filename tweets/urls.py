from django.urls import path, include

from . import views

app_name = "tweets"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("tweets/new/", views.CreateView.as_view(), name="new"),
    path("tweets/<int:pk>/delete/", views.DeleteView.as_view(), name="delete"),
    path('tweets/<int:pk>/edit/', views.UpdateView.as_view(), name='edit'),
    path('tweets/<int:pk>/', views.ShowView.as_view(), name='show'),
    path('tweets/<int:pk>/comments/', include('comments.urls')),
    path('tweets/search_tweets/', views.tweet_search, name='search'),
]