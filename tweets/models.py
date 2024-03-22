import datetime
from django.db import models
from django.conf import settings


class Tweet(models.Model):
    text = models.CharField(max_length=255)  # 長いテキストの場合はTextFieldを使用します。
    image = models.TextField()  # 画像はImageFieldを使用し、upload_toで保存先を指定します。
    created_at = models.DateTimeField(auto_now_add=True)  # オブジェクト作成時に現在の日時を自動的にセット
    updated_at = models.DateTimeField(auto_now=True)  # オブジェクト更新時に現在の日時を自動的にセット
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    # def clean(self):
    #     forbidden_words = ['不適切な単語', '禁止された単語']
    #     for word in forbidden_words:
    #         if word in self.text:
    #             raise ValidationError({
    #                 'text': _("このテキストには禁止されている単語が含まれています。")
    #             })
    class Meta:
        db_table = 'tweets'
