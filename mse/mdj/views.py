from django.shortcuts import render, get_object_or_404
from .models import Evento, Equipamento, Localidade, Agente
from rest_framework import viewsets
from .serializers import EventoSerializer, EquipamentoSerializer, LocalidadeSerializer, AgenteSerializer

def lista_de_eventos(request):
    eventos = Evento.objects.all()
    return render(request,
                  'mdj/evento/lista.html',
                  {'eventos': eventos})

def detalhe_de_evento(request, eqpt, ano_ini, mes_ini, dia_ini, hora_ini, min_ini, seg_ini, ano_fim, mes_fim, dia_fim, hora_fim, min_fim, seg_fim):
    evento = get_object_or_404(Evento, 
                               equipamento__id=eqpt,
                               inicio__year=ano_ini,
                               inicio__month=mes_ini,
                               inicio__day=dia_ini,
                               inicio__hour=hora_ini,
                               inicio__minute=min_ini,
                               inicio__second=seg_ini,
                               fim__year=ano_fim,
                               fim__month=mes_fim,
                               fim__day=dia_fim,
                               fim__hour=hora_fim,
                               fim__minute=min_fim,
                               fim__second=seg_fim)
    return render(request,
                  'mdj/evento/detalhe.html',
                  {'evento': evento})

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().order_by('inicio')
    serializer_class = EventoSerializer


class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all().order_by('nome')
    serializer_class = EquipamentoSerializer


class LocalidadeViewSet(viewsets.ModelViewSet):
    queryset = Localidade.objects.all().order_by('nome')
    serializer_class = LocalidadeSerializer


class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.all().order_by('nome')
    serializer_class = AgenteSerializer
