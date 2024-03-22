from django.contrib import admin

from .models import Tweet
from comments.models import Comment

class CommentInline(admin.StackedInline):
    model = Comment

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["text","image"]}),
    ]
    readonly_fields = ("created_at", "updated_at")  # 読み取り専用フィールドとして指定
    list_filter = ["created_at"]
    search_fields = ["text"]
    inlines = [CommentInline]



admin.site.register(Tweet, TweetAdmin)
