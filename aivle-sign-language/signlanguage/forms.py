from django import forms
from .models import *

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['image','answer']
        
class AiModelForm(forms.ModelForm):
    class Meta:
        model = AiModel
        fields = ['is_selected']
        
class AiModelForm2(forms.ModelForm):
    class Meta:
        model = AiModel
        fields = ['ai_file', 'version', 'is_selected']