from django.contrib import admin

# Register your models here.
from gallery.models import Foto
from properties.forms import ImovelRelatedForm, ImovelForm
from properties.models import Residencia, Imovel, Terreno, Fazenda

from django.utils.translation import gettext_lazy as _

from config.models import Status


class ImovelListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Status'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """

        status = list(Status.objects.values_list('descricao', 'descricao'))
        return status

        # return (
        #     ('80s', _('in the eighties')),
        #     ('90s', _('in the nineties')),
        # )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.

        # if self.value() == '80s':
        #     return queryset.filter(birthday__gte=date(1980, 1, 1),
        #                             birthday__lte=date(1989, 12, 31))
        # if self.value() == '90s':
        #     return queryset.filter(birthday__gte=date(1990, 1, 1),
        #                             birthday__lte=date(1999, 12, 31))
        if not self.value():
            return queryset
        else:
            return queryset.filter(imovel__status__descricao=self.value())


class Imovelsavemodel(admin.ModelAdmin):
    save_as = True
    change_form_template = "properties/changeform.html"

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
            imovel.status = form.cleaned_data.get('status')
            imovel.contato = form.cleaned_data.get('contato')
            imovel.descricao = form.cleaned_data.get('descricao')
            imovel.save()
        else:
            imovel = Imovel(UF=form.cleaned_data.get('UF'),
                            cidade=form.cleaned_data.get('cidade'),
                            cep=form.cleaned_data.get('cep'),
                            nome=form.cleaned_data.get('nome'),
                            logradouro=form.cleaned_data.get('logradouro'),
                            numero=form.cleaned_data.get('numero'),
                            complemento=form.cleaned_data.get('complemento'),
                            status=form.cleaned_data.get('status'),
                            descricao=form.cleaned_data.get('descricao'),
                            contato=form.cleaned_data.get('contato'),
                            )
            obj.imovel = imovel
            imovel.save()
        super().save_model(request, obj, form, change)


class FotoinlineResidencia(admin.TabularInline):
    model = Foto
    verbose_name = 'Fotos'
    verbose_name_plural = 'Fotos'
    exclude = ['terreno', 'fazenda', 'imovel']
    fk_name = 'residencia'


class ResidenciaAdmin(Imovelsavemodel):
    form = ImovelRelatedForm
    list_display = ['imovel', 'dormitorios', 'suites', 'lavabos', 'banheiros', 'salas', 'sacadas', 'vagas', 'cozinhas']
    list_filter = [ImovelListFilter, 'dormitorios', 'suites', 'lavabos', 'banheiros', 'salas', 'sacadas', 'vagas', 'cozinhas']
    model = Residencia
    inlines = (FotoinlineResidencia,)

    fieldsets = (
        ('Imóvel', {
            'fields': (
                'UF', 'cidade', 'cep', 'nome', 'descricao', 'logradouro', 'numero', 'complemento', 'status', 'contato'),
        }),
        ('Residência', {
            'fields': (
                'dormitorios', 'suites', 'lavabos', 'banheiros', 'salas', 'sacadas', 'vagas', 'cozinhas', 'infra',
                'outros')}),
        ('Fotos', {
            'fields': ('fotos',)
        }),
    )

    def save_model(self, request, obj, form, change):
        super(ResidenciaAdmin, self).save_model(request, obj, form, change)
        files = request.FILES.getlist('fotos', None)
        if files:
            for f in files:
                filename = f.name
                foto = Foto.objects.create(residencia=obj, nome=filename, imovel=obj.imovel, file=f)
                foto.save()


admin.site.register(Residencia, ResidenciaAdmin)


class FotoinlineTerreno(admin.TabularInline):
    model = Foto
    verbose_name = 'Fotos'
    verbose_name_plural = 'Fotos'
    exclude = ['residencia', 'fazenda', 'imovel']
    fk_name = 'terreno'


class TerrenoAdmin(Imovelsavemodel):
    form = ImovelRelatedForm
    list_display = ['imovel', 'hectares', 'dimencoes', 'loteamento', 'casa', 'plano', 'limpo', 'agua']
    list_filter = ['loteamento', 'casa', 'plano', 'limpo', 'agua']
    model = Terreno
    inlines = (FotoinlineTerreno,)

    fieldsets = (
        ('Imóvel', {
            'fields': (
                'UF', 'cidade', 'cep', 'nome', 'descricao', 'logradouro', 'numero', 'complemento', 'status', 'contato'),
        }),
        ('Terreno', {
            'fields': (
                'hectares', 'dimencoes', 'loteamento', 'casa', 'plano', 'limpo', 'limpo_texto', 'agua', 'agua_texto',
                'posicao')}),
        ('Fotos', {
            'fields': ('fotos',)
        }),
    )

    def save_model(self, request, obj, form, change):
        super(TerrenoAdmin, self).save_model(request, obj, form, change)
        files = request.FILES.getlist('fotos', None)
        if files:
            for f in files:
                filename = f.name
                foto = Foto.objects.create(terreno=obj, nome=filename, imovel=obj.imovel, file=f)
                foto.save()


admin.site.register(Terreno, TerrenoAdmin)


class FotoinlineFazenda(admin.TabularInline):
    model = Foto
    verbose_name = 'Fotos'
    verbose_name_plural = 'Fotos'
    exclude = ['residencia', 'terreno', 'imovel']
    fk_name = 'fazenda'


class FazendaAdmin(Imovelsavemodel):
    form = ImovelRelatedForm
    list_display = ['imovel', 'hectares', 'dimencoes', 'loteamento', 'casa', 'plano', 'limpo', 'agua']
    list_filter = ['loteamento', 'casa', 'plano', 'limpo', 'agua']
    model = Fazenda
    inlines = (FotoinlineFazenda,)

    fieldsets = (
        ('Imóvel', {
            'fields': (
                'UF', 'cidade', 'cep', 'nome', 'descricao', 'logradouro', 'numero', 'complemento', 'status', 'contato'),
        }),
        ('Terreno', {
            'fields': (
                'hectares', 'dimencoes', 'loteamento', 'casa', 'plano', 'limpo', 'limpo_texto', 'agua', 'agua_texto',
                'posicao')}),
        ('Fazenda', {
            'fields': (
                'energia', 'animais', 'propriedade',
            )}),
        ('Fotos', {
            'fields': ('fotos',)
        }),
    )

    def save_model(self, request, obj, form, change):
        super(FazendaAdmin, self).save_model(request, obj, form, change)
        files = request.FILES.getlist('fotos', None)
        if files:
            for f in files:
                filename = f.name
                foto = Foto.objects.create(fazenda=obj, nome=filename, imovel=obj.imovel, file=f)
                foto.save()


admin.site.register(Fazenda, FazendaAdmin)


class ImovelAdmin(admin.ModelAdmin):
    list_display = ['UF', 'cidade', 'nome', 'complemento', 'status', 'contato']
    list_filter = ['UF', 'cidade', 'status']
    form = ImovelForm
    change_form_template = "properties/changeform.html"

    def save_model(self, request, obj, form, change):
        super(ImovelAdmin, self).save_model(request, obj, form, change)
        files = request.FILES.getlist('fotos', None)
        if files:
            for f in files:
                filename = f.name
                foto = Foto.objects.create(nome=filename, imovel=obj, file=f)
                foto.save()

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# admin.site.register(Imovel, ImovelAdmin)
