from django.db import models
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()


class Foto(models.Model):
    imovel = models.ForeignKey('properties.Imovel', related_name='residencia_id', null=True, blank=True, on_delete=models.CASCADE)
    residencia = models.ForeignKey('properties.Residencia', related_name='residencia_id', null=True, blank=True, on_delete=models.CASCADE)
    terreno = models.ForeignKey('properties.Terreno', related_name='terreno_id',  null=True, blank=True, on_delete=models.CASCADE)
    fazenda = models.ForeignKey('properties.Fazenda', related_name='fazenda_id', null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=300)
    file = models.ImageField('Arquivo', upload_to='fotos', storage=gd_storage)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Foto'

    def __str__(self):
        return self.nome
