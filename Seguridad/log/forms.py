from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'user', 'password']

    password = forms.CharField(widget=forms.PasswordInput)
