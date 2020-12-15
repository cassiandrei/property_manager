from django.db import models


# Create your models here.
class Status(models.Model):
    descricao = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Status'
        verbose_name = 'Status'

    def __str__(self):
        return self.descricao
