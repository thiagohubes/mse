from django.shortcuts import render, get_object_or_404
from .models import Evento, Equipamento, Localidade, Agente
from rest_framework import viewsets, generics
from .serializers import EventoSerializer, EquipamentoSerializer, LocalidadeSerializer, AgenteSerializer


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
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().order_by('inicio')
    serializer_class = EventoSerializer


class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all().order_by('nome')
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return EquipamentoReadSerializer
    #serializer_class = EquipamentoSerializer
        return EquipamentoSerializer



class LocalidadeViewSet(viewsets.ModelViewSet):
    queryset = Localidade.objects.all().order_by('nome')
    serializer_class = LocalidadeSerializer


class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.all().order_by('nome')
    serializer_class = AgenteSerializer
