from django.contrib import admin

from iot.models import Dispositivo, Agendamento, Consumo

class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('name','status',)

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('name','horario')

class ConsumoAdmin(admin.ModelAdmin):
    list_display = ('dispositivo','horario','corrente')

admin.site.register(Dispositivo,DispositivoAdmin)
admin.site.register(Agendamento,AgendamentoAdmin)
admin.site.register(Consumo,ConsumoAdmin)
