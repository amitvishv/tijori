from django.http import JsonResponse
from django.views import View
from api.models import HistoricPrice, IntradayPrice


# GET /api/company/<fincode>/current_price/
class CurrentPriceViews(View):
    def get(self, request, fincode):
        data = IntradayPrice.objects.filter(company__fincode=fincode).order_by('-date_time').values('company__symbol',
                                                                                                    'company__fincode',
                                                                                                    'company__name',
                                                                                                    'price',
                                                                                                    'date_time')[0]
        return JsonResponse({'response': list(data)}, status=200, safe=False)


# GET / api / company / < fincode > / historical_prices /
class HistoricalPriceViews(View):
    def get(self, request, fincode):
        data = HistoricPrice.objects.filter(company__fincode=fincode).order_by('-date_time').values('company__symbol',
                                                                                                    'company__fincode',
                                                                                                    'company__name',
                                                                                                    'price',
                                                                                                    'date_time')
        return JsonResponse({'response': list(data)}, status=200, safe=False)
