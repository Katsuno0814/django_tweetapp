from django.contrib import admin

from .models import CustomUser
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["nickname","email","password"]}),
    ]
    readonly_fields = ("created_at", "updated_at")  # 読み取り専用フィールドとして指定
    list_filter = ["created_at"]
    search_fields = ["nickname"]



admin.site.register(CustomUser)
