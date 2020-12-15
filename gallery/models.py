from django.db import models
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

class Foto(models.Model):
    nome = models.CharField('Nome', max_length=30)
    imovel = models.ForeignKey('properties.Imovel', on_delete=models.CASCADE)
    file = models.ImageField(upload_to='fotos', storage=gd_storage)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Foto'

    def __str__(self):
        return self.imovel.__str__()
