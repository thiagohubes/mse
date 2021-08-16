from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Agente(models.Model):
    TIPOS_AGENTES = (
            ('raspberry-pi-model-b', 'Raspberry-Pi-Model-B'),
            )
    endereco_ip = models.GenericIPAddressField(protocol='IPv4')
    tipo = models.CharField(max_length=250,
                            choices=TIPOS_AGENTES,
                            default='raspberry-pi-model-b')
    class Meta:
        ordering = ('endereco_ip',)

    def __str__(self):
        return self.endereco_ip

