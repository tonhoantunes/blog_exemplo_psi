from django import forms
from django.core.exceptions import ValidationError
from .models import Mensagem

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['nome', 'email', 'telefone', 'cidade', 'mensagem']
        #widgets = {
        #    'nome': forms.TextInput(attrs={
        #        'class': 'form-control',
        #        'placeholder': 'Digite seu nome: '
        #    })
        #}

    def clean_cidade(self):
        data = self.cleaned_data["cidade"]
        cidades_validas = ["SPP", "São Pedro", "Bom Jesus"]
        
        if (not data in cidades_validas):
            raise ValidationError("Cidade inválida!")

        return data
    