from rest_framework import serializers

from .models import Evento, Equipamento, Localidade, Agente


class LocalidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Localidade
        fields = ('nome',)


class EquipamentoSerializer(serializers.HyperlinkedModelSerializer):
    localidade = LocalidadeSerializer()
    class Meta:
        model = Equipamento
        fields = ('nome', 'tipo', 'modelo', 'localidade')


class EventoSerializer(serializers.HyperlinkedModelSerializer):
    equipamento = EquipamentoSerializer()
    class Meta:
        model = Evento
        fields = ('equipamento', 'inicio', 'fim')


class AgenteSerializer(serializers.HyperlinkedModelSerializer):
    localidade = LocalidadeSerializer()
    class Meta:
        model = Agente
        fields = ('nome', 'endereco_ip', 'tipo', 'localidade')
