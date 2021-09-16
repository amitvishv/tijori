from django.db import models


class Company(models.Model):
    fincode = models.IntegerField()
    name = models.CharField(max_length=50, null=True, blank=True)
    symbol = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class IntradayPrice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.FloatField()
    date_time = models.DateTimeField()

    def __str__(self):
        return self.company.symbol

class HistoricPrice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.FloatField()
    date_time = models.DateTimeField()

    def __str__(self):
        return self.company.symbol