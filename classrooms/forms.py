from django import forms
from .models import Classroom

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'capacity', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Campo de texto con clase 'form-control'
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),  # Campo de número con 'form-control'
            'location': forms.TextInput(attrs={'class': 'form-control'}),  # Campo de texto con 'form-control'
        }
