import requests
from io import StringIO
import csv

Stock_list = None
data_list = None

def getInfo():
    global Stock_list, data_list
    response = requests.get('https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data')
    file = StringIO(response.text,newline='')
    csvReader = csv.DictReader(file)
    data_list = list(csvReader)
    StockName_Temp = set()
    for item in data_list:
        StockName_Temp.add(item['證券名稱'])
    Stock_list = sorted(list(StockName_Temp))


getInfo()