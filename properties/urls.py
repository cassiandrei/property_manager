from django.urls import path

from properties.views import fotos

app_name = 'properties'
urlpatterns = [
    path('<id>/fotos/', fotos, name='fotos'),
]
