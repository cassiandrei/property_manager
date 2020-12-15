# coding=utf-8
from django import forms
from django.forms import widgets
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.conf import settings

from config.models import Status


class RelatedFieldWidgetCanAdd(widgets.Select):

    def __init__(self, related_model, related_url=None, *args, **kw):
        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = 'admin:%s_%s_add' % info

        # Be careful that here "reverse" is not allowed
        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = [super(RelatedFieldWidgetCanAdd, self).render(name, value, *args, **kwargs)]
        output.append('<a href="%s" class="add-another" id="add_id_%s" onclick="return showAddAnotherPopup(this);"> ' % \
                      (self.related_url, name))
        output.append('<img src="%sadmin/img/icon_addlink.gif" width="10" height="10" alt="%s"/></a>' % (
            settings.STATIC_URL, ''))
        return mark_safe(''.join(output))


class ImovelRelatedForm(forms.ModelForm):
    UF = forms.CharField(label='UF', max_length=2, required=True)
    cidade = forms.CharField(label='Cidade', max_length=50, required=True)
    cep = forms.CharField(label='CEP', max_length=10, required=False)
    nome = forms.CharField(label='Nome', max_length=100, required=True)
    logradouro = forms.CharField(label='Logradouro', max_length=50, required=True)
    numero = forms.IntegerField(label='Número', min_value=0, required=False)
    complemento = forms.CharField(label='Complemento', max_length=30, required=False)
    status = forms.ModelChoiceField(label='Status', queryset=Status.objects.all(),
                                    widget=RelatedFieldWidgetCanAdd(Status))
    contato = forms.CharField(label='Contato', max_length=500, widget=forms.Textarea())

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
