from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    # 추가적인 valuedation? 설정
    # model의 필드와 이름이 같다면, DB에 저장이 된다
    title = forms.CharField(
        min_length=2,
        max_length=100,
        required=True
        )
    category = forms.CharField(
        max_length=30,
        required=True
        )
    content = forms.CharField(
        widget=forms.Textarea,
        required=True,
        min_length=2,
        max_length=10000
        )
    
    # model의 필드가 아니면, HTMl +검증은 하되 저장은 하지 않는다
    is_save = forms.BooleanField(required=False, label='wanna save?', help_text='저장하려면 체크하세요') # DB에 저장 X
    class Meta:
        model = Question
        # 아래 필드들은 모델에 있어야 하며, 데이터 검증 + HTML생성을 합니다
        # title,contet, category는 필드면서 동시에 모델과 연동 is_save는 연동X
        fields = '__all__' 
        