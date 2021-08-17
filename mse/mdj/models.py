from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Agente(models.Model):
    TIPOS_AGENTES = (
        ('raspberry-pi-model-b', 'Raspberry-Pi-Model-B'),
    )
    endereco_ip = models.GenericIPAddressField(protocol='IPv4')
    nome = models.CharField(max_length=250,
                            default='agente-1')
    tipo = models.CharField(max_length=250,
                            choices=TIPOS_AGENTES,
                            default='raspberry-pi-model-b')
    localidade = models.ForeignKey('Localidade', 
                                   on_delete=models.CASCADE,
                                   related_name='agente')
    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


class Localidade(models.Model):
    nome = models.CharField(max_length=250,
                            default='SE XYZ')
    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


class Equipamento(models.Model):
    TIPOS_EQUIPAMENTOS = (
        ('disjuntor', 'Disjuntor'),
    )
    MODELOS_EQUIPAMENTOS = (
        ('modelo-a', 'Modelo A'),
    )
    nome = models.CharField(max_length=250,
                            default='DJ XYZ')
    tipo = models.CharField(max_length=250,
                            default='disjuntor')
    modelo = models.CharField(max_length=250,
                              default='modelo-a')
    localidade = models.ForeignKey('Localidade', 
                                   on_delete=models.CASCADE,
                                   related_name='equipamento')
    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    inicio = models.DateTimeField(default=timezone.now())
    fim = models.DateTimeField(default=timezone.now())
    equipamento = models.ForeignKey('Equipamento',
                                    on_delete=models.CASCADE,
                                    related_name='evento')
    class Meta:
        ordering = ('inicio',)

    def __str__(self):
        return str(self.inicio)


