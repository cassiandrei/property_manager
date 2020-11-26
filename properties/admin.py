from django.contrib import admin

# Register your models here.
from properties.forms import ImovelRelatedForm
from properties.models import Residencia, Imovel


class Imovelsavemodel(admin.ModelAdmin):
    save_as = True

    def save_model(self, request, obj, form, change):
        if change:
            imovel = obj.imovel
            imovel.UF = form.cleaned_data.get('UF')
            imovel.cidade = form.cleaned_data.get('cidade')
            imovel.cep = form.cleaned_data.get('cep')
            imovel.nome = form.cleaned_data.get('nome')
            imovel.logradouro = form.cleaned_data.get('logradouro')
            imovel.numero = form.cleaned_data.get('numero')
            imovel.complemento = form.cleaned_data.get('complemento')
            imovel.save()
        else:
            imovel = Imovel(UF=form.cleaned_data.get('UF'),
                                cidade=form.cleaned_data.get('cidade'),
                                cep=form.cleaned_data.get('cep'),
                                nome=form.cleaned_data.get('nome'),
                                logradouro=form.cleaned_data.get('logradouro'),
                                numero=form.cleaned_data.get('numero'),
                                complemento=form.cleaned_data.get('complemento')
                            )
            obj.imovel = imovel
            imovel.save()
        obj.imovel = imovel
        super().save_model(request, obj, form, change)


class ResidenciaAdmin(Imovelsavemodel):
    form = ImovelRelatedForm
    list_display = ['imovel', 'dormitorios', 'suites', 'lavabos', 'banheiros', 'salas', 'sacadas', 'vagas', 'cozinhas']
    list_filter = ['dormitorios', 'suites', 'lavabos', 'banheiros', 'salas', 'sacadas', 'vagas', 'cozinhas']
    model = Residencia

    fieldsets = (
        ('Imóvel', {
            'fields': ('UF', 'cidade', 'cep', 'nome', 'logradouro', 'numero', 'complemento'),
        }),
        ('Residência', {
            'fields': (
            'dormitorios', 'suites', 'lavabos', 'banheiros', 'salas', 'sacadas', 'vagas', 'cozinhas', 'infra',
            'outros')}),
    )


admin.site.register(Residencia, ResidenciaAdmin)
