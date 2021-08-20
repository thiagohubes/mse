from rest_framework import serializers
from .models import Evento, Equipamento, Localidade, Agente
from drf_writable_nested.serializers import WritableNestedModelSerializer


class LocalidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = Localidade
         fields = ('nome',)

class EquipamentoSerializer(WritableNestedModelSerializer,
                            serializers.HyperlinkedModelSerializer):
    localidade = LocalidadeSerializer()
    class Meta:
        model = Equipamento
        fields = ('nome', 'tipo', 'modelo', 'localidade')


class EventoSerializer(WritableNestedModelSerializer,
                       serializers.HyperlinkedModelSerializer):
    equipamento = EquipamentoSerializer()
    class Meta:
        model = Evento
        fields = ('equipamento', 'inicio', 'fim', 'sequencia')


class AgenteSerializer(serializers.HyperlinkedModelSerializer):
    localidade = LocalidadeSerializer(read_only=True)
    class Meta:
        model = Agente
        fields = ('nome', 'endereco_ip', 'tipo', 'localidade')
