from django.contrib import admin
from api.models import Company, HistoricPrice, IntradayPrice

# Register your models here.
admin.site.register(Company)
admin.site.register(HistoricPrice)
admin.site.register(IntradayPrice)
