from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(CustomUserCreationForm):

    class Meta(CustomUserCreationForm.Meta):
        model = get_user_model()
        fields = CustomUserCreationForm.Meta.fields