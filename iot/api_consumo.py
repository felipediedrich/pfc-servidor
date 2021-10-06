from django.views import View
from django.http import JsonResponse
# from pandas.core.resample import resample
from .models import Consumo
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

@method_decorator(csrf_exempt, name='dispatch')
class SeriesConsumo(View):
    def get(self, request, mac, freq):

        # Posible frequencies: H, D, M
        if freq.lower() not in ['h','d','w','m']: return JsonResponse({"message":"Frequency not in ('h','w','d','m')"}, status=400)
    
        dados = Consumo.objects.filter(dispositivo__mac = mac).values('horario','corrente')
        resample = pd.DataFrame(dados).resample(freq, on='horario').corrente.mean().round(2).fillna('NULL')

        return JsonResponse({'x':resample.index.tolist(),'y':resample.tolist()})
