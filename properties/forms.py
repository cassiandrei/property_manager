# coding=utf-8
from django import forms


class ImovelRelatedForm(forms.ModelForm):
    UF = forms.CharField(label='UF', max_length=2, required=True)
    cidade = forms.CharField(label='Cidade', max_length=50, required=True)
    cep = forms.CharField(label='CEP', max_length=10, required=False)
    nome = forms.CharField(label='Nome', max_length=100, required=True)
    logradouro = forms.CharField(label='Logradouro', max_length=50, required=True)
    numero = forms.IntegerField(label='Número', min_value=0, required=False)
    complemento = forms.CharField(label='Complemento', max_length=30, required=False)

    class Meta:
        exclude = ['imovel']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.initial['UF'] = self.instance.imovel.UF
            self.initial['cidade'] = self.instance.imovel.cidade
            self.initial['cep'] = self.instance.imovel.cep
            self.initial['nome'] = self.instance.imovel.nome
            self.initial['logradouro'] = self.instance.imovel.logradouro
            self.initial['numero'] = self.instance.imovel.numero
            self.initial['complemento'] = self.instance.imovel.complemento
        except:
            pass
