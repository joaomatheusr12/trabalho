from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        input_formats=['%d/%m/%Y'],  # <- Permitir entrada no formato brasileiro
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'placeholder': 'dd/mm/aaaa'}
        )
    )

    class Meta:
        model = Pessoa
        fields = '__all__'
