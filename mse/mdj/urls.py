from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'mdj'
router = routers.DefaultRouter()
router.register(r'evento', views.EventoViewSet)
router.register(r'equipamento', views.EquipamentoViewSet)
router.register(r'localidade', views.LocalidadeViewSet)
router.register(r'agente', views.AgenteViewSet)

urlpatterns = [
    path('', views.lista_de_eventos, name='lista_de_eventos'),
    path('<int:eqpt><int:ano_ini><int:mes_ini><int:dia_ini><int:hora_ini><int:min_ini><int:seg_ini><int:ano_fim><int:mes_fim><int:dia_fim><int:hora_fim><int:min_fim><int:seg_fim>', views.detalhe_de_evento, name='detalhe_de_evento'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
