from django.contrib import admin
from .models import Agente, Localidade, Equipamento, Evento

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = ('endereco_ip', 'nome', 'tipo', 'localidade')

@admin.register(Localidade)
class LocalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tipo', 'modelo', 'localidade')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('sequencia', 'tag', 'inicio', 'fim', 'equipamento')

