from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     REGION_A = 'sl'
#     REGION_B = 'dj'
#     REGION_C = 'gj'
#     REGION_D = 'gm'
#     REGION_E = 'bs'
#     REGION_CHOICES = [
#         (REGION_A, '서울'),
#         (REGION_B, '대전'),
#         (REGION_C, '광주'),
#         (REGION_D, '구미'),
#         (REGION_E, '부산'),
#     ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select())

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-tilte',
                'placeholder' : 'Enter the title',
                'maxlength' : 10,
            }
        )
    )
    class Meta:
        # 사용할 필드를 작성
        model = Article
        # fields = ('title', 'content',)
        fields = '__all__'
        # exclude = 'title' # 제외하고 싶은 필드를 선택

