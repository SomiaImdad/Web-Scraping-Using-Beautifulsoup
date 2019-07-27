import bs4 as bs
import urllib.request
import pandas as pd
import datetime

source = urllib.request.urlopen('https://www.brecorder.com/exchange-rates/')
soup = bs.BeautifulSoup(source, 'lxml')

table = soup.findAll('div', class_='box')

today = datetime.date.today()
dates = today.strftime('%d-%m-%Y')

_date = []
countries = []
currencies = []
sell = []
buy_tt = []
buy_od = []

for data in table:
    _date.append(dates)
    countries.append(data.find('div', class_='currency').getText())
    currencies.append(data.find('div', class_='country').getText())
    sell.append(data.find('div', class_='sell').getText())
    buy = data.findAll('div', class_='buy')
    buy_tt.append(buy[0].getText())
    buy_od.append(buy[1].getText())

column_names = ['Date' , 'Country','Currency','Selling_TT_OD','Buying_TT_Clear','Buying_OD_TCHQ']

df = pd.DataFrame(list(zip(_date , countries, currencies, sell, buy_tt, buy_od)))

df.drop(0, inplace= True)

df.columns = column_names

print(df)
