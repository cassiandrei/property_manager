from django.shortcuts import render, get_object_or_404

# Create your views here.
from gallery.models import Foto
from properties.models import Imovel


def fotos(request, id):
    imovel = get_object_or_404(Imovel, id=id)
    context = {
        'imovel': imovel,
        'fotos': Foto.objects.filter(imovel=imovel)
    }
    return render(request, 'properties/fotos.html', context=context)