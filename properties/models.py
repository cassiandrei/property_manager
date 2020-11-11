from django.db import models


# Create your models here.
class Imovel(models.Model):
    UF = models.CharField('UF', max_length=2, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=2, blank=True, null=True)
    cep = models.CharField('CEP', max_length=10, blank=True, null=True)
    nome = models.CharField('Nome', max_length=10, blank=True, null=True)
    logradouro = models.CharField('Logradouro', max_length=50, blank=True, null=True)
    numero = models.PositiveIntegerField('Número', blank=True, null=True)
    complemento = models.CharField('Complemento', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'

    def __str__(self):
        return '{}, {}, {}, {}/{}'.format(self.nome, self.logradouro, str(self.numero), self.cidade, self.UF)


class Residencia(models.Model):
    imovel = models.OneToOneField(Imovel, on_delete=models.CASCADE)
    dormitorios = models.PositiveSmallIntegerField('Quantidade de dormitórios')
    suites = models.PositiveSmallIntegerField('Quantidade de suítes')
    lavabos = models.PositiveSmallIntegerField('Quantidade de lavabos')
    banheiros = models.PositiveSmallIntegerField('Quantidade de Banheiros')
    salas = models.PositiveSmallIntegerField('Quantidade de Salas')
    sacadas = models.PositiveSmallIntegerField('Quantidade de Sacadas')
    vagas = models.PositiveSmallIntegerField('Quantidade de vagas para carros')
    cozinhas = models.PositiveSmallIntegerField('Quantidade de cozinhas')
    infra = models.TextField('Infraestrutura', blank=True, null=True)
    outros = models.TextField('Infraestrutura', blank=True, null=True)

    class Meta:
        verbose_name = 'Residência'
        verbose_name_plural = 'Residências'

    def __str__(self):
        return self.imovel.__str__()
