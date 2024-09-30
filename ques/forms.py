from django.forms import ModelForm, Textarea, Select, TextInput
from .models import question

class questionForm(ModelForm):
    class Meta:
        model = question
        fields = ['name', 'course', 'year', 'question_text']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'course': Select(attrs={'class': 'form-select'}),
            'year': Select(attrs={'class': 'form-select'}),
            'question_text': Textarea(attrs={'class': 'form-control'}),
        }