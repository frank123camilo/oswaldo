from django import forms
from .models import Aprendices

class AprendicesForm(forms.ModelForm):
    class Meta:
        model = Aprendices
        fields = ['id','nombre', 'apellido', 'email', 'calificacion', 'curso', 'competencias']
