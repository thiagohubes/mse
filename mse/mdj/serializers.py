# from rest_framework_json import serializers
from rest_framework import serializers
from .models import Evento, Equipamento, Localidade, Agente
#from drf_writable_nested.serializers import WritableNestedModelSerializer


class EquipamentoSerializer(serializers.HyperlinkedModelSerializer):
    #localidade = LocalidadeSerializer(read_only=True)
    evento = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='evento-detail')
    class Meta:
        model = Equipamento
        fields = ('nome', 'tipo', 'modelo', 'localidade')

class LocalidadeSerializer(serializers.HyperlinkedModelSerializer):
    equipamento = EquipamentoSerializer(many=True, read_only=True)
    class Meta:
        model = Localidade
        fields = ('nome',)

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    #equipamento = EquipamentoSerializer(read_only=True)
    equipamento = serializers.SlugRelatedField(queryset=Equipamento.objects.all(), slug_field='nome')
    class Meta:
        model = Evento
        fields = ('equipamento', 'inicio', 'fim', 'sequencia')


class AgenteSerializer(serializers.HyperlinkedModelSerializer):
    #localidade = LocalidadeSerializer(read_only=True)
    localidade = LocalidadeSerializer()
    class Meta:
        model = Agente
        fields = ('nome', 'endereco_ip', 'tipo', 'localidade')
