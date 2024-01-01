from django import forms
from .models import FormBerita

class FormBerita(forms.ModelForm):
    class Meta:
        model = FormBerita
        fields ="__all__"
    judul =forms.CharFields(max_lenght=200)
    konten =forms.CharFields(max_lenght=200)