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
        exclude = ['material']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.initial['marca'] = self.instance.material.marca
            self.initial['valor'] = self.instance.material.valor
            self.initial['ativo'] = self.instance.material.ativo
            self.initial['able_kit'] = self.instance.material.able_kit
            self.initial['script'] = self.instance.material.script
            self.initial['codigo'] = self.instance.material.codigo
            self.initial['classe_bndes'] = self.instance.material.classe_bndes
        except:
            pass
