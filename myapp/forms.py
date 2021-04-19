from django import forms
from myapp.models import *

class UpdateForm(forms.ModelForm):
    class Meta:
        model=MyUserData
        fields=['username','email','phone','place']