from django.shortcuts import render, get_object_or_404
from .models import Evento, Equipamento, Localidade, Agente
from rest_framework import viewsets, generics
from .serializers import EventoSerializer, EquipamentoSerializer, LocalidadeSerializer, AgenteSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse


def lista_de_eventos(request):
    eventos = Evento.objects.all()
    return render(request,
                  'mdj/evento/lista.html',
                  {'eventos': eventos})

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

