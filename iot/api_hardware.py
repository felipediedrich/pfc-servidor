from django.views import View
from django.http import JsonResponse
import json
from .models import Dispositivo, Agendamento
from django.http import HttpResponseBadRequest, HttpResponse
import pytz
from datetime import datetime, timedelta
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class OnOff(View):
    def post(self, request, mac):

        dispositivo = Dispositivo.objects.filter(mac=mac).first()
        parameters = json.loads(request.body)

        if dispositivo == None: return JsonResponse({"message":"MAC Address don't exist!"}, status=400)
        elif 'status' not in parameters: return JsonResponse({"message":"Parameter 'status' don't sended!"}, status=400)
        elif parameters['status'] not in [0,1]: return JsonResponse({"message":"Invalid, send status equals 1 or 0"}, status=400)
        elif parameters['status'] == 1:
            dispositivo.status = True
            dispositivo.last_ping = datetime.now()
            dispositivo.save()
            return JsonResponse({'message':'ok','status':1}, status=200)

        elif parameters['status'] == 0:
            dispositivo.status = False
            dispositivo.last_ping = datetime.now()
            dispositivo.save()
            return JsonResponse({'message':'ok','status':0}, status=200)

    def get(self, request, mac):
        dispositivo = Dispositivo.objects.filter(mac=mac).first()

        if dispositivo == None: return JsonResponse({"message":"MAC Address don't exist!"}, status=400)

        # Parameters
        last_ping = dispositivo.last_ping.astimezone(pytz.timezone('America/Sao_Paulo')).time()
        now = datetime.now().time()
        weekday = str((datetime.now() + timedelta(days=1)).weekday())

        agendamento = Agendamento.objects.filter(dispositivo__mac = mac,horario__gte = last_ping,horario__lte = now,repetir__contains = weekday).first()

        if agendamento != None:
            dispositivo.status = agendamento.modo
            if "T" in agendamento.repetir: agendamento.delete()

        dispositivo.last_ping = datetime.now()
        dispositivo.save()

        if not dispositivo.status: return JsonResponse({"status": 0 })
        else: return JsonResponse({"status": 1 })

