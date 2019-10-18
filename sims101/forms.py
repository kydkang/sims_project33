from django import forms
from .models import Index101

class IndexForm(forms.ModelForm): 
    class Meta:
        model = Index101
        fields = ['data_one', 'data_two', 'calculated_value']
        calculated_value = forms.CharField(disabled=True) 
        
        widgets = {
            'calculated_value': forms.TextInput(attrs={'readonly': 'readonly'}),
        }