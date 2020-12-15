from django.db import models


# Create your models here.
class Imovel(models.Model):
    UF = models.CharField('UF', max_length=2)
    cidade = models.CharField('Cidade', max_length=50)
    cep = models.CharField('CEP', max_length=10, blank=True, null=True)
    nome = models.CharField('Nome', max_length=100)
    logradouro = models.CharField('Logradouro', max_length=50)
    numero = models.PositiveIntegerField('Número', blank=True, null=True)
    complemento = models.CharField('Complemento', max_length=30, blank=True, null=True)
    status = models.ForeignKey('config.Status', on_delete=models.PROTECT, null=True)
    contato = models.TextField('Contato', blank=True, null=True)

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'

    def __str__(self):
        return '{}, {}, {}, {}/{}'.format(self.nome, self.logradouro, str(self.numero), self.cidade, self.UF)


class Residencia(models.Model):
    imovel = models.OneToOneField(Imovel, on_delete=models.CASCADE)
    dormitorios = models.PositiveSmallIntegerField('Dormitórios')
    suites = models.PositiveSmallIntegerField('Suítes')
    lavabos = models.PositiveSmallIntegerField('Lavabos')
    banheiros = models.PositiveSmallIntegerField('Banheiros')
    salas = models.PositiveSmallIntegerField('Salas')
    sacadas = models.PositiveSmallIntegerField('Sacadas')
    vagas = models.PositiveSmallIntegerField('Vagas para carros')
    cozinhas = models.PositiveSmallIntegerField('Cozinhas')
    infra = models.TextField('Infraestrutura', blank=True, null=True)
    outros = models.TextField('Outros', blank=True, null=True)

    class Meta:
        verbose_name = 'Residência'
        verbose_name_plural = 'Residências'

    def __str__(self):
        return self.imovel.__str__()


class Terreno(models.Model):
    imovel = models.OneToOneField(Imovel, on_delete=models.CASCADE)
    hectares = models.FloatField('Hectares', blank=True, null=True)
    dimencoes = models.TextField('Dimensões', blank=True, null=True)
    loteamento = models.BooleanField('Loteamento')
    casa = models.BooleanField('Possui casa?')
    plano = models.BooleanField('Plano')
    limpo = models.BooleanField('Limpo')
    limpo_texto = models.TextField('Descrição sobre a limpeza do terreno', null=True, blank=True)
    agua = models.BooleanField('Água')
    agua_texto = models.TextField('Descrição Água', blank=True, null=True)
    posicao = models.TextField('Posição solar', blank=True, null=True)


    class Meta:
        verbose_name = 'Terreno'
        verbose_name_plural = 'Terrenos'

    def __str__(self):
        return self.imovel.__str__()


class Fazenda(Terreno):
    energia = models.BooleanField('Energia')
    animais = models.TextField('Criação de animais')
    propriedade = models.TextField('Propriedade')

    class Meta:
        verbose_name = 'Fazenda'
        verbose_name_plural = 'Fazenda'

    def __str__(self):
        return self.imovel.__str__()

