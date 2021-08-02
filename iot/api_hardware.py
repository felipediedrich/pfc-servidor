from django.views import View
from django.http import JsonResponse
import json
from .models import Dispositivo
from django.http import HttpResponseBadRequest
from datetime import datetime

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class OnOff(View):
    def post(self, request, mac):

        dispositivo = Dispositivo.objects.filter(mac=mac).first()

        if dispositivo == None: return JsonResponse({"message":"MAC Address don't exist!"}, status=400)
        elif 'status' not in request.POST: return JsonResponse({"message":"Status don't sended!"}, status=400)
        elif request.POST['status'] not in ['0','1']: return JsonResponse({"message":"Invalid, send status equals '1' or '0'"}, status=400)
        
        elif request.POST['status'] == '1':
            dispositivo.status = True
            dispositivo.save()
            return JsonResponse({'message':'ok','status':1}, status=200)

        elif request.POST['status'] == '0':
            dispositivo.status = False
            dispositivo.save()
            return JsonResponse({'message':'ok','status':0}, status=200)

    def get(self, request, mac):
        dispositivo = Dispositivo.objects.filter(mac=mac).first()

        if dispositivo == None: return JsonResponse({"message":"MAC Address don't exist!"}, status=400)
        elif not dispositivo.status: msg = JsonResponse({"status": 0 })
        else: msg = JsonResponse({"status": 1 })

        dispositivo.last_ping = datetime.now()
        dispositivo.save()

        return msg
