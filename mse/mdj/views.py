from django.shortcuts import render, get_object_or_404
from .models import Evento, Equipamento, Localidade, Agente
from rest_framework import viewsets, generics
from .serializers import EventoSerializer, EquipamentoSerializer, LocalidadeSerializer, AgenteSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from datetime import datetime, timedelta
from django.db.models import Count


def lista_de_eventos(request):
    EQ_TIPO_1 = ['Siemens-3AT5', 'Siemens-3AT5-EI', 'Siemens-8DQ1']
    EMERGENCIA_1 = 150
    URGENCIA_1 = 75
    MEDIA_1 = 50
    MONIT_1 = 25
    EMERGENCIA_2 = 100
    URGENCIA_2 = 50
    MEDIA_2 = 25
    MONIT_2 = 12
    estado = str()
    eventos = Evento.objects.all()
    eventos_ultimo_dia = Evento.objects.filter(inicio__gte=datetime.now()-timedelta(days=1))
    nome_local = list(tuple())
    eventos_nome_local = list(tuple())
    for evento in eventos_ultimo_dia:
        nome = evento.equipamento.nome
        local = evento.equipamento.localidade.nome
        modelo = evento.equipamento.modelo
        nome_local.append((nome, local, modelo))
    nome_local = list(set(nome_local))
    for nome, local, modelo in nome_local:
        evento = Evento.objects.filter(equipamento__nome=nome, equipamento__localidade__nome=local, equipamento__modelo=modelo, inicio__gte=datetime.now()-timedelta(days=1))
        contagem = evento.count()
        if modelo in EQ_TIPO_1:
            if contagem > EMERGENCIA_1:
                estado = "Emergência"
            elif contagem > URGENCIA_1:
                estado = "Urgência"
            elif contagem > MEDIA_1:
                estado = "Média"
            elif contagem > MONIT_1:
                estado = "Monitoramento"
            else:
                estado = "OK"
        else:
            if contagem > EMERGENCIA_2:
                estado = "Emergência"
            elif contagem > URGENCIA_2:
                estado = "Urgência"
            elif contagem > MEDIA_2:
                estado = "Média"
            elif contagem > MONIT_2:
                estado = "Monitoramento"
            else:
                estado = "OK"
        eventos_nome_local.append((nome, local, modelo, contagem, estado))
    return render(request,
                  'mdj/evento/lista.html',
                  {'eventos': eventos,
                   'eventos_nome_local': eventos_nome_local})

def detalhe_de_evento(request, sequencia):
    evento = get_object_or_404(Evento, sequencia=sequencia)
    return render(request,
                  'mdj/evento/detalhe.html',
                  {'evento': evento})

#class EventoList(generics.ListCreateAPIView):
# ModelViewSet provê .list() .create() .retrieve() .update() e .destroy()
#-----
# class EventoViewSet(viewsets.ModelViewSet):
#     queryset = Evento.objects.all().order_by('inicio')
#     serializer_class = EventoSerializer
# 
# 
# class EquipamentoViewSet(viewsets.ModelViewSet):
#     queryset = Equipamento.objects.all().order_by('nome')
#     serializer_class = EquipamentoSerializer
#---
#    def get_serializer_class(self):
#        if self.request.method in ['GET']:
#            return EquipamentoReadSerializer
#        return EquipamentoSerializer
#---
# class LocalidadeViewSet(viewsets.ModelViewSet):
#     queryset = Localidade.objects.all().order_by('nome')
#     serializer_class = LocalidadeSerializer
# 
# 
# class AgenteViewSet(viewsets.ModelViewSet):
#     queryset = Agente.objects.all().order_by('nome')
#     serializer_class = AgenteSerializer

class EquipamentoList(generics.ListCreateAPIView):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
    name = 'equipamento-list'

class EquipamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
    name = 'equipamento-detail'

class EventoList(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    name = 'evento-list'

class EventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    name = 'evento-detail'

class LocalidadeList(generics.ListCreateAPIView):
    queryset = Localidade.objects.all()
    serializer_class = LocalidadeSerializer
    name = 'localidade-list'

class LocalidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Localidade.objects.all()
    serializer_class = LocalidadeSerializer
    name = 'localidade-detail'

class AgenteList(generics.ListCreateAPIView):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerializer
    name = 'agente-list'

class AgenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerializer
    name = 'agente-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'equipamentos': reverse(EquipamentoList.name, request=request),
            'eventos': reverse(EventoList.name, request=request),
            'localidade': reverse(LocalidadeList.name, request=request),
            'agente': reverse(AgenteList.name, request=request),
            })

