# forms.py
from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'user', 'password']
    
    password = forms.CharField(widget=forms.PasswordInput)


# forms.py