import datetime
from django.db import models


class Tweet(models.Model):
    name = models.CharField(max_length=10)  # 文字列フィールドはCharFieldを使用します。max_lengthは必須の引数です。
    text = models.CharField(max_length=255)  # 長いテキストの場合はTextFieldを使用します。
    image = models.TextField()  # 画像はImageFieldを使用し、upload_toで保存先を指定します。
    created_at = models.DateTimeField(auto_now_add=True)  # オブジェクト作成時に現在の日時を自動的にセット
    updated_at = models.DateTimeField(auto_now=True)  # オブジェクト更新時に現在の日時を自動的にセット

    def __str__(self):
        return self.text
    class Meta:
        db_table = 'tweets'
