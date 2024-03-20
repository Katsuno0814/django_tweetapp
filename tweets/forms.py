from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['name', 'image', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nickname'}),
            'text': forms.Textarea(attrs={'placeholder': 'Text', 'rows': 4}),
        }
        labels = {
            'name': 'ニックネーム',
            'image': '画像URL',
            'text': 'テキスト',
        }