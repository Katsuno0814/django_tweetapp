from django.db import models
from django.conf import settings

# 仮定: UserとTweetモデルがすでに定義されているとします。

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tweet = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE)  # 'app名'はTweetモデルが定義されているアプリの名前に置き換えてください。
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
      db_table = 'comments'
