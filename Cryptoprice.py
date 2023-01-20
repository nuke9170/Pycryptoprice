import json
import requests
import time
from datetime import datetime

# Binance API URL
key = "https://api.binance.com/api/v3/ticker/price?symbol="

currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT","ETHUSDT","BNBUSDT","SOLUSDT"]

for b in range (1440):
    j = 0
    time.sleep(60)
    now=datetime.now()
    ct=now.strftime("%H:%M:%S")
    with open(r'C:\Users\NuKe\Desktop\Cryptoprice.txt', 'a',encoding='utf-8')as f:
        f.writelines("At time : "+ct+"\n") 
        for i in currencies:
        
            url = key+currencies[j]
            data = requests.get(url)
            data = data.json()
            j = j+1
            print(f"{data['symbol']} price is {data['price']}")
            f.writelines(f"{data['symbol']} price is {data['price']}\n")
        f.writelines("\n")    
        f.close()
    

   




        


