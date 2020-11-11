from django.contrib import admin

# Register your models here.
from properties.models import Residencia


class ResidenciaAdmin(admin.ModelAdmin):
    # form = ImovelRelatedForm
    list_display = ['dormitorios', 'suites', 'lavabos', 'banheiros', 'salas', 'sacadas', 'vagas', 'cozinhas']
    list_filter = ['dormitorios', 'suites', 'lavabos', 'banheiros', 'salas', 'sacadas', 'vagas', 'cozinhas']
    model = Residencia
    # change_form_template = "materiais/changeform.html"

    # fieldsets = (
    #     ('Material', {
    #         'fields': ('marca', 'valor', 'ativo', 'able_kit', 'codigo', 'script', 'classe_bndes'),
    #     }),
    #     ('Disjuntor', {
    #         'fields': ('disjuntor', 'tipo', 'modelo')}),
    # )


admin.site.register(Residencia, ResidenciaAdmin)
