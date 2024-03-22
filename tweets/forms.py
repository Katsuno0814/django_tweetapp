from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['image', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Text', 'rows': 4}),
        }
        labels = {
            'image': '画像URL',
            'text': 'テキスト',
        }

class SearchForm(forms.Form):
    keyword = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '投稿を検索する',
            'class': 'search-input'
        })
    )