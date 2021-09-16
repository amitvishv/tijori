from api.models import Company, HistoricPrice, IntradayPrice
from datetime import datetime
import re
datetimeformat = '%Y-%m-%d %H:%M:%S.%f'
filenames = [ 'companies.ace', 'intraday_prices.ace', 'historical_prices.ace']
for filename in filenames:
    print("filename --->", filename)
    with open(filename) as f:
        lines = f.readlines()
        for i in lines:
            if '<<row>>' in i:
                data = re.split('<<row>>|<</row>>', i)[1]
                if 'companies' in filename:
                    fincode, company_name, symbol = data.split('|')
                    Company.objects.create(fincode=fincode, name=company_name, symbol=symbol)
                if 'intraday' in filename:
                    symbol, price, date_time = data.split('|')
                    symbol_obj = Company.objects.get(symbol=symbol)
                    IntradayPrice.objects.create(company=symbol_obj, price=price, date_time=datetime.strptime(date_time, datetimeformat))

                if 'historical_prices' in filename:
                    fincode, date_time, price = data.split('|')
                    fincode_obj = Company.objects.get(fincode=fincode)
                    HistoricPrice.objects.create(company=fincode_obj, price=price, date_time=datetime.strptime(date_time, datetimeformat))
print("Success")