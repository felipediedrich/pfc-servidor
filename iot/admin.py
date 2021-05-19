from django.contrib import admin

from iot.models import Dispositivo, Agendamento

class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('name','status','user')
    list_filter = ('user',)

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('name','horario')

admin.site.register(Dispositivo,DispositivoAdmin)
admin.site.register(Agendamento,AgendamentoAdmin)
