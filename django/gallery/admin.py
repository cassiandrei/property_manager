from django.contrib import admin

# Register your models here.
from gallery.models import Foto


class HiddenAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


admin.site.register(Foto, HiddenAdmin)
